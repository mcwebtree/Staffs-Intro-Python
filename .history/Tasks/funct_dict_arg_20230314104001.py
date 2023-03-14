
def ex3 ( **args ):
    for key, value in args.items():
        print ( key + ": " + value)


ex3 (bob="1", dave="2", steve="3")
