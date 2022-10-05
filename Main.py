from openpyxl import load_workbook
import requests
import time

names, page_ids, page_url = [], [], []
total_count = 0
sleep = 1
params = {
    "token" : open("token.txt", "r").readline(),
    "group_id" : "diarywebvdv",
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

url = f"https://api.vk.com/method/groups.getMembers?access_token={params['token']}&group_id={params['group_id']}&sort={params['sort']}&offset={params['offset']}&count=100&v=5.131"
response = requests.get(url).json()
total_count = response["response"]["count"]

while total_count > params["offset"]:
    Check()
    params["offset"] += 100
    time.sleep(0.5)

exel_file = "Table.xlsx"
work_book = load_workbook(exel_file)

if "Data" in work_book:
    work_book.remove(work_book["Data"])

work_list = work_book.create_sheet("Data")
work_list.column_dimensions['A'].width = 10
work_list.column_dimensions['B'].width = 24
work_list.column_dimensions['C'].width = 10
work_list.column_dimensions['D'].width = 30
for i in range(1,len(names)+1):
    work_list[f"A{i}"] = i
    work_list[f"B{i}"] = names[i-1]
    work_list[f"C{i}"] = page_ids[i-1]
    work_list[f"D{i}"] = page_url[i-1]

work_book.save(exel_file)
work_book.close()
