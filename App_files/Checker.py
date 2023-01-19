from App_files.JSON_compile import Create_JSON
import requests
import time

total_count = 0
sleep = 1
class Checker:

    def __init__(self, params,path,new):
       self.params = params
       self.users = {}
       self.Begin()
       print(path)
    #    if self.params["Excel"]:
    #         self.Create_table(wb,new)

       if self.params["JSON"]:
            Create_JSON(self.users,path)

    def User_check(self,ids):

        ids = ','.join(ids)
        u_url = f"https://api.vk.com/method/users.get?access_token={self.params['token']}&fields=photo_max&user_ids={ids}&v=5.131"
        response = requests.get(u_url).json()

        for profile in response['response']:
            self.users[str(profile["id"])] = {
                "Name": profile['first_name']+" "+profile['last_name'],
                "link": "https://vk.com/"+str(profile['id']),
                "Photo" : profile["photo_max"]
                }

    def Check(self):
        global sleep

        url = f"https://api.vk.com/method/groups.getMembers?access_token={self.params['token']}&group_id={self.params['group_id']}&sort={self.params['sort']}&offset={self.params['offset']}&count=100&v=5.131"
        response = requests.get(url).json()
        count = response["response"]["count"]
        ids = []

        for obj in response["response"]["items"]:
            ids.append(str(obj))

        self.User_check(ids)

    def Begin(self):
        global total_count

        url = f"https://api.vk.com/method/groups.getMembers?access_token={self.params['token']}&group_id={self.params['group_id']}&sort={self.params['sort']}&offset={self.params['offset']}&count=100&v=5.131"
        response = requests.get(url).json()

        if "error" in response.keys():
            print(response["error"]["error_msg"])
            return

        total_count = response["response"]["count"]

        while total_count > self.params["offset"]:
            self.Check()
            self.params["offset"] += 100
            time.sleep(0.45)
