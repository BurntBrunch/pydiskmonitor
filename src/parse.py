#!/usr/bin/env python
# coding: utf-8

from pyparsing import Word, Optional, ZeroOrMore, alphanums, Literal, StringEnd

def parse_rule(rule):
    """ Given a rule string, return a key-value pair """

    result = []
    def got_pair(tokens):
        result.append(tuple(tokens[-2:]))

    possibleChars = alphanums+"_-/^&*'"

    keyOrValue = Optional(Literal('"').suppress()) + Word(possibleChars) + Optional(Literal('"').suppress())
    keyValuePair = keyOrValue + Literal("=").suppress() + keyOrValue
    keyValuePair.setParseAction(got_pair)
    line = keyValuePair + ZeroOrMore(Literal(',').suppress() + keyValuePair) + StringEnd()

    try:
        line.parseString(rule)
        return result
    except:
        return None

def check_rule(rule, obj):
    """ Rule is a list of key-value tuples,
        obj is the object to check against """

    if rule is None:
        return False

    def key_check((k, v)):
        if k in obj:
            return obj[k] == v
        elif hasattr(obj, k):
            return getattr(obj,k) == v
        else: 
            return False

    return all(map(key_check, rule))

def check_rules(rules, obj):
    """ Rules is a list of strings,
        obj is the object to check against """

    return any(map(lambda rule: check_rule(parse_rule(rule), obj), rules))


if __name__ == "__main__":
    t = ['a = b, c = d',
         'a=b,c=d,e=f',
         'a = c,',
         'a = d, b =']

    for test in t:
        try:
            print test, 
            print parse_rule(test)
        except:
            print "failed"

    obj = { 'a': 'b', 'e': 'f' }
    print obj

    t = ['a=b',
         'a=b,c=d',
         'a=b,c=d,e=f',
         'a=b,e=f']

    for test in t:
        try:
            print test,
            print check_rules((test,), obj)
        except:
            print "failed"
