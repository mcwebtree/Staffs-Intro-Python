
def ex3 ( **kwargs  ):
    for key, value in kwargs.items():
        print ( key + ": " + value)


ex3 (bob="1", dave="2", steve="3")
