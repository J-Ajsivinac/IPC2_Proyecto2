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
    BTN_INFO = os.path.join(_root, "info.svg").replace("\\", "\\\\")
    BTN_INFO_HOVER = os.path.join(_root, "infoHover.svg").replace("\\", "\\\\")
    BTN_HOME = os.path.join(_root, "home.svg").replace("\\", "\\\\")
    BTN_HOME_HOVER = os.path.join(_root, "homeHover.svg").replace("\\", "\\\\")
    BTN_DRON = os.path.join(_root, "drone.svg").replace("\\", "\\\\")
    BTN_DRON_HOVER = os.path.join(_root, "dronHover.svg").replace("\\", "\\\\")
    BTN_MESSAGE = os.path.join(_root, "message.svg").replace("\\", "\\\\")
    BTN_MESSAGE_HOVER = os.path.join(_root, "messageHover.svg").replace("\\", "\\\\")
