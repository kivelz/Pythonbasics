
input = (input("Do you want to shutdown?: "))

def __shut_down__(input) :
    if(input == "yes") :
        print("System shutting down")
    elif(input == "no"):
        print("shutdown aborted")
    elif(input != "yes" or input != "no"):
        print("sorry")
        
__shut_down__(input);