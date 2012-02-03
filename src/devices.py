from PyQt4.QtCore import *

import dbus
import uuid
import os

from dbus.mainloop.qt import DBusQtMainLoop

from parse import check_rules

class DeviceManager(object):
    
    def __init__(self):
        self.settings = QSettings()
        self.devices  = {}
        
        self.load_devices()
    
    def load_devices(self):
        self.settings.beginGroup('devices')
        devices_keys = self.settings.childGroups()
        devices = {}

        for key in devices_keys:
            self.settings.beginGroup(key)

            device = {}
            device['name'] = str(self.settings.value('name', 'Unnamed device').toString())
            device['id'] = str(self.settings.value('id').toString())
            
            rules_count = self.settings.beginReadArray('rules')
            rules = []
            for ruleidx in xrange(rules_count):
                self.settings.setArrayIndex(ruleidx)
                rules.append(str(self.settings.value('rule',
                                                     '').toString()).strip())

            self.settings.endArray()

            device['rules'] = rules
            device['exec'] = str(self.settings.value('exec', None).toString())

            devices[device['id']] = device

            self.settings.endGroup()

        self.settings.endGroup()
        self.devices = devices

    def save_devices(self):
        self.settings.beginGroup('devices')
        self.settings.remove('')

        for key, device in self.devices.items():
            self.settings.beginGroup(device['id'])

            self.settings.setValue('name', device['name'])
            self.settings.setValue('id', device['id'])
            
            self.settings.beginWriteArray('rules')

            for ruleidx in xrange(len(device['rules'])):
                self.settings.setArrayIndex(ruleidx)
                self.settings.setValue('rule', device['rules'][ruleidx].strip())
            
            self.settings.endArray()

            self.settings.setValue('exec', device['exec'])

            self.settings.endGroup()

        self.settings.endGroup()

    def new_device(self):
        return {
            'id': str(uuid.uuid4().hex),
            'name': 'Unnamed Device',
            'exec': '/bin/true',
            'rules': []
                }
    
    def save_device(self, dev):
        self.devices[dev['id']] = dev
        self.save_devices()

    def remove_device(self, dev):
        self.load_devices()
        if dev['id'] in self.devices:
            del self.devices[dev['id']]
        self.save_devices()

    def match_device(self, obj):
        for dev in self.devices.values():
            if check_rules(dev['rules'], obj):
                print "Device matched:", dev['name']
                cmd = str(dev['exec'])
                
                for prop in obj:
                    cmd = cmd.replace("{%s}" % prop, obj[prop])

                os.system(cmd)
            else:
                print "Device did not match:", dev['name']

class UDisksManager(object):

    def __init__(self, manager):
        self.device_manager = manager

        DBusQtMainLoop(set_as_default=True)
        self.dbus = dbus.SystemBus()

        self.manager_object = self.dbus.get_object('org.freedesktop.UDisks',
                                            '/org/freedesktop/UDisks')
        self.manager = dbus.Interface(self.manager_object,
                                dbus_interface='org.freedesktop.UDisks')

        self.manager.connect_to_signal("DeviceAdded", self.device_attached)
        self.manager.connect_to_signal("DeviceRemoved", self.device_removed)

        self.registered_signals = {}
        

    def device_removed(self, obj):
        obj = str(obj)
        print "Device removed:",obj
        self.dbus.remove_signal_receiver(self.device_changed,
                                         signal_name='Changed',
                                         dbus_interface='org.freedesktop.UDisks.Device',
                                         path=obj)


    def device_attached(self, obj, sender=None, **kwargs):
        print "Device: ", obj

        dev_obj = self.dbus.get_object('org.freedesktop.UDisks', obj)
        props_if = dbus.Interface(dev_obj,
                            dbus_interface='org.freedesktop.DBus.Properties')

        device_ifn = 'org.freedesktop.UDisks.Device'
        device_if = dbus.Interface(dev_obj, device_ifn)

        
        if self.get_dev_prop(obj, 'DeviceIsPartition'):
            if self.get_dev_prop(obj, 'DeviceIsMounted'):
                self.device_changed(path=obj)
            elif 'Changed' not in self.registered_signals.setdefault(obj, set()):
                device_if.connect_to_signal("Changed", self.device_changed,
                                            dbus_interface=device_ifn,
                                            path_keyword='path')

                self.registered_signals[obj].add('Changed')

    def device_changed(self, path=None, **kwargs):
        print "Device changed:", path

        props = {
            'model': str(self.get_dev_prop(path, 'DriveModel')),
            'vendor': str(self.get_dev_prop(path, 'DriveVendor')),
            'fs_uuid': str(self.get_dev_prop(path, 'IdUuid')),
            'fs_label': str(self.get_dev_prop(path, 'IdLabel')),
            'dev_file': str(self.get_dev_prop(path, 'DeviceFile')),
            'mount_path': str(self.get_dev_prop(path, 'DeviceMountPaths')[0]),
            }

        self.device_manager.match_device(props)

    def get_dev_prop(self, obj, propname):
        device_ifn = 'org.freedesktop.UDisks.Device'
        props_ifn = 'org.freedesktop.DBus.Properties'

        dev_obj = self.dbus.get_object('org.freedesktop.UDisks', obj)
        try:
            return dev_obj.Get(device_ifn, propname, dbus_interface=props_ifn)
        except dbus.connection.Exception:
            return None
