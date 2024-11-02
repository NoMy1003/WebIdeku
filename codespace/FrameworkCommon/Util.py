##System import


##Framework import
import codespace.FrameworkCommon.GlobalVariables as GlobalVariables

def GetXpath(key, mode):
    '''
        GetXpath: Get xpath value from json
            Input:
                key: key name of xpath value from json
                mode: func / test (get xpath from func or test)
            Return code: N/A
    '''
    ##Return xpath value from xpath.json
    try:
        if mode == "func":
            GlobalVariables._Logger_.info("Get xpath from function.")
            GlobalVariables._Logger_.info(str(GlobalVariables._CurrentFuncFilename_))
            GlobalVariables._Logger_.info(str(GlobalVariables._CurrentFuncQualName_))
            return GlobalVariables._XpathJsonData_[GlobalVariables._CurrentFuncFilename_][GlobalVariables._CurrentFuncQualName_][key]
        elif mode == "test":
            GlobalVariables._Logger_.info("Get xpath from test.")
            GlobalVariables._Logger_.info(str(GlobalVariables._CurrentTestFilename_))
            GlobalVariables._Logger_.info(str(GlobalVariables._CurrentTestQualName_))
            return GlobalVariables._XpathJsonData_[GlobalVariables._CurrentTestFilename_][GlobalVariables._CurrentTestQualName_][key]
    except KeyError:
        GlobalVariables._Logger_.exception("Please check your xpath setting exist in region json file !!!!")
        GlobalVariables._Logger_.info("Please check your xpath exist in region json file, missing key:" + key)

    except IOError:
        GlobalVariables._Logger_.exception("Please check your json file for xpath !!!!")
        GlobalVariables._Logger_.info("Please check your json file for xpath !!!!")

    except:
        GlobalVariables._Logger_.exception("Encounter framework exception !!!!")
        GlobalVariables._Logger_.info("Encounter framework exception !!!!")