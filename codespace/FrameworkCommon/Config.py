##System import
import platform

##Framework import


def CheckOSPlatform():
    if platform.system().lower() == "linux" or platform.system().lower() == "linux2":
        return "linux"
    elif platform.system().lower() == "darwin":
        return "darwin"
    elif platform.system().lower() == "windows":
        return "windows"

##System function config
_platform_ = CheckOSPlatform()
dict_systemslash = {"windows":"\\", "darwin":"/", "linux":"/"}
_AvdName_ = ""
_ADBPortNumber_ = "5554"
_UsingEmulator_ = ""
_DeviceNumber_ = ""
_CaseID_ = ""

##Global config （wait time)
_InstantWaitingPeriod_ = 5
_ShortWaitingPeriod_ = 10
_AverageWaitingPeriod_ = 15
_GeneralWaitingPeriod_ = 25
_LongWaitingPeriod_ = 60

##Test data
_TestCaseRegion_ = ""
_TestCasePlatform_ = ""
_TestCaseFeature_ = ""

##Android config
_AppiumProcesslID_ = ""
_AppiumPort_ = 10000
AppiumTriggerCommand = "appium -p " + str(_AppiumPort_) + " --base-path /wd/hub --log ./appium_log/appium_log.log"
desired_caps_no_app = {
    'platformName': 'Android',  ##平台名稱
    'platformVersion': '12',  ##Android OS 版本
    'deviceName': 'Android Emulator', ##設備id，如果用實體機這裡就要填實體機id，emulator的話隨便填
    'automationName': 'UiAutomator2' ##使用的自動化引擎，目前是使用UiAutomator2
}
desired_caps_with_app = {
    'platformName': 'Android',  ##平台名稱
    'platformVersion': '12',  ##Android OS 版本
    'deviceName': 'Android Emulator', ##設備id，如果用實體機這裡就要填實體機id，emulator的話隨便填
    "appPackage": "com.example.android", ##更換成目標應用的包名
    "appActivity": "com.example.android.Main", ##更換成目標應用的主活動名稱
    "automationName": "UiAutomator2",  ##指定自動化引擎為UiAutomator2
    "noReset": False,  ##是否reset，那因為我們的app會有登入記錄cache，所以應重置
    "autoGrantPermissions": True ##自動賦予該app所有權限
}
