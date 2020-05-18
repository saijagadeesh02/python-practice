def ask():
    while(True):
    
        try:
            a = int(input("Input an integer:"))
            a = a**2
        except:
            print("An error occurred! Please try again! Seems like you haven't passed an integer")
            continue
        else:
            print(f'Thank you, your number squared is:{a}')
            break
ask()