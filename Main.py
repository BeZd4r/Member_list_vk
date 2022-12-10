from PyQt6.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox, QPushButton
from App_files.Main_Window import Ui_MainWindow
from App_files.Checker import Checker
from threading import Thread
from openpyxl import Workbook
import requests
import time
import sys
import os

app = QApplication(sys.argv)
window = QDialog()
window.setFixedSize(480,360)
ui = Ui_MainWindow()
ui.setupUi(window)
window.show()

calculate = None
colors = {False : "#ff0000", True : "#19ff19"}
params = {
    "token" : open("App_files/token.txt", "r").readline(),
    "group_id" : "",
    "sort" : "id_asc",
    "offset" : 0,
    "Excel" : True,
    "JSON"  : False
}

def Error(msg):
    match msg:
        case "Invalid group id":
            err = QMessageBox.warning(window, msg, "Введен неверный id группы")
        case "Access denied: group hide members":
            err = QMessageBox.warning(window, msg, "Группа закрыла доступ к своим подписчикам")
        case "User authorization failed: no access_token passed.":
            err = QMessageBox.warning(window, msg, "Вы не записали свой access token Vk в файл token.txt")


def Checked_for_error():
    url = f"https://api.vk.com/method/groups.getMembers?access_token={params['token']}&group_id={params['group_id']}&sort={params['sort']}&offset={params['offset']}&count=100&v=5.131"
    response = requests.get(url).json()
    if "error" in response.keys():
        Error(response['error']['error_msg'])
        print(response['error']['error_msg'])
        return False
    else:
        return True

def Check_proccess():
    if calculate != None:
        if calculate.is_alive():
            def Stop():
                calculate.join()
            stop = QPushButton("Остановить")
            stop.clicked.connect(Stop)
            not_yet = QMessageBox.warning(window, "Мы еще не закончили!", "Еще выполняется парсинг прошлого запроса :)")
            return

def Begin_to_main(f_path,new):
    Checker(params,f_path,new)

def New_file():
    global calculate

    params["group_id"] = ui.Path.text()
    params["token"] = open("App_files/token.txt", "r").readline()

    if not Checked_for_error():
        return

    f_path = os.getcwd() + f"/New_tables/Table_{params['group_id']}.xlsx"
    wb = Workbook()
    wb.save(f_path)

    calculate = Thread(target=Begin_to_main ,args=(f_path, True))
    calculate.start()
    # i = 0
    # while calculate.is_alive():
    #     print(i)
    #     i+=1
    #     time.sleep(1)

def Exist_file():
    global calculate

    params["group_id"] = ui.Path.text()
    params["token"] = open("App_files/token.txt", "r").readline()

    if not Checked_for_error():
        return

    f_path = QFileDialog.getOpenFileName(window, 'Open file', filter="*.xlsx")[0]

    calculate = Thread(target=Begin_to_main ,args=(f_path, False))
    calculate.start()

def Create_Excel():
    params["Excel"] = not params["Excel"]
    ui.Excel.setStyleSheet(f"background-color: {colors[params['Excel']]}")

def Create_JSON():
    params["JSON"] = not params["JSON"]
    ui.JSON.setStyleSheet(f"background-color: {colors[params['JSON']]}")

ui.New.clicked.connect(New_file)
ui.Exist.clicked.connect(Exist_file)
ui.Excel.clicked.connect(Create_Excel)
ui.JSON.clicked.connect(Create_JSON)
sys.exit(app.exec())
