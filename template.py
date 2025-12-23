class Environment:
    LibInfo = {
        "name": "Template",
        "credits": [],
        "version": 0,
        "reqVersion": 0,
        "description": "Lorem Ispum Dolor Sit Amit",
        "helpinfo": "Lorem Ispum Dolor Sit Amit"
    }
    import libload as lib
    global libs, system
    libs = lib.load_libs()
    system = libs["system"]
    def RunFromEnv(function):return function