import requests
import json
from win10toast import ToastNotifier
import time


endpoint = "https://presence.roblox.com/v1/presence/users"
userid = input("Target userid: ")
body = {
    "userIds": [userid]
}

printlogs = False
plinput = input("Do you want to print logs? (Y/n)")
plinput.lower()
if plinput == "y":
    printlogs=True

print(f"{plinput}  {printlogs}")

toaster = ToastNotifier()

#vars
isOnline = False
isOnGame = False
isOnStudio = False
#Offline = 0, Online = 1, Game = 2, Studio = 3, Invis = 4
while True:
    r = requests.post(endpoint, json=body)
    data = r.json()

    if printlogs: print(json.dumps(data, indent=4))

    if data['userPresences'][0]['userPresenceType'] == 0:
        print("User is offline")
        if isOnline == True:
            toaster.show_toast(title="User offline", msg="The user is offline", duration=4)
        isOnGame = False
        isOnStudio = False
        isOnline = False

    elif data['userPresences'][0]['userPresenceType'] == 1:
        print("User is online!")
        if isOnline == False:
            toaster.show_toast(title="User online", msg="The user is online!", duration=7)
        isOnline = True
        isOnGame = False

    elif data['userPresences'][0]['userPresenceType'] == 2:
        print("User is playing a game!")
        if isOnGame == False:
            toaster.show_toast(title="User playing game!", msg="The user is inside a game!", duration=6)
        isOnGame = True
        isOnline = False

    elif data['userPresences'][0]['userPresenceType'] == 3:
        print("User is on studio!")
        if isOnStudio == False:
            toaster.show_toast(title="User on studio", msg="The user is inside roblox studio!", duration=15)
        isOnline = False
        isOnGame  = False
        isOnStudio = True

    elif data['userPresences'][0]['userPresenceType'] == 4:
        print("User is invisible???")
        if isOnline == False:
            toaster.show_toast(title="User invisible..", msg="The user is invisible!", duration=10)
        isOnline = True
        isOnGame = False
        isOnStudio = False

    time.sleep(1.6715)