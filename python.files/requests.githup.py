import requests



class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'


    def get_user(self, username):
        response = requests.get(self.api_url+'/users/'+username)
        return response.json()



    def getRepositeries(self, username):
       response = requests.get(self.api_url+'/users/'+username+'/repos')
       return response.json()

github = Github()



while True:
    secim = input("1 - Find User\n2 - Get Repositories\n3 - Create Repositeries\n4 - Exit\nSecim : ")

    if secim == '4':
        break

    else:
        if secim == '1':
            username = input("Username : ")
            result = github.get_user(username)
            print(f"name : {result['name']} public repos : {result['public_repos']} followera : {result['followers']} ")

        elif secim == '2':
            username = input("username : ")
            result = github.getRepositeries(username)
            for repo in result:
                print(repo["name"])

        elif secim == '3':
            pass

        else:
            print("Yanlıs Secim!!!") 


















