##System import
import time

##Framework import
import codespace.FrameworkCommon.FrameworkBase as FrameworkBase

##Initial OK function
def OK(actual_result, expect_result, message):
    return FrameworkBase.OK(actual_result, expect_result, message)

def SleepTime(arg):
    '''
        SleepTime: Sleep time
            Input arg:
                times : time to sleep
    '''
    ret = 1
    times = arg["times"]
    time.sleep(int(times))

    OK(ret, int(arg["result"]), "AndroidBaseUICore.SleepTime -> " + times + " sec")