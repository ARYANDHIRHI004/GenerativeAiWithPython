def get_input():
    print("getting user input...")

def validating_input():
    print("validating data...")

def save_to_db():
    print("Saving to database")

def register_user():
    get_input()
    validating_input()
    save_to_db()

register_user()



def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup

total_price = calculate_bill(5, 20)

print(total_price)