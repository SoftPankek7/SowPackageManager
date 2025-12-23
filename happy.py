class Environment:
    LibInfo = {
        "name": "Happy Birthday!",
        "credits": ["Charlie T"],
        "version": 1.0,
        "reqVersion": 1.3,
        "description": "It's a birthday cake!",
        "helpinfo": "happy [name] - name is not needed."
    }
    import libload as lib
    global libs, system
    libs = lib.load_libs()
    system = libs["system"]
    def RunFromEnv(function):
        if len(function) >= 1:
            name = function
            print(system.Output.Format.RESET)
            print(system.Output.Format.BRIGHT_YELLOW+"           .  .  .  .  ."+system.Output.Format.RESET)
            print(system.Output.Format.BRIGHT_CYAN+"           |  |  |  |  |"+system.Output.Format.RESET)
            print("          "+system.Output.Format.BG_BRIGHT_RED+".-------------."+system.Output.Format.RESET)
            print("          "+system.Output.Format.BG_BRIGHT_RED+"|~~~~~~~~~~~~~|"+system.Output.Format.RESET)
            print("          "+system.Output.Format.BG_BRIGHT_RED+"|~~~~~~~~~~~~~|"+system.Output.Format.RESET)
            print("          "+system.Output.Format.BG_BRIGHT_RED+"[_____________]"+system.Output.Format.RESET)
            print("          Happy birthday,")
            print(system.Output.Format.LIB_RESET)
            for i in range(len(name)):
                sepe = "," if not i == len(name)-1 else ""
                print("          "+str(name[i])+sepe)
            
        else:
            print(system.Output.Format.RESET)
            print(system.Output.Format.BRIGHT_YELLOW+"           .  .  .  .  ."+system.Output.Format.RESET)
            print(system.Output.Format.BRIGHT_CYAN+"           |  |  |  |  |"+system.Output.Format.RESET)
            print("          "+system.Output.Format.BG_BRIGHT_RED+".-------------."+system.Output.Format.RESET)
            print("          "+system.Output.Format.BG_BRIGHT_RED+"|~~~~~~~~~~~~~|"+system.Output.Format.RESET)
            print("          "+system.Output.Format.BG_BRIGHT_RED+"|~~~~~~~~~~~~~|"+system.Output.Format.RESET)
            print("          "+system.Output.Format.BG_BRIGHT_RED+"[_____________]"+system.Output.Format.RESET)
            print("          Happy birthday!")
            print(system.Output.Format.LIB_RESET)
            
        return function;