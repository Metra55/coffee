import sqlite3
from PyQt5.QtWidgets import (
    QMainWindow, QTableWidgetItem, QPushButton, QDialog
)

from window_ui import Ui_MainWindow



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self._init_ui()

    def _init_ui(self):
        self.con = sqlite3.connect("coffee.sqlite")
        self.otrisovka()

    def otrisovka(self):
        self.cur = self.con.cursor()

        result = self.cur.execute(f"""
                        SELECT title,stepen_objarki, molotiy_v_zernah,vkusno,price,obiyom_upakovki FROM coffes                            """).fetchall()

        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))

        self.tableWidget.setHorizontalHeaderLabels(['Название', 'степень обжарки', 'молотый/в зернах', 'описание вкуса', 'цена', ' объем упаковки'])

        for i, elem in enumerate(result):
            for j, value in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))
