def serve_chai():
    chia_type = "Masala"
    print(f"Insaide function {chia_type}")

chai_type = "Ginger"
serve_chai()
print(f"Outside function {chai_type}")


def chai_counter():
    chai_order = "lemon"

    def print_order():
        chai_order = "Ginger"
        print(f"Inner: {chai_order}")
    print_order()
    print(f"enclosed: {chai_order}")

chai_order = "orange"
chai_counter()
print("global: ", chai_order)

