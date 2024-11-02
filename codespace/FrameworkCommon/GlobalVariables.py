##System import
import os

##Framework import
from codespace.FrameworkCommon.Logger import InitialDebugLog

##Global variables
_Logger_ = InitialDebugLog()
_XpathJsonData_ = {}
_FuncJsonData_ = {}
_CurrentFuncFilename_ = ""
_CurrentFuncQualName_ = ""
_CurrentTestFilename_ = ""
_CurrentTestQualName_ = ""

##Log variables
_CurrentLogTime_ = ""

##Framework related
class Framework:
    _CurDataDIR_ = os.getcwd()
    _CaseList_ = []
    _CaseStartTime_ = None
    _IsSingleCaseFail_ = 0
    _CaseIDExpectedResult_ = {}
    _CaseIDActualResult_ = {}