ans='y'
while ans!='n':
    try:
        user_input = input("Please enter a whole number: ")
        try:
            number = abs(int(user_input))
            print(f"Great! You entered the whole number: {number}")
            
        except ValueError:
            print("You must enter a whole number!")
            
        finally:
             ans = input("Do you want to try again? (y/n): ").lower()
             if ans != 'y':
                print("Ok, see you next time!")
                
    except KeyboardInterrupt:
        print("\nYou pressed Ctrl+C! See you next time!")
        break
