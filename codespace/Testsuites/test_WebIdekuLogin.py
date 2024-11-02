##Import framework module
import pytest
import codespace.FrameworkCommon.FrameworkBase as FrameworkBase
import codespace.FrameworkCommon.CommonMethod as CommonMethod
import codespace.FrameworkCommon.DecoratorHelper as DecoratorHelper
from codespace.FrameworkCommon.FrameworkBase import *
import allure

##Import platform module
from codespace.FrameworkCommon.Util import GetXpath
import codespace.Web.Common.BaseUICore as BaseUICore

##Import feature module
from codespace.Web.Feature.WebIdekuLoginMethod import *


CaseName = "WebIdekuLogin"

##Function level setup / teardown
@pytest.fixture()
def PrepareTest():
    print("\n[----Running case setup----]\n")
    BaseUICore.InitialWebDriver({"result": "1"})
    print("\n[----Running case setup ended----]\n")

    yield

    print("\n[----Running case teardown----]\n")
    BaseUICore.DeinitialWebDriver()
    print("\n[----Running case teardown ended----]\n")

##Class level setup / teardown
@pytest.fixture(scope="class")
def PrepareTestClass():

    yield


@allure.title(CaseName)
@pytest.mark.usefixtures("PrepareTestClass")
class TestWebIdekuLogin:

    @DecoratorHelper.TestRecorderMod
    def test_WebIdekuLogin0001(self, PrepareTest):
        '''
            test_WebIdekuLogin0001 - 檢查登入頁面基本UI顯示
        '''
        ##Go to login page
        WebIdekuLogin.GoToLoginPage({"result": "1"})
        BaseUICore.PageHasLoaded({"result": "1"})
        CommonMethod.SleepTime({"times": "3", "result": "1"})

        ##Check company brand
        BaseUICore.CheckElementExist({"locate": GetXpath("company_brand", mode="test"), "passok": "1", "result": "1"})

        ##Check company logo
        BaseUICore.CheckElementExist({"locate": GetXpath("company_logo", mode="test"), "passok": "1", "result": "1"})

        ##Check login page title
        BaseUICore.CheckElementExist({"locate": GetXpath("login_page_title", mode="test"), "passok": "1", "result": "1"})

        ##Check username input
        BaseUICore.CheckElementExist({"locate": GetXpath("username_input", mode="test"), "passok": "1", "result": "1"})

        ##Check password input
        BaseUICore.CheckElementExist({"locate": GetXpath("password_input", mode="test"), "passok": "1", "result": "1"})

        ##Check login button
        BaseUICore.CheckElementExist({"locate": GetXpath("login_button", mode="test"), "passok": "1", "result": "1"})

        ##Check forget password button
        BaseUICore.CheckElementExist({"locate": GetXpath("forget_password_button", mode="test"), "passok": "1", "result": "1"})

    @DecoratorHelper.TestRecorderMod
    def test_WebIdekuLogin0002(self, PrepareTest):
        '''
            test_WebIdekuLogin0002 - 檢查正常登入行為
        '''

        ##Go to login page
        WebIdekuLogin.GoToLoginPage({"result": "1"})
        BaseUICore.PageHasLoaded({"result": "1"})
        CommonMethod.SleepTime({"times": "3", "result": "1"})

        ##Input username : Admin
        WebIdekuLogin.InputUsername({"username": "Admin", "result": "1"})

        ##Input password : admin123
        WebIdekuLogin.InputPassword({"password": "admin123", "result": "1"})
        CommonMethod.SleepTime({"times": "3", "result": "1"})

        ##Click login button
        WebIdekuLogin.ClickLogin({"result": "1"})
        BaseUICore.PageHasLoaded({"result": "1"})

        ##Check page url : enter dashboard page
        BaseUICore.CheckCurrentUrl({"mode": "partial", "expect_url": "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index", "result": "1"})

        ##Check username title
        BaseUICore.CheckElementExist({"locate": GetXpath("username_title", mode="test"), "passok": "1", "result": "1"})

    @DecoratorHelper.TestRecorderMod
    def test_WebIdekuLogin0003(self, PrepareTest):
        '''
            test_WebIdekuLogin0003 - 檢查帳號錯誤行為
        '''

        ##Go to login page
        WebIdekuLogin.GoToLoginPage({"result": "1"})
        BaseUICore.PageHasLoaded({"result": "1"})
        CommonMethod.SleepTime({"times": "3", "result": "1"})

        ##Input username : Admin1
        WebIdekuLogin.InputUsername({"username": "Admin1", "result": "1"})

        ##Input password : admin123
        WebIdekuLogin.InputPassword({"password": "admin123", "result": "1"})
        CommonMethod.SleepTime({"times": "3", "result": "1"})

        ##Click login button
        WebIdekuLogin.ClickLogin({"result": "1"})
        BaseUICore.PageHasLoaded({"result": "1"})

        ##Check page url : still in login page
        BaseUICore.CheckCurrentUrl({"mode": "partial", "expect_url": "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", "result": "1"})

        ##Check error content
        BaseUICore.CheckElementExist({"locate": GetXpath("invalid_credentials_error", mode="test"), "passok": "1", "result": "1"})

    @DecoratorHelper.TestRecorderMod
    def test_WebIdekuLogin0004(self, PrepareTest):
        '''
            test_WebIdekuLogin0004 - 檢查密碼錯誤行為
        '''

        ##Go to login page
        WebIdekuLogin.GoToLoginPage({"result": "1"})
        BaseUICore.PageHasLoaded({"result": "1"})
        CommonMethod.SleepTime({"times": "3", "result": "1"})

        ##Input username : Admin
        WebIdekuLogin.InputUsername({"username": "Admin", "result": "1"})

        ##Input password : admin1234
        WebIdekuLogin.InputPassword({"password": "admin1234", "result": "1"})
        CommonMethod.SleepTime({"times": "3", "result": "1"})

        ##Click login button
        WebIdekuLogin.ClickLogin({"result": "1"})
        BaseUICore.PageHasLoaded({"result": "1"})

        ##Check page url : still in login page
        BaseUICore.CheckCurrentUrl({"mode": "partial", "expect_url": "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", "result": "1"})

        ##Check error content
        BaseUICore.CheckElementExist({"locate": GetXpath("invalid_credentials_error", mode="test"), "passok": "1", "result": "1"})

    @DecoratorHelper.TestRecorderMod
    def test_WebIdekuLogin0005(self, PrepareTest):
        '''
            test_WebIdekuLogin0005 - 檢查帳號空白行為
        '''

        ##Go to login page
        WebIdekuLogin.GoToLoginPage({"result": "1"})
        BaseUICore.PageHasLoaded({"result": "1"})
        CommonMethod.SleepTime({"times": "3", "result": "1"})

        ##Input account : [blank]
        WebIdekuLogin.InputUsername({"username": "", "result": "1"})

        ##Input password : admin123
        WebIdekuLogin.InputPassword({"password": "admin123", "result": "1"})
        CommonMethod.SleepTime({"times": "3", "result": "1"})

        ##Click login button
        WebIdekuLogin.ClickLogin({"result": "1"})
        BaseUICore.PageHasLoaded({"result": "1"})

        ##Check page url : still in login page
        BaseUICore.CheckCurrentUrl({"mode": "partial", "expect_url": "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", "result": "1"})

        ##Check account "required" error content
        BaseUICore.CheckElementExist({"locate": GetXpath("account_required_error", mode="test"), "passok": "1", "result": "1"})

    @DecoratorHelper.TestRecorderMod
    def test_WebIdekuLogin0006(self, PrepareTest):
        '''
            test_WebIdekuLogin0006 - 檢查密碼空白行為
        '''

        ##Go to login page
        WebIdekuLogin.GoToLoginPage({"result": "1"})
        BaseUICore.PageHasLoaded({"result": "1"})
        CommonMethod.SleepTime({"times": "3", "result": "1"})

        ##Input account : Admin
        WebIdekuLogin.InputUsername({"username": "Admin", "result": "1"})

        ##Input password : [blank]
        WebIdekuLogin.InputPassword({"password": "", "result": "1"})
        CommonMethod.SleepTime({"times": "3", "result": "1"})

        ##Click login button
        WebIdekuLogin.ClickLogin({"result": "1"})
        BaseUICore.PageHasLoaded({"result": "1"})

        ##Check page url : still in login page
        BaseUICore.CheckCurrentUrl({"mode": "partial", "expect_url": "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", "result": "1"})

        ##Check password "required" error content
        BaseUICore.CheckElementExist({"locate": GetXpath("password_required_error", mode="test"), "passok": "1", "result": "1"})

    @DecoratorHelper.TestRecorderMod
    def test_WebIdekuLogin0007(self, PrepareTest):
        '''
            test_WebIdekuLogin0007 - 檢查"忘記密碼"流程
        '''

        ##Go to login page
        WebIdekuLogin.GoToLoginPage({"result": "1"})
        BaseUICore.PageHasLoaded({"result": "1"})
        CommonMethod.SleepTime({"times": "3", "result": "1"})

        ##Click forget password button
        WebIdekuLogin.ClickForgetPassword({"result": "1"})
        BaseUICore.PageHasLoaded({"result": "1"})

        ##Click cancel
        WebIdekuLoginResetPassword.ClickCancel({"result": "1"})
        CommonMethod.SleepTime({"times": "5", "result": "1"})

        ##Check page url : return to login page
        BaseUICore.CheckCurrentUrl({"mode": "partial", "expect_url": "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", "result": "1"})
        BaseUICore.PageHasLoaded({"result": "1"})

        ##Click forget password button
        WebIdekuLogin.ClickForgetPassword({"result": "1"})
        BaseUICore.PageHasLoaded({"result": "1"})

        ##Input username
        WebIdekuLoginResetPassword.InputUsername({"username": "Admin", "result": "1"})

        ##Click reset password
        WebIdekuLoginResetPassword.ClickResetPassword({"result": "1"})
        BaseUICore.PageHasLoaded({"result": "1"})

        ##Check reset password email sent successfully title / content / note title / note content
        BaseUICore.CheckElementExist({"locate": GetXpath("success_title", mode="test"), "passok": "1", "result": "1"})
        BaseUICore.CheckElementExist({"locate": GetXpath("success_content_01", mode="test"), "passok": "1", "result": "1"})
        BaseUICore.CheckElementExist({"locate": GetXpath("success_content_02", mode="test"), "passok": "1", "result": "1"})
        BaseUICore.CheckElementExist({"locate": GetXpath("success_note_title", mode="test"), "passok": "1", "result": "1"})
        BaseUICore.CheckElementExist({"locate": GetXpath("success_note_content", mode="test"), "passok": "1", "result": "1"})
