class Environment:
    LibInfo = {
        "name": "Execute",
        "credits": ["Charlie T"],
        "version": 1.0,
        "reqVersion": 1.3,
        "description": "Excecute python/shell/environment code arbituarily",
        "helpinfo": "ex -[s/p/e](s = shell, p = python, e = environment) [code]\nExample code:\n  ex -s echo Hello, World!\n  ex -p print(\"Hello, World!\")\n  ex -e exit"
    }

    import libload as lib
    global libs, system
    libs = lib.load_libs()
    system = libs["system"]

    def RunFromEnv(func):
        if len(func) < 2:
            print(f"You have {len(func)}/2 Arguments.\n - See help ex for more info")
            return 1;
        else:
            if not func[0] in ["-s", "-p", "-e"]:
                print(f"Invalid CLI switch ({func[0]})\n - See help ex for more info")
                return 2;
            else:
                if func[0] == "-s":
                    import os
                    os.system(func[1])
                elif func[0] == "-p":
                    exec(func[1])
                elif func[0] == "-e":
                    system.ShellRuntime.CommandRunner.Exec(func[1])
                else:
                    print(f"Unprocessable CLI switch ({func[0]})\n - See help ex for more info")
if __name__ == "__main__":
    print("This file cannot run without the Environment.")