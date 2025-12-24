'''

SOW PACKAGE MANAGER
VIEW LICENSE WITH SOW LICENSE
PROPERTY OF AUTHORS

'''

import requests

def link(link):
    resp = requests.get(link)
    if resp.status_code != 200:
        print("Could not obtain via scraping.\nStatus Code:", resp.status_code)
        raise ConnectionError
    else:
        if not link in ["https://raw.githubusercontent.com/SoftPankek7/SowPackageManager/refs/heads/main/LICENSE"]:
            system.Output.info("Got data from "+str(link))
    return resp.text.replace('\r\n', '\n').replace('\r', '\n')

class PackageManaging:
    def download(name):
        try:
            print("Downloading raw content of "+name)
            item = link("https://raw.githubusercontent.com/SoftPankek7/SowPackageManager/refs/heads/main/"+str(name)+".py")
            print("Got Content.")
            print("Installing "+str(name))
            with open(name, "wt") as file:
                file.write(item) # file.write
            print("Downloaded "+str(name))
            print("Done! Downloaded to path.")
            return True
        except ConnectionError:
            return False
    def install(name):
        try:
            print("Downloading raw content of "+name+".py")
            item = link("https://raw.githubusercontent.com/SoftPankek7/SowPackageManager/refs/heads/main/"+str(name)+".py")
            print("Got Content.")
            print("Trying to clear "+name+".py")
            with open(name+".py", 'w') as file:pass
            print("Installing "+str(name))
            with open(name+".py", "wt") as file:
                file.write(item)
            print("Installed "+name+".py")
            print(f"Linking {str(name)} to libs.el")
            with open("libs.el", "at") as file:
                file.write("\n"+str(name))
            print("Finished Linking.")
            print("Done! Restart env to see effects.")
            return True
        except ConnectionError:
            return False
        
    def update():
        try:
            while True:
                prompt = input("This is going to reinstall the sow library - possibly corrupting it.\nAre you sure? (Y/N)  ")
                if prompt.lower() == "y":
                    print("Downloading raw content of sow")
                    item = link("https://raw.githubusercontent.com/SoftPankek7/SowPackageManager/refs/heads/main/sow.py")
                    print("Got Content.")
                    print("Installing sow")
                    with open("sow.py", "wt") as file:
                        file.write(item)
                    print("Downloaded sow")
                    print("Done!")
                    print("Closing Env...")
                    system.Output.halt("Sow has been installed and required a restart.")
                    return True
                elif prompt.lower() == "n":
                    break
                else:
                    print("That is an incorrect option.")
        except ConnectionError:
            return False

    def get_license():
        try:
            item = link("https://raw.githubusercontent.com/SoftPankek7/SowPackageManager/refs/heads/main/LICENSE")
            print(item)
        except ConnectionError:
            pass

    def clear_libs():
        while True:
            prompt = input("This is going to unlink ALL non-system libaries.\nAre you sure? (Y/N)  ")
            if prompt.lower() == "y":
                with open("libs.el", "wt") as file:
                    file.write("""; comments delimited by semicolons.
; do not use dashes, they are for 
; system use however, they can be 
; used in comments
; (CLEANED BY SOW)

system
clear
contents
examplelib
info
help
edit

tedit
sow
ex

-- IMPORTED --


""")
                    break
            elif prompt.lower() == "n":
                break
            else:
                print("That is an incorrect option.")

class Environment:

    LibInfo = {
        "name": "sow",
        "credits": ["Charlie T"],
        "version": 1.6,
        "reqVersion": 1.6,
        "description": "The deafult package manager.",
        "helpinfo": "sow install [A]\nsow download [A]\nsow license\nsow clear\nsow update\nsow version"
    }

    import libload as lib
    global libs, system
    libs = lib.load_libs()
    system = libs["system"]

    def RunFromEnv(func):
        if len(func) == 0:
            # User has not provided any func.
            import libload as lib
            lib.load_libs()["help"].Environment.RunFromEnv(["sow"])
        else:
            if func[0].lower() == "install":
                if not len(func) == 1:
                    PackageManaging.install(func[1].lower())
                else:
                    print("Please specify more than 1 argument for install.")
            elif func[0].lower() == "download":
                if not len(func) == 1:
                    print(func[1].lower())
                    PackageManaging.download(func[1].lower())
                else:
                    print("Please specify more than 1 argument for download.")
            elif func[0].lower() == "license":
                PackageManaging.get_license()
            elif func[0].lower() == "clear":
                PackageManaging.clear_libs()
            elif func[0].lower() == "update":
                PackageManaging.update()
            elif func[0].lower() == "version":
                print(f"Sow v{Environment.LibInfo["version"]}")
            else:
                print("Please specify a correct argument.")
if __name__ == "__main__":
    print("Please do not run without the environment.")