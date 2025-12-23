# 💻

class Environment:
    LibInfo = {
        "name": "Better Shell",
        "credits": ["Charlie T"],
        "version": 1.0,
        "reqVersion": 1.3,
        "description": "Just a cooler shell, imitating linux-like systems",
        "helpinfo": "bettershell (gliph) - \nGliph is the character displayed in the CLI interface. Defaults to 💻."
    }

    import libload as lib
    global libs, system
    libs = lib.load_libs()
    system = libs["system"]

    def RunFromEnv(func):
        print("[*] Press ^C to exit into normal shell.")
        if len(func) >= 1:
            gliph = func[0]
        else:
            gliph = "💻"
        cli = system.Output.Format.RESET + system.Output.Format.BG_BLUE + " "+gliph+"   " + system.Output.Format.RESET + system.Output.Format.BLUE + ">" + system.Output.Format.RESET + " "
        while True:
            cmd = input(cli)
            if cmd.strip() != "":
                system.ShellRuntime.CommandRunner.Exec(cmd)
if __name__ == "__main__":
    print("This file cannot run without the Environment.")