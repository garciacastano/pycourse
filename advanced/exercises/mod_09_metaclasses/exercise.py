#! /usr/bin/env python
#-*- coding: utf-8 -*-
u"""
Created on Oct 3, 2013

@author: ealogar

@license: MIT

@contact: ealogar@gmail.com

Module 09 (metaclasses) exercise: apply decorators with metaclasses and generate new functionality
"""
#===============================================================================
# EXERCISE: pycourse/advanced/exercises/exercises/mod_09_metaclasses/exercise_mod_09
#
# - Combine a metaclass with a decorator:
#    - We want to measure the execution time of all class methods (excluding __* methods)
#    - Implement a decorator as a function to measure the execution time of a function
#    - Add the execution time to the decorated function as an attribute
#    - Instead of decorating the class, we decorate in metaclass __new__ method every function
#    - We can decide which methods to decorate and which not
#    - Add a function or attributes to show last_execution_time of every method
#    - We can store the execution time in the decorator as an attribute...
#    - We can use metaclass to add methods and attributes
#
# - Run the tests in 'tests.py' executing 'nosetests -v' inside its folder
#
# - Check the solution in module 'solution.py'
#===============================================================================


from time import sleep, time
from random import randint
from functools import wraps
from re import search
from inspect import isfunction, getmembers, ismethod
from copy import copy
from types import MethodType


def measure(f):
    """Simple decorator to measure the execution time of a member function
    It will add the last time as an attribute of the object.
    """

    @wraps(f)
    def wrapper(*args, **kwargs):
        before = time()
        func = f(*args, **kwargs)
        delta = time() - before
        time_internal_var = '_time_{0}'.format(f.__name__)
        setattr(args[0], time_internal_var, delta)

        def ellapsed_time(obj):
            return getattr(obj, time_internal_var, 'na')

        wrapper.last_time = MethodType(ellapsed_time, args[0])
        return func
    return wrapper


def show_execution_time(obj):
    """print by console the attribute last_time of every
    methods of obj who has it available
    """
    for method in getmembers(obj, ismethod):
        if not search(r'^__*', method[0]):
            print 'Method {0} - last execution time {1}'.format(method[0],
                                    getattr(obj, '_time_{0}'.format(method[0]), 'Na'))


class MeasureMetaclass(type):
    """Metaclass to add measures to every method of a class using measure
    decorator.
    It makes available show_execution_time
    e.g:
    >>my_class = SomeClass()
    >>my_class.get_fruits()
    >>my_class.get_dries_fruits()
    >>my_class.show_execution_time()
    """
    def __new__(mcs, classname, bases, attrs_dict):
        for attr, attrval in attrs_dict.iteritems():
            if isfunction(attrval) and not attr.startswith("__"):
                attrs_dict[attr] = measure(attrval)

        attrs_dict["show_execution_time"] = show_execution_time
        return type.__new__(mcs, classname, bases, attrs_dict)


class SomeClass(object):

    __metaclass__ = MeasureMetaclass

    def __init__(self):
        self.fruits = ['apple', 'peach', 'banana', 'strawberry']
        self.dried_fruits = ['peanut', 'nouse', 'almond']

    def get_fruits(self):
        sleep(0.01)  # getting is quick ...
        return copy(self.fruits)

    def add_fruit(self, fruit):
        if fruit not in self.get_fruits():
            sleep(0.1)  # inserting is expensive
            self.fruits.append(fruit)

    def delete_fruit(self, fruit):
        if fruit in self.get_fruits():
            sleep(0.2)
            del self.fruits[fruit]

    def get_dries_fruits(self):
        sleep(randint(0, 100) / 100)
        return copy(self.dried_fruits)
