##System import
from datetime import datetime
import configparser
import pytest
import os
import time
import re
from webdriver_auto_update.chrome_app_utils import ChromeAppUtils
from webdriver_auto_update.webdriver_manager import WebDriverManager

##Framework import
import codespace.FrameworkCommon.FrameworkBase as FrameworkBase
import codespace.FrameworkCommon.GlobalVariables as GlobalVariables
import codespace.FrameworkCommon.Config as Config

##-T 後面輸入[case_name] - [case_id]
GlobalVariables.Framework._CaseList_ = re.split(',', FrameworkBase._OPT_['-T'])

def CheckChromedriverUpdate(driver_path):
    '''
        CheckChromedriverUpdate - Check if chromedriver is latest version
            Input argu:
                driver_path - chromedriver path
    '''
    try:
        ##Create an instance of WebDriverManager
        driver_manager = WebDriverManager(driver_path)

        ##Call the main method to manage chromedriver
        driver_manager.main()
    except Exception as e:
        GlobalVariables._Logger_.info(e)

def InitialPytestLogfile():
    '''
        InitialPytestLogfile - Initialize pytest.ini file
            Input argu:
                N/A
    '''
    ##Overwrite log_file filename in pytest.ini with datetime
    GlobalVariables._CurrentLogTime_ = datetime.now().strftime("%Y%m%d%H%M%S")

    test_config = configparser.ConfigParser()
    test_config.read('pytest.ini')
    pytest_log_path = f".{Config.dict_systemslash[Config._platform_]}Pytest_Log{Config.dict_systemslash[Config._platform_]}Pytest-{GlobalVariables._CurrentLogTime_}-logs.log"

    ##Update the string at log_file to with latest datetime
    #test_config.set('pytest', 'log_file', './pytest_logs/Pytest-{}-logs.log'.format(curr_datetime))
    test_config.set('pytest', 'log_file', pytest_log_path)

    with open('pytest.ini', 'w') as configfile:
        test_config.write(configfile)


class Test():
    def __init__(self):

        ##Initial pytest log
        InitialPytestLogfile()

    ##python3 -m pytest codespace/Testsuites/test_unit_example.py
    def RUN(self):

        ##Insure chromedriver version (precondition for web automation)
        CheckChromedriverUpdate('C:\chromedriver')

        ##Initialize testsuites path and set up testsuites
        current_path = os.path.dirname(__file__)
        start_path = os.path.join(current_path, 'codespace/Testsuites')
        GlobalVariables._Logger_.info(start_path)

        ##Get and run case list
        run_cases = []
        for i in range(len(GlobalVariables.Framework._CaseList_)):
            ##Get case name and id from case list
            case_name = GlobalVariables.Framework._CaseList_[i].split('-')[0]
            case_id = ""
            cases = []

            ##Case with case number
            if '-' in GlobalVariables.Framework._CaseList_[i]:
                case_id = GlobalVariables.Framework._CaseList_[i].split('-')[1]

                ##Store case data to Config
                Config._TestCasePlatform_, Config._TestCaseFeature_ = FrameworkBase.FilterCaseRegionAndPlatform(case_name)

                ##Append cases with [test module]::[test class]::[test function]
                cases.append("test_" + case_name + ".py::" + "Test" + case_name + "::" + "test_" + case_name + case_id)

                ##Check if input correct and add prefix (Test module path)
                for case_number in range(len(cases)):
                    if "test_" + case_name + case_id[0:4] in cases[case_number]:
                        #run_cases.append('codespace/Testsuites/' + cases[case_number])
                        run_cases.append(os.path.join("codespace", "Testsuites", cases[case_number]))

            ##Case without case number (run all test under class)
            else:
                ##Store case data to Config
                Config._TestCasePlatform_, Config._TestCaseFeature_ = FrameworkBase.FilterCaseRegionAndPlatform(case_name)

                ##Append cases with [test module]::[test class]::[test function]
                cases.append("test_" + case_name + ".py::" + "Test" + case_name)

                ##Check if input correct and add prefix (Test module path)
                for case_number in range(len(cases)):
                    if "test_" + case_name in cases[case_number]:
                        #run_cases.append('codespace/Testsuites/' + cases[case_number])
                        run_cases.append(os.path.join("codespace", "Testsuites", cases[case_number]))


        if run_cases:
            pytest.main([*run_cases, "-v", "--alluredir", "target/allure-results/" + GlobalVariables._CurrentLogTime_, "-s", "--cache-clear", "--clean-alluredir"])
        else:
            GlobalVariables._Logger_.info("No cases found")

##Get start time
stime = time.time()

if __name__ == '__main__' :
    ##Load framework xpath
    FrameworkBase.LoadXpathJsonData()

    AP = Test()
    AP.RUN()