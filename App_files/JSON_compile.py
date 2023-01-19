import json

class Create_JSON:

    def __init__(self,users, url):
        self.base = {}
        self.users = users
        self.url = url
        self.Create()

    def Create(self):
        self.base["users"] = self.users
        print(self.users)

        with open(f"{self.url}.json", "w", encoding="utf-8") as wf:
            wf.write(json.dumps(self.base, indent = 4, ensure_ascii=False))
