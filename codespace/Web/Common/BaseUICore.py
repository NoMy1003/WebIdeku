##Import system library
import time
import logging
import sys
from datetime import datetime
from xml.parsers.expat import ParserCreate, ExpatError, errors
import xml.etree.ElementTree as ET
from email import message
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

##Import framework library
import codespace.FrameworkCommon.FrameworkBase as FrameworkBase
import codespace.FrameworkCommon.Logger as Logger
import codespace.FrameworkCommon.GlobalVariables as GlobalVariables
import codespace.FrameworkCommon.DecoratorHelper as DecoratorHelper

chromedriver = 'C:\chromedriver\chromedriver.exe'
edgedriver = 'C:\chromedriver\chromedriver.exe'
start_time = time.time()

STANDARD_TIME = 15
_WebDriver_ = ""

def OK(actual_result, expect_result, function_name):
    FrameworkBase.OK(actual_result, expect_result, function_name)

@DecoratorHelper.FuncRecorder
def InitialWebDriver(arg):
    '''
        InitialWebDriver - Start web driver and setup initial status
            Input : N/A
    '''
    ret = 1
    global _WebDriver_

    try:
        ##Chrome
        service = Service(executable_path=chromedriver)
        options = EdgeOptions()
        options.add_argument("--incognito")
        options.add_argument("--start-maximized")
        #_WebDriver_ = webdriver.Chrome(service=service,options=options)
        service = Service(EdgeChromiumDriverManager().install())
        _WebDriver_ = webdriver.Edge(service=service,options=options)

    except WebDriverException:
        ret = 0
        GlobalVariables._Logger_.exception("Encounter webdriver exception")
    except Exception as e:
        ret = -1
        GlobalVariables._Logger_.exception(e)

    OK(ret, int(arg["result"]), "InitialWebDriver")

@DecoratorHelper.FuncRecorder
def DeinitialWebDriver():
    '''
        DeinitialWebDriver - Start web driver and setup initial status
            Input : N/A
            Output :
                1 - success
                0 - expect exception
                -1 - unknown exception
            
    '''
    ret = 1
    global _WebDriver_

    try:
        _WebDriver_.delete_all_cookies()
        time.sleep(1)
        _WebDriver_.quit()

    except AttributeError:
        GlobalVariables._Logger_.info("Please initial web driver first, maybe web driver is closed in script fail or tear down")
        GlobalVariables._Logger_.info("Set variable _WebDriver_ => None")
        _WebDriver_ = None

    except WebDriverException:
        GlobalVariables._Logger_.exception("Encounter webdriver exception. Maybe wedriver is crashed / closed / connection error. Please check log for more informaion.")
        GlobalVariables._Logger_.info("Set variable _WebDriver_ => None")
        _WebDriver_ = None

    except:
        GlobalVariables._Logger_.exception('Got exception error')
        GlobalVariables._Logger_.info("Set variable _WebDriver_ => None")
        _WebDriver_ = None

@DecoratorHelper.FuncRecorder
def SleepTime(arg):
    '''
        SleepTime - Start web driver and setup initial status
            Input : N/A
            Output :
                1 - success
                0 - expect exception
                -1 - unknown exception
    '''
    ret = 1
    second = int(arg["second"])

    try:
        time.sleep(second)
    except:
        ret = -1
        GlobalVariables._Logger_.debug("Encounter unknown exception")

    OK(ret, int(arg["result"]), "SleepTime")

@DecoratorHelper.FuncRecorder
def RedirectToUrl(arg):
    '''
        RedirectToUrl - Redirect to url
            Input :
                url - url to redirect to
            Output :
                1 - success
                0 - expect exception
                -1 - unknown exception
    '''
    ret = 1
    url = arg["url"]

    try:
        _WebDriver_.get(url)
        WebDriverWait(_WebDriver_, STANDARD_TIME).until(lambda _WebDriver_: _WebDriver_.execute_script('return document.readyState') == 'complete')
        time.sleep(3)
    except:
        ret = -1
        GlobalVariables._Logger_.exception("Encounter exceptions")

    OK(ret, int(arg["result"]), "RedirectToUrl")

@DecoratorHelper.FuncRecorder
def SwitchBrowserWindow(arg):
    '''
        SwitchBrowserWindow - Switch browser window
            Input :
                page_id - 0 (first page) / 1 (second page) / -1 (last page)
            Output :
                1 - success
                0 - expect exception
                -1 - unknown exception
    '''
    ret = 1
    page_id = arg["page_id"]

    try:
        ##Switch to specific browser page
        handles = _WebDriver_.window_handles
        _WebDriver_.switch_to.window(handles[int(page_id)])
    except:
        ret = -1
        GlobalVariables._Logger_.exception("Encounter exceptions")

    OK(ret, int(arg["result"]), "SwitchBrowserWindow")

@DecoratorHelper.FuncRecorder
def CloseBrowserWindow(arg):
    '''
        CloseBrowserWindow - Close current browser window
            Input :
                N/A
            Output :
                1 - success
                0 - expect exception
                -1 - unknown exception
    '''
    ret = 1

    try:
        ##Close current browser window
        _WebDriver_.close()
    except:
        ret = -1
        GlobalVariables._Logger_.exception("Encounter exceptions")

    OK(ret, int(arg["result"]), "CloseBrowserWindow")

@DecoratorHelper.FuncRecorder
def Click(arg):
    '''
        Click - Click action on element
            Input :
                mode - xpath / javascript
                locate - xpath of click element
                message - click message
    '''
    ret = 1
    mode = arg["mode"]
    locate = arg["locate"]
    message = arg["message"]

    try:
        if mode == "xpath":
            WebDriverWait(_WebDriver_, STANDARD_TIME).until(EC.presence_of_element_located((By.XPATH, locate))).click()
        elif mode == "javascript":
            button = WebDriverWait(_WebDriver_, STANDARD_TIME).until(EC.presence_of_element_located((By.XPATH, locate)))
            _WebDriver_.execute_script("arguments[0].click();", button)
    except:
        ret = -1
        GlobalVariables._Logger_.exception("Encounter exceptions")

    OK(ret, int(arg["result"]), "Click -> [Message] " + message)

@DecoratorHelper.FuncRecorder
def Input(arg):
    '''
        Input - Input action on element
            Input :
                locate - xpath of input element
                value - input value
    '''
    ret = 1
    locate = arg["locate"]
    value = arg["value"]

    try:
        WebDriverWait(_WebDriver_, STANDARD_TIME).until(EC.presence_of_element_located((By.XPATH, locate))).send_keys(value)
    except:
        ret = -1
        GlobalVariables._Logger_.exception("Encounter exceptions")

    OK(ret, int(arg["result"]), "Input -> [Value] " + value)

@DecoratorHelper.FuncRecorder
def MoveToElementAndClick(arg):
    '''
    MoveToElementAndClick : Move to a location and click it's subitem which is hidden in dropdown or comment
            Input argu :
                locate - Position of the main item
                locatehidden - Position of the hidden data item
            Return code :
                1 - success
                0 - fail
                -1 - error
    '''
    locate = arg['locate']
    locatehidden = arg['locatehidden']
    ret = 1
    message = ""

    ##Initial action by webdriver
    action = ActionChains(_WebDriver_)

    try:
        ##Get element
        element = _WebDriver_.find_element("xpath", locate)

        ##Move to first element
        action.move_to_element(element).perform()
        time.sleep(1)

        ##Wait element appear by method
        GlobalVariables._Logger_.info("Enter xpath method")
        wait = WebDriverWait(_WebDriver_, STANDARD_TIME).until(EC.visibility_of_element_located((By.XPATH, locatehidden)))

        ##Move to second element
        action.move_to_element(wait).click().perform()

    except NoSuchElementException:
        message = "No such element. Element xpath => %s" % (locate)
        GlobalVariables._Logger_.exception(message)
        #GetElementTreeAndCompare({"locate":locate})
        ret = -1

    except TimeoutException:
        message = "Cannot find element in %s seconds. Element xpath => %s" % (STANDARD_TIME, locate)
        GlobalVariables._Logger_.exception(message)
        #GetElementTreeAndCompare({"locate":locate})
        ret = -1

    except WebDriverException:
        message = "Encounter webdriver exception. Maybe wedriver is crashed / closed / connection error."
        GlobalVariables._Logger_.exception(message)
        ret = -1

    except:
        message = "Encounter unknown exception."
        GlobalVariables._Logger_.exception(message)
        ret = -1

    OK(ret, int(arg['result']), 'MoveToElementAndClick->' + message)

@DecoratorHelper.FuncRecorder
def PageHasLoaded(arg):
    '''
    PageHasLoaded : Check DOM status code and wait for the page is fully loaded.
            Input argu : N/A
            Return code :
                1 - success
                0 - fail
                -1 - error
    '''
    ret = 0
    message = ""

    ##Get current time
    start_time = time.time()

    try:
        ##Check webpage status in 60 seconds
        while time.time() < start_time + 60:
            page_state = _WebDriver_.execute_script('return document.readyState;')

            ##Page status is interactive
            if page_state in ('interactive', 'complete'):
                GlobalVariables._Logger_.info("DOM is now interactive, total waiting time is %s" % (start_time))
                ret = 1
                break

            ##Page status is not interactive, wait and keep checking
            else:
                time.sleep(0.1)
                GlobalVariables._Logger_.info("DOM is not fully loaded yet, current waiting time is %s" % (start_time))

    except WebDriverException:
        message = "Encounter webdriver exception. Maybe wedriver is crashed / closed / connection error."
        GlobalVariables._Logger_.exception(message)
        ret = -1

    except:
        message = "Encounter unknown exception."
        GlobalVariables._Logger_.exception(message)
        ret = -1

    OK(ret, int(arg['result']), 'PageHasLoaded->' + message)

def CheckElementExist(arg):
    '''
    CheckElementExist : Check the element exist or not
            Input argu :
                locate - Position in web
                passok - 1 (enter "OK" function) / 0 (won't enter "OK" function, return True / False)
            Return code :
                1 - success
                0 - fail
                -1 - error
    '''
    ret = 1
    locate = arg["locate"]
    message = ""
    GlobalVariables._Logger_.info("Enter CheckElementExist")
    GlobalVariables._Logger_.info("locate = %s" % (locate))

    ##Delclare passok argument, if not pass in argument, set it to default value "1"
    try:
        passok = arg["passok"]
    except KeyError:
        passok = "1"
        GlobalVariables._Logger_.info('KeyError - passok default is 1')
    except:
        passok = "1"
        GlobalVariables._Logger_.info('Other error - passok default is 1')
    finally:
        GlobalVariables._Logger_.info("passok = %s" % (passok))

    ##Locate element by specific method, use presence_of_element_located wait util element display in [STANDARD_TIME] seconds
    try:
        WebDriverWait(_WebDriver_, STANDARD_TIME).until(EC.presence_of_element_located((By.XPATH, (locate))))

        if int(arg["result"]):
            message = "Element xpath exists : %s" % (locate)

    ##Can not locate element in timeout exception
    except TimeoutException:
        message = "Cannot find element in %s seconds. Element xpath : %s" % (STANDARD_TIME, locate)
        GlobalVariables._Logger_.exception(message)
        ret = 0

    ##Can not locate element in unknown exception
    except:
        message = "Encounter unknown exception."
        GlobalVariables._Logger_.exception(message)
        ret = -1

    ##If passok is 1, enter ok function to end function, or return ret to checkout result in other function
    if int(passok):
        OK(ret, int(arg['result']), 'CheckElementExist -> ' + message)
    else:
        return ret

@DecoratorHelper.FuncRecorder
def SendKeyboardEvent(arg):
    '''
    SendKeyboardEvent : Send keyboard event and combinations to path (xpath only).
            Input argu :
                locate - path
                sendtype - choose what kind of keys you want to send, ctrl+"a"/ctrl+"c"/ctrl+"x"/ctrl+"v"/Del/Enter/Back/Tab/Down
            Return code :
                1 - success
                0 - fail
                -1 - error
    '''
    locate = arg["locate"]
    sendtype = arg["sendtype"]
    message = "Send type %s" % (sendtype)
    ret = 1

    try:

        if sendtype == "select all":
            WebDriverWait(_WebDriver_, STANDARD_TIME).until(EC.visibility_of_element_located((By.XPATH, (locate)))).send_keys(Keys.CONTROL,'a')
        elif sendtype == "copy":
            WebDriverWait(_WebDriver_, STANDARD_TIME).until(EC.visibility_of_element_located((By.XPATH, (locate)))).send_keys(Keys.CONTROL,'c')
        elif sendtype == "cut":
            WebDriverWait(_WebDriver_, STANDARD_TIME).until(EC.visibility_of_element_located((By.XPATH, (locate)))).send_keys(Keys.CONTROL,'x')
        elif sendtype == "paste":
            WebDriverWait(_WebDriver_, STANDARD_TIME).until(EC.visibility_of_element_located((By.XPATH, (locate)))).send_keys(Keys.CONTROL,'v')
        elif sendtype == "delete":
            WebDriverWait(_WebDriver_, STANDARD_TIME).until(EC.visibility_of_element_located((By.XPATH, (locate)))).send_keys(Keys.DELETE)
        elif sendtype == "enter":
            WebDriverWait(_WebDriver_, STANDARD_TIME).until(EC.visibility_of_element_located((By.XPATH, (locate)))).send_keys(Keys.ENTER)
        elif sendtype == "back":
            WebDriverWait(_WebDriver_, STANDARD_TIME).until(EC.visibility_of_element_located((By.XPATH, (locate)))).send_keys(Keys.BACK_SPACE)
        elif sendtype == "tab":
            WebDriverWait(_WebDriver_, STANDARD_TIME).until(EC.visibility_of_element_located((By.XPATH, (locate)))).send_keys(Keys.TAB)
        elif sendtype == "down":
            WebDriverWait(_WebDriver_, STANDARD_TIME).until(EC.visibility_of_element_located((By.XPATH, (locate)))).send_keys(Keys.DOWN)
        elif sendtype == "esc":
            ##Press escape globally
            webdriver.ActionChains(_WebDriver_).send_keys(Keys.ESCAPE).perform()
        else:
            GlobalVariables._Logger_.debug("Please choose the right method again.")
            ret = -1

    except TimeoutException:
        message = "Cannot find element in %s seconds. Element xpath => %s" % (STANDARD_TIME, locate)
        GlobalVariables._Logger_.exception(message)
        #GetElementTreeAndCompare({"locate":locate})
        ret = 0

    except:
        message = "Encounter unknown exception."
        GlobalVariables._Logger_.exception(message)
        ret = -1

    OK(ret, int(arg['result']), 'SendKeyboardEvent->' + message)

@DecoratorHelper.FuncRecorder
def KeyboardAction(arg):
    '''
    KeyboardAction : Determine kinds of keyboard action using on browser.
        Input argu :
            locate - path
            actiontype - copy / cut / paste / delete / enter
        Return code :
            1 - success
            0 - fail
            -1 - error
    '''
    locate = arg["locate"]
    actiontype = arg["actiontype"]
    ret = 1

    if actiontype == 'copy':
        SendKeyboardEvent({"locate":locate, "sendtype": "select all", "result": "1"})
        SendKeyboardEvent({"locate":locate, "sendtype": "copy", "result": "1"})

    elif actiontype == 'cut':
        SendKeyboardEvent({"locate":locate, "sendtype": "select all", "result": "1"})
        SendKeyboardEvent({"locate":locate, "sendtype": "cut", "result": "1"})

    elif actiontype == 'paste':
        SendKeyboardEvent({"locate":locate, "sendtype": "select all", "result": "1"})
        SendKeyboardEvent({"locate":locate, "sendtype": "paste", "result": "1"})

    elif actiontype == 'delete':
        ##Use Select all + Delete on windows
        SendKeyboardEvent({"locate":locate, "sendtype": "select all", "result": "1"})
        SendKeyboardEvent({"locate":locate, "sendtype": "delete", "result": "1"})

    elif actiontype == 'enter':
        SendKeyboardEvent({"locate":locate, "sendtype": "enter", "result": "1"})

    ##Press keyboard arrow down
    elif actiontype == 'down':
        SendKeyboardEvent({"locate":locate, "sendtype": "down", "result": "1"})

    elif actiontype == 'tab':
        SendKeyboardEvent({"locate":locate, "sendtype": "tab", "result": "1"})

    else:
        GlobalVariables._Logger_.error("Please choose actiontype correctly!")

    OK(ret, int(arg['result']), 'KeyboardAction->' + actiontype)

@DecoratorHelper.FuncRecorder
def BrowserRefresh(arg):
    '''
    BrowserRefresh : Refresh browser
        Input argu : N/A
        Return code :
            1 - success
            0 - fail
            -1 - error
    '''
    ret = 1

    try:
        _WebDriver_.refresh()
    except:
        GlobalVariables._Logger_.exception("Encounter unknown error")

    OK(ret, int(arg['result']), 'BrowserRefresh')

@DecoratorHelper.FuncRecorder
def BrowserPageNavigate(arg):
    '''
    BrowserPageNavigate : Go to previous page/ next page on browser
        Input argu :
            control - back / forward
        Return code :
            1 - success
            -1 - error
    '''
    ret = 1
    control = arg['control']
    message = ""

    try:
        if control == 'back':
            _WebDriver_.back()
            message = "Go to previous page"

        elif control == 'forward':
            _WebDriver_.forward()
            message = "Go to next page"

        else:
            message = "Wrong input arg..."
            GlobalVariables._Logger_.info(message)
            ret = 0
    except:
        GlobalVariables._Logger_.exception("Encounter unknown error")
        ret = -1

    OK(ret, int(arg['result']), 'BrowserPageNavigate->' + message)

@DecoratorHelper.FuncRecorder
def GetBrowserScreenshot(arg):
    '''
    GetBrowserScreenshot : Get screenshot from browser
        Input argu :
            filename - filename of screenshot
        Return code :
            1 - success
            -1 - error
    '''
    ret = 1
    filename = arg['filename']

    try:
        _WebDriver_.save_screenshot(filename)

    ##Handle webdriver exception
    except WebDriverException:
        GlobalVariables._Logger_.exception("Encounter webdriver exception. Maybe wedriver is crashed / closed / connection error. Please check log for more informaion.")
        ret = 0
    except:
        GlobalVariables._Logger_.exception("Encounter unknown error")
        ret = -1

    OK(ret, int(arg['result']), 'GetBrowserScreenshot')

def CheckCurrentUrl(arg):
    '''
    CheckCurrentUrl : Check current url matches the expect url
        Input argu :
            mode - whole / partial
            expect_url -  expect url in current page
        Return code :
            1 - success
            0 - fail
    '''
    ret = 1
    mode = arg["mode"]
    expect_url = arg['expect_url']

    try:
        get_url = _WebDriver_.current_url
        GlobalVariables._Logger_.exception("Actual get url: " + get_url)
        if mode == "whole":
            assert expect_url == get_url
        elif mode == "partial":
            assert expect_url in get_url
    except:
        ret = 0

    OK(ret, int(arg['result']), 'CheckCurrentUrl')

def GetLocateText(arg):
    '''
    GetLocateText : Get text of location from xpath
        Input argu :
            locate - xpath location
        Return code :
            1 - success
            -1 - error
    '''
    ret = 1
    locate = arg['locate']

    try:
        CheckElementExist({"locate": locate, "passok": "1", "result": "1"})
    
    except NoSuchElementException:
        GlobalVariables._Logger_.exception("Cannot find element. Please check page or xpath exists")
        ret = 0

    ##Handle webdriver exception
    except WebDriverException:
        GlobalVariables._Logger_.exception("Encounter webdriver exception. Maybe wedriver is crashed / closed / connection error. Please check log for more informaion.")
        ret = 0
    except:
        GlobalVariables._Logger_.exception("Encounter unknown error")
        ret = -1

    GlobalVariables._Logger_.info("Get text : " + WebDriverWait(_WebDriver_, STANDARD_TIME).until(EC.visibility_of_element_located((By.XPATH, (locate)))).get_attribute("innerHTML"))
    return WebDriverWait(_WebDriver_, STANDARD_TIME).until(EC.visibility_of_element_located((By.XPATH, (locate)))).get_attribute("innerHTML")