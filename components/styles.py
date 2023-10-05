class Styles:
    S_SCROLLBAR_TABLE = """
        QTableWidget {
            background-color: #2a2a36;
            gridline-color: #292a2f;
            border:0px;
            border-radius:10px;
            
        }
        QTableWidget::item {
            color: #ffffff;
            border:0px;
            border-bottom: 2px solid #343442;
        }
        QTableWidget::item:selected {
            background-color: #343442;
        }
        QTableCornerButton::section { background-color: #171821 }
        QScrollBar:vertical {
            border: none;
            background-color:#343442;
            width: 10px;
            border-radius: 0px;
        }
        QScrollBar::handle:vertical {   
            background: #7d91db;
            min-height: 20px;
            border-radius: 4px;
        }
        
        QScrollBar::add-line:vertical {
            border: none;
            background: none;
        }
        QScrollBar::sub-line:vertical {
            border: none;
            background: none;
        }
        
        QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical
            {
                background: none;
            }

        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
            {
                background: none;
            }
    """
    S_COMBOBOX = """
        QComboBox {
            background-color: #252633;
            border: 0px;
            padding: 8px 0px 8px 0px;
            color:white;
            border-radius:5px;
        }
        QComboBox::drop-down {
            width: 20px;
            padding-right:6px;
            border: none;
            color:white;
        }
        
        QComboBox::down-arrow {
            image: url(icons/down.svg);
            height:30;
        }
        
        QComboBox QAbstractItemView {
            border: 0px;
            selection-background-color: #5D5F80;
            color:white;
            background-color:#2F3040;
        }
    """

    WHITE_INFO = "color:white;border:0px;font-weight:600"

    BTN_ALERT = """
        QPushButton {
            background-color: #1a1a1f;
            color: white;
            border: 2px solid #2D2A36;
            border-radius: 5px;
            padding:8px 0 8px 0px;
            font-weight:600;
        }
        QPushButton:hover {
            background-color: #2A2D36;
            color: white;
        }"""

    INPUT_DRON = """
        QLineEdit {
            border: 0px;
            border-radius: 4px;
            color:white;
            padding: 6px 8px;
            background: #252633;
            selection-background-color: #595C7A;
        }
    """

    HEADER_TABLE = """
        QHeaderView::section 
        { 
            background-color: #0E0F14;
            color:#ffffff;
            font-weight:600;
            border:0px;
            border-top-left-radius:10px;
            border-top-right-radius:10px;
        }"""

    BLUE_BTN = """
        QPushButton {
            background-color: #468efc;
            color: white;
            border: 0px;
            border-radius: 5px;
            padding:8px 0 8px 0px;
            font-weight:600;
        }
        QPushButton:hover {
            background-color: #356BBD;
            color: white;
        }"""

    PURPLE_BTN = """
        QPushButton {
            background-color: #c3c4f4;
            color: #2B2B36;
            border: 0px;
            border-radius: 5px;
            padding:8px 0 8px 0px;
            font-weight:600;
        }
        QPushButton:hover {
            background-color: #AFB0DB;
            color: #2B2B36;
        }"""

    TEXT_INSTRUCTIONS = """
        QTextEdit {
            background-color: #2a2a36;
            color: white;
            border: 0px;
            selection-background-color: #595C7A;
        }
        QScrollBar:vertical {
            border: none;
            background-color:#343442;
            width: 10px;
            border-radius: 0px;
        }
        QScrollBar::handle:vertical {   
            background: #7d91db;
            min-height: 20px;
            border-radius: 4px;
        }
        
        QScrollBar::add-line:vertical {
            border: none;
            background: none;
        }
        QScrollBar::sub-line:vertical {
            border: none;
            background: none;
        }
        
        QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical
        {
            background: none;
        }

        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
        {
            background: none;
        }
        """
    PRINC_BTN = """
        QToolButton {
            background-color: #2B2C3B;
            color: #636587;
            border: 0px;
            font-weight:600;
            border-radius: 6px;
        }
        QToolButton:hover {
            background-color: #303242;
            color: #9195C7;
        }
        QToolButton:pressed {
            background-color: #343547;
            color: #ffffff;
        }
        """

    FORM_BTN = """
        QPushButton {
            background-color: #a6f1c8;
            color: #000002;
            border: 0px;
            font-weight:500;
            border-radius: 5px;
            text-align: center;
        }
        QPushButton:hover {
            background-color: #9BE1BB;
            color: #2a3343;
        }
        QPushButton:pressed {
            background-color: #89C7A5;
            color: #202733;
        }
        """

    SIDEBAR_BTN = """
        QPushButton {
            background-color: #13151b;
            color: #696a78;
            border: 0px;
            font-weight:600;
            border-radius: 4px;
            padding:12px 0 12px 15px;
            text-align: left;
        }
        QPushButton:hover {
            background-color: #1B1E26;
            color: #dcdcde;
            font-weight:600;
        }
        """

    SIDEBAR_BTN_ACTIVE = """
        QPushButton {
            background-color: #242833;
            color: #b1b8fa;
            border: 0px;
            border-radius: 4px;
            padding:12px 0 12px 15px;
            text-align: left;
            font-weight:600;
        }"""
