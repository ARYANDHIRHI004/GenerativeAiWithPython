name = ["Aryan", "Arun", "Sam", "Ali"]

bill = [50, 100, 56, 45]

for bill, name in zip(bill, name):
    print(f"{name} paid {bill}")


