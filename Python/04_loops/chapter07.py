
flavours = ["masala", "jinger", "orange", "Out of stock"]

for flavour in flavours:
    if flavour == "Out of stock":
        continue
    if flavour == "Discontinued":
        break
    print(f"") 
