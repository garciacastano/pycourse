#! /usr/bin/env python
#-*- coding: utf-8 -*-
u"""
Created on Nov 13, 2012

@author: pablito56

@license: MIT

@contact: pablito56@gmail.com

Module 07 (descriptors) exercise: Use descriptor protocol to cache an attribute value
"""
#===============================================================================
# EXERCISE: pycourse/advanced/exercises/exercises/mod_07_descriptors/exercise_mod_07
#
# - Use descriptor protocol to cache during a certain TTL the return value of a function as an attribute
#
# - Run the tests in 'tests_mod_07.py' executing 'nosetests -v' inside its folder
#
# - Check the solution in module 'solution_mod_07.py'
#===============================================================================


import time


class CachedAttribute(object):
    def __init__(self, name, func, seconds):
        self.name = name
        self.func = func
        self.delta = seconds
        self.expiration = None
        self.cached_result = None

    def __get__(self, inst, cls):
        return self.func(inst)


class CachedAttrClass(object):
    def expensive_operation(self):
        from time import sleep
        from random import seed, random
        sleep(2)
        seed()
        return random()
    cached_attr = CachedAttribute('_cached_attr', expensive_operation, 3)
