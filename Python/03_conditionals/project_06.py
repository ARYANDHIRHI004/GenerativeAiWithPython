seat_type = input("Enter seat type: ").lower()

match seat_type:
    case "sleeper":
        print("sleeper - No Ac, beds available")
    case "ac":
        print("AC - Ac, beds available")
    case "luxury":
        print("Raj Mahal -Premium seats with meal")
    case _:
        print("Majak mt kr")

        

