import os


class Icons:
    _root = os.path.dirname(os.path.abspath(__file__))
    BTN_RESET = os.path.join(_root, "reset.svg").replace("\\", "\\\\")
    BTN_UPL = os.path.join(_root, "upload.svg").replace("\\", "\\\\")
    BTN_XML = os.path.join(_root, "xml.svg").replace("\\", "\\\\")
    BTN_PROCESS = os.path.join(_root, "process.svg").replace("\\", "\\\\")
    ICON_ERROR = os.path.join(_root, "error.svg").replace("\\", "\\\\")
    ICON_ALERT = os.path.join(_root, "alert.svg").replace("\\", "\\\\")
    ICON_CHECK = os.path.join(_root, "check.svg").replace("\\", "\\\\")
    ICON_INFO = os.path.join(_root, "infor.svg").replace("\\", "\\\\")
