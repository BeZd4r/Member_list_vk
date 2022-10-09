from msilib.schema import Error
from PyQt6.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox
from App_files.Main_Window import Ui_MainWindow
from App_files.Checker import Checker
from openpyxl import Workbook
import requests
import sys
import os

app = QApplication(sys.argv)
window = QDialog()
window.setFixedSize(480,360)
ui = Ui_MainWindow()
ui.setupUi(window)
window.show()

params = {
    "token" : open("App_files/token.txt", "r").readline(),
    "group_id" : "",
    "sort" : "id_asc",
    "offset" : 0
}

def Error(msg):
    match msg:
        case "Invalid group id":
            err = QMessageBox.warning(window, msg, "Введен неверный id группы")
        case "Access denied: group hide members":
            err = QMessageBox.warning(window, msg, "Группа закрыла доступ к своим подписчикам")

def Checked_for_error():
    url = f"https://api.vk.com/method/groups.getMembers?access_token={params['token']}&group_id={params['group_id']}&sort={params['sort']}&offset={params['offset']}&count=100&v=5.131"
    response = requests.get(url).json()
    if "error" in response.keys():
        Error(response['error']['error_msg'])
        return False
    else:
        return True

def New_file():
    params["group_id"] = ui.Path.text()

    if not Checked_for_error():
        return

    f_path = os.getcwd() + f"/New_tables/Table_{params['group_id']}.xlsx"
    wb = Workbook()
    wb.save(f_path)

    Checker(params,f_path,True)

def Exist_file():
    params["group_id"] = ui.Path.text()

    if not Checked_for_error():
        return

    f_path = QFileDialog.getOpenFileName(window, 'Open file', filter="*.xlsx")[0]
    Checker(params,f_path,False)

ui.New.clicked.connect(New_file)
ui.Exist.clicked.connect(Exist_file)
sys.exit(app.exec())
