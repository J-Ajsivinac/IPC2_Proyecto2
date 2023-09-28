import os


class Icons:
    _root = os.path.dirname(os.path.abspath(__file__))
    BTN_RESET = os.path.join(_root, "reset.svg").replace("\\", "\\\\")
    BTN_UPL = os.path.join(_root, "upload.svg").replace("\\", "\\\\")
    BTN_XML = os.path.join(_root, "xml.svg").replace("\\", "\\\\")
