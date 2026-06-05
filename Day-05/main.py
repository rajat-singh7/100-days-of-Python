#Some More Question on if-elif-else:
password = "Sarita8423@"
user_Input = input("Enter a password to log in:")
if password == user_Input:
    print("Access Granted")
else:
    print("Access Denied.\ntry Again")

#Match case Statements...(A type of if elif else)
x = 6 # x is the variable to match
match x:
    case 0: #If x ix zero
        print("X is Zero")
    #Case with if-conditions
    case 4:
        print("Case is 4")
    case _: #default Case
        print(x)

a = 90
match a:
    case 0:
        print("A is Zero")
    case 4:
        print("Case is 4")
    case _ if a!=90:
        print(a,"is not 90")
    case _ if a!=80:
        print(a,"is not 80")
    case _:
        print(a)
command = input("Enter your command:").lower()
match command:
    case "start":
        print("Engine is Starting....")
    case "stop":
        print("Engine is Stopping....")
    case "pause":
        print("Engine is paused...")
    case _:
        print("Unknown command")

pin = 5250
balance = 56000
pin_input = input("Enter PIN:")
match pin_input:
    case "5250":
        command1 = input("Enter Balance/withdraw/exit:").lower()
        match command1:
            case "balance":
                print(f"Balance: ₹ {balance}")
            case "withdraw":
                print(f"Enter Amount: ")
            case "exit":
                print("Thanks to visit")
            case _:
                print("Invalid option")
    case _:
        print("Wrong Pin")

