#!/usr/bin/env python3
class LongStringError(Exception):
    def __init__(self, msg, theLength):
        Exception.__init__(self, msg)
        self.theLength = theLength

    def length(self):
        return self.theLength
