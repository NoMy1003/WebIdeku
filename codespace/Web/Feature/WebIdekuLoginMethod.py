import codespace.FrameworkCommon.FrameworkBase as FrameworkBase
import codespace.FrameworkCommon.DecoratorHelper as DecoratorHelper
import codespace.FrameworkCommon.CommonMethod as CommonMethod
from codespace.FrameworkCommon.Util import GetXpath
import codespace.Web.Common.BaseUICore as BaseUICore

##Initial OK function
def OK(actual_result, expect_result, message):
    return FrameworkBase.OK(actual_result, expect_result, message)

class WebIdekuLogin:

    @DecoratorHelper.FuncRecorderMod
    def GoToLoginPage(arg):
        '''
            GoToLoginPage: Go to login page
                Input arg:
                    N/A
        '''
        ret = 1
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

        ##Go to Ideku login page
        BaseUICore.RedirectToUrl({"url": url, "result": "1"})
        BaseUICore.PageHasLoaded({"result": "1"})

        OK(ret, int(arg["result"]), "WebIdekuLogin.GoToLoginPage")

    @DecoratorHelper.FuncRecorderMod
    def InputUsername(arg):
        '''
            InputUsername: Input account
                Input arg:
                    username - username input
        '''
        ret = 1
        username = arg["username"]

        ##Input username
        xpath = GetXpath("username_input", mode="func")
        BaseUICore.Input({"locate": xpath, "value": username, "result": "1"})

        OK(ret, int(arg["result"]), "WebIdekuLogin.InputUsername")

    @DecoratorHelper.FuncRecorderMod
    def InputPassword(arg):
        '''
            InputPassword: Input password
                Input arg:
                    password - password input
        '''
        ret = 1
        password = arg["password"]

        ##Input password
        xpath = GetXpath("password_input", mode="func")
        BaseUICore.Input({"locate": xpath, "value": password, "result": "1"})

        OK(ret, int(arg["result"]), "WebIdekuLogin.InputPassword")
    
    @DecoratorHelper.FuncRecorderMod
    def ClickLogin(arg):
        '''
            ClickLogin: Click login button
                Input arg:
                    N/A
        '''
        ret = 1

        ##Click login button
        xpath = GetXpath("login_button", mode="func")
        BaseUICore.Click({"mode": "xpath", "locate": xpath, "message": "Click login button", "result": "1"})

        OK(ret, int(arg["result"]), "WebIdekuLogin.ClickLogin")
    
    @DecoratorHelper.FuncRecorderMod
    def ClickForgetPassword(arg):
        '''
            ClickLogin: Click login button
                Input arg:
                    N/A
        '''
        ret = 1

        ##Click "Forgot your password?"
        xpath = GetXpath("forget_password_button", mode="func")
        BaseUICore.Click({"mode": "xpath", "locate": xpath, "message": "Click forget password", "result": "1"})

        OK(ret, int(arg["result"]), "WebIdekuLogin.ClickForgetPassword")

class WebIdekuLoginResetPassword:

    @DecoratorHelper.FuncRecorderMod
    def ClickCancel(arg):
        '''
            ClickCancel: Click cancel button
                Input arg:
                    N/A
        '''
        ret = 1

        ##Click cancel button
        xpath = GetXpath("cancel_button", mode="func")
        BaseUICore.Click({"mode": "xpath", "locate": xpath, "message": "Click cancel button", "result": "1"})

        OK(ret, int(arg["result"]), "WebIdekuLoginResetPassword.ClickCancel")
    
    @DecoratorHelper.FuncRecorderMod
    def InputUsername(arg):
        '''
            InputUsername: Input account
                Input arg:
                    username - username input
        '''
        ret = 1
        username = arg["username"]

        ##Input username
        xpath = GetXpath("username_input", mode="func")
        BaseUICore.Input({"locate": xpath, "value": username, "result": "1"})

        OK(ret, int(arg["result"]), "WebIdekuLoginResetPassword.InputUsername")
    
    @DecoratorHelper.FuncRecorderMod
    def ClickResetPassword(arg):
        '''
            ClickResetPassword: Click reset password button
                Input arg:
                    N/A
        '''
        ret = 1

        ##Click reset password button
        xpath = GetXpath("reset_button", mode="func")
        BaseUICore.Click({"mode": "xpath", "locate": xpath, "message": "Click reset password button", "result": "1"})

        OK(ret, int(arg["result"]), "WebIdekuLoginResetPassword.ClickResetPassword")