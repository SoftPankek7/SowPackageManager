''' A simple file-reading util for the Environment. (Built-in) '''

class Environment:
    LibInfo = {
        "name": "Info",
        "credits": [],
        "version": 1.3,
        "description": "Get Information from libaries! (Built-in)",
        "helpinfo": "info [LIBRARY] [-r, -n, -c, -v, -d, -h]\n-r  = LIBRARY's Raw Info Data\n-n  = LIBRARY's Name\n-c  = LIBRARY's Credits\n-v  = LIBRARY's Version\n-d  = LIBRARY's Description\n-h  = LIBRARY's Help info (same as the command help)"
    }
    import libload as lib
    global libs, system
    libs = lib.load_libs()
    system = libs["system"]
    def RunFromEnv(function):
        try:
            if len(function) == 1:
                print("Raw:"+ str(libs[function[0]].Environment.LibInfo))
                info = libs[function[0]].Environment.LibInfo
                print("Name:     "+str(info["name"]))
                print("Credits:     "+str(info["credits"]))
                print("Version:  "+str(info["version"]))
                print("Desc:\n"+str(info["description"]))
                print("Help:\n"+str(info["helpinfo"]))
            if len(function) >= 2:
                for i in function:
                    if i == function[0]:
                        continue
                    else:
                        info = libs[function[0]].Environment.LibInfo
                        if i == "-r":
                            print("Raw:"+ str(libs[function[0]].Environment.LibInfo))
                        elif i == "-n":
                            print("Name:     "+str(info["name"]))
                        elif i == "-c":
                            print("Credits:     "+str(info["credits"]))
                        elif i == "-v":
                            print("Version:  "+str(info["version"]))
                        elif i == "-d":
                            print("Desc:\n"+str(info["description"]))
                        elif i == "-h":
                            print("Help:\n"+str(info["helpinfo"]))
                        else:
                            print("* Arg "+i+" not supported. Try help info.")

        except Exception as Error:
            system.Output.warn("Could not generate info - "+str(Error))
            pass
        except IndexError:
            system.Output.warn("Could Not Read File (No Args)")
            system.Output.info("Try typing help info")
