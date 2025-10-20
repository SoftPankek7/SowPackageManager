'''

An Example Lib to aid begginers to know how to create their own libaries.
Basically adds two numbers together from the Command Line Arguments.

'''

class Environment:

    LibInfo = {
        "name": "ExampleLib",
        "credits": ["PersonA", "PersonB"],
        "version": 10.0,
        "description": "An Example Lib to aid begginers to know how to create their own libaries.\nBasically adds two numbers together from the Command Line Arguments.",
        "helpinfo": "examplelib [A] [B]\nReturns [A] + [B] in text\n[A] and [B] have to be integer friendly to work."
    }

    # Include the system - so we can do text formatting, output, etc.
    import libload as lib
    global libs, system
    libs = lib.load_libs()
    system = libs["system"]

    def RunFromEnv(func):
        # SYSTEM.LPRINT :  Prints text (for libs) - and then automatically resets the text at the end.
        #      ||||||      It makes it easier & smaller to print out text :) However, it sacrifices
        #      VVVVVV      some stuff - such as arguments e.g: print("Hello!", end="!!!")
        system.lprint(system.Output.Format.BLUE + "Examplelib Arguments: "+str(func))

        if len(func) != 2: # Check if running with 2 Command Line Args
            print("This is an example library that adds two numbers.")
            # Why yes, Yes it is!
            # Feel free to learn how to make libaries
            # from this :)
            print("How about try running this via")

            system.lprint(system.Output.Format.ITALIC + system.Output.Format.RED + "examplelib 1 1") # Keep output DIM always, for clarity.
        else:
            output = Environment.add(func[0], func[1]) # Add the 2 Command Line Args together.
            if output != False:
                system.lprint(system.Output.Format.ITALIC + str(func[0]) +" + "+str(func[0])+" = "+str(output))
            else:
                print("Hey, those aren't numbers!")

        print(Fact()) # Just a cool fact!

    def add(a, b):
        try:
            return int(a)+int(b)
        except:
            return False

def Fact():
    return "Functions don't need to be in the Environment Class!"
