#!/usr/bin/python3

class CountedIterator(iter):
    def __init__(self, iter_object, counter):
        self.iter_object = iter_object
        self.counter = counter

    def iter_object(self):
        