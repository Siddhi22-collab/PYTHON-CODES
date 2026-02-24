week=int(input("enter a week day"))
match week:
        case 1:
            print("sunday")
        case 2:
            print("monday")
        case 3:
            print("Tuesday")
        case 4:
            print("wednesday")
        case 5:
            print("thursday")
        case 6:
            print("friday")
        case 7:
            print("saturday ")
        case _:
            print("undefine week day")