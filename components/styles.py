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
            padding: 6px 0px 6px 0px;
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

    WHITE_INFO = "color:white;border:0px;font-weight:500"

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
