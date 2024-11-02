##System import
import os
import subprocess
import json
import getopt
import sys
import time

##Framework import
from codespace.FrameworkCommon.Logger import InitialDebugLog
import codespace.FrameworkCommon.GlobalVariables as GlobalVariables
import codespace.FrameworkCommon.Config as Config

_OPT_ = {}
opts, args = getopt.getopt(sys.argv[1:], 'E:N:P:T:S:R:HX', ["step"])

##Error handle for input parameter
if sys.argv[1:]:
    for name, value in opts:
        if '-T' in name:
            Config._CaseID_ = value
        _OPT_[name] = value
        if '-E' in name:
            ##lanuch emulator
            Config._UsingEmulator_ = True

            ##Store avd value
            Config._AvdName_ = value

            if Config._platform_ == 'windows':
                command = "emulator @" + value + ' -port ' + str(int(value.split('_')[-1]) * 2 + 5552)
                Config._DeviceNumber_ = int(value.split('_')[-1])
                emulator_process = subprocess.Popen(command)
            elif Config._platform_ == 'darwin' or Config._platform_ == 'linux':
                command = "cd $ANDROID_HOME/emulator; emulator @" + value
                emulator_process = subprocess.Popen(command, shell=True)
            time.sleep(90)
        if '-S' in name:
            Config._EnvType_ = value
        if '-H' in name:
            ##Using headless mode
            Config._Headless_ = True
        if '-P' in name:
            Config._TriggerCaseMode_ = value.lower()
        if '-R' in name:
            Config._RemoteSeleniumDriver_ = value

def OK(actual_result, expect_result, message = ""):
    if actual_result == expect_result:
        print(f"[OK, {actual_result} == {expect_result}] {message}")
        GlobalVariables._Logger_.info(f"[OK, {actual_result} == {expect_result}] {message}")
        assert True
    else:
        print(f"[Fail, {actual_result} != {expect_result}] {message}")
        GlobalVariables._Logger_.error(f"[Fail, {actual_result} != {expect_result}] {message}")
        assert False

def GetTriggerProcessPID(command):
    #get_pid_command = "pgrep -f " + "\'" + command + "\'"
    result = subprocess.run(['pgrep', '-f', command], stdout=subprocess.PIPE, text=True)

    ##Get result
    process_id = result.stdout
    GlobalVariables._Logger_.info("Process id get : " + str(process_id))
    return process_id

def KillProcessByPID(pid):
    '''
        KillProcessByPID : kill process by process id
            Input argu :
                pid: pid of process
            Return code: N/A
    '''

    ##Kill process by process ID list
    if Config._platform_ == 'windows':
        cmd = "taskkill /pid " + str(pid) + " /t /f"
    elif Config._platform_ == 'darwin':
        cmd = "kill -9 " + str(pid)

    GlobalVariables._Logger_.info("killing task -> command: " + cmd)
    os.system(cmd)

def FilterCaseRegionAndPlatform(testcasetype):
    ''' 
        FilterCaseRegionAndPlatform : Filter platform / feature name from trggered command
            Input:
                testcasetype: test case type (Ex. WebTest)
    '''
    platform = ""
    platform_group = ["Web", "Android", "API"]

    ##Filter case platform
    for each_platform in platform_group:
        if each_platform in testcasetype:
            GlobalVariables._Logger_.info("Config._TestCaseType_ = %s" % (testcasetype))
            GlobalVariables._Logger_.info("platform = %s" % (each_platform))
            platform = each_platform
            break
        else:
            #GlobalVariables.CommonVar._GlobalLogger_.error("Config._TestCaseType_ = %s" % (testcasetype))
            platform = "Please Check your test case platform is correct !!!!"

    ##Filter test case feature name
    if platform in platform_group:
        feature = testcasetype.split(platform)[-1]
        GlobalVariables._Logger_.info("feature = %s" % (feature))
    else:
        feature = ""
        GlobalVariables._Logger_.info("feature = %s" % (feature))
        GlobalVariables._Logger_.error("Please Check your test case platform is correct !!!!")
        print("Please Check your test case region/platform is correct !!!!")

    return platform, feature

def LoadXpathJsonData():
    '''
        LoadXpathJsonData: Get json data of xpath
            Input:
                N/A
            Return code : N/A
    '''
    ##Load json to data
    try:
        file_path = os.path.join("Data", "Xpath", "AllPath.json")
        with open(file_path, 'r', encoding='utf-8') as file:
            GlobalVariables._XpathJsonData_ = json.load(file)
    except FileNotFoundError:
        GlobalVariables._Logger_.info("File not found error.")
    except:
        GlobalVariables._Logger_.info("Encounter unknown exception.")

def LoadFunctionJsonData():
    '''
        LoadFunctionJsonData: Get function json data
            Input:
                N/A
            Return code : N/A
    '''
    ##Load json to data
    try:
        file_path = os.path.join("Data", "InputJson", "FunctionInput.json")
        with open(file_path, 'r', encoding='utf-8') as file:
            GlobalVariables._FuncJsonData_ = json.load(file)
    except FileNotFoundError:
        GlobalVariables._Logger_.info("File not found error.")
    except:
        GlobalVariables._Logger_.info("Encounter unknown exception.")
