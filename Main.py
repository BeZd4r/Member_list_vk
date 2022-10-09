import datetime
from PyQt6.QtWidgets import QApplication, QDialog, QFileDialog
from App_files.Main_Window import Ui_MainWindow
from App_files.Checker import Begin_Check
from openpyxl import load_workbook
import requests
import time
import sys

app = QApplication(sys.argv)
window = QDialog()
window.setFixedSize(480,360)
ui = Ui_MainWindow("Bebra")
ui.setupUi(window)
window.show()


names, page_ids, page_url = [], [], []
total_count = 0
sleep = 1
params = {
    "token" : open("App_files/token.txt", "r").readline(),
    "group_id" : "",
    "sort" : "id_asc",
    "offset" : 0
}

def User_check(ids):
    users = ','.join(ids)
    u_url = f"https://api.vk.com/method/users.get?access_token={params['token']}&user_ids={users}&v=5.131"
    response = requests.get(u_url).json()

    for prof in response['response']:
        names.append(prof['first_name']+" "+prof['last_name'])
        page_ids.append(prof['id'])
        page_url.append("https://vk.com/"+str(prof['id']))

def Check():
    global sleep

    url = f"https://api.vk.com/method/groups.getMembers?access_token={params['token']}&group_id={params['group_id']}&sort={params['sort']}&offset={params['offset']}&count=100&v=5.131"
    response = requests.get(url).json()
    count = response["response"]["count"]
    ids = []

    for obj in response["response"]["items"]:
        ids.append(str(obj))

    User_check(ids)

def Begin():
    global total_count

    url = f"https://api.vk.com/method/groups.getMembers?access_token={params['token']}&group_id={params['group_id']}&sort={params['sort']}&offset={params['offset']}&count=100&v=5.131"
    response = requests.get(url).json()

    if "error" in response.keys():
        print(response["error"]["error_msg"])
        return

    total_count = response["response"]["count"]

    while total_count > params["offset"]:
        Check()
        params["offset"] += 100
        time.sleep(0.5)

def Create_table(url,new):
    wb = load_workbook(url)

    if new == True:
        ws = wb.create_sheet("Members_Data")
    elif new == False:
        ws = wb[wb.sheetnames[-1]]

    ws.column_dimensions['A'].width = 24
    ws.column_dimensions['B'].width = 15
    ws.column_dimensions['C'].width = 30
    for i in range(1,len(names)+1):
        ws[f"A{i}"] = names[i-1]
        ws[f"B{i}"] = page_ids[i-1]
        ws[f"C{i}"] = page_url[i-1]

    wb.save(url)
    wb.close()

def New_file():
    params["group_id"] = ui.Path.text()

    Begin()

    f_path = f"New_tables/Table_{params['group_id']}.xlsx"
    f = open(f_path,"a")
    f.close()

    Create_table(f_path,True)

def Exist_file():
    params["group_id"] = ui.Path.text()

    Begin()

    f_path = QFileDialog.getOpenFileName(window, 'Open file')[0]

    Create_table(f_path, False)

ui.New.clicked.connect(New_file)
ui.Exist.clicked.connect(Exist_file)
sys.exit(app.exec())
