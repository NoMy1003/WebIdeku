import time
import os
import functools
from functools import wraps
import inspect
import re
import codespace.FrameworkCommon.GlobalVariables as GlobalVariables
import json
#import codespace.FrameworkCommon.Mapper as Mapper
##Do not import Util

class FuncRecorder(object):

    def __init__(self, func):
        self._func = func
        GlobalVariables._CurrentFuncFilename_ = ""
        GlobalVariables._CurrentFuncQualName_ = ""

    #def __call__(self, args):
    def __call__(self, *args, **kwargs):

        ##Log function name before running
        GlobalVariables._Logger_.info("Prepare enter %s" % (self._func.__name__))
        GlobalVariables._Logger_.info(f"{args}, {kwargs}")

        ##Record function time
        ##Start time
        time_first = time.time()

        ##Get function filename and real name
        GlobalVariables._CurrentFuncFilename_ = re.split(r"[.;/]", self._func.__code__.co_filename)[-2]
        GlobalVariables._CurrentFuncQualName_ = self._func.__qualname__

        ##Execute function
        #self._func(args)
        self._func(*args, **kwargs)

        ##End time
        time_second = time.time()

        ##Log function name after running
        GlobalVariables._Logger_.info("Leave %s at %.2f sec" % (self._func.__name__, time_second-time_first))
        GlobalVariables._Logger_.info("Get function filename: " + GlobalVariables._CurrentFuncFilename_)
        GlobalVariables._Logger_.info("Get function real name: " + GlobalVariables._CurrentFuncQualName_)


def FuncRecorderMod(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        GlobalVariables._CurrentFuncQualName_ = func.__qualname__
        GlobalVariables._CurrentFuncFilename_ = re.split(r"[.;/\\\r]", func.__code__.co_filename)[-2]

        return func(*args, **kwargs)
    return wrapper

def TestRecorderMod(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        GlobalVariables._CurrentTestQualName_ = func.__qualname__
        GlobalVariables._CurrentTestFilename_ = re.split(r"[.;/\\\r]", func.__code__.co_filename)[-2]

        return func(*args, **kwargs)
    return wrapper