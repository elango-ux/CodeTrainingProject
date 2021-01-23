# infiniteloop  true in while  get input and quit 
while True:
    command = input(">")
    print("ECHO",command)
    if command.lower()=="quit":
        break
