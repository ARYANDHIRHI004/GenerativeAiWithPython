def function_name():
    return "Aryan"

def make_chai():
    return "Here is your chai"

return_value = make_chai()

print(return_value)

def idle_chaiwala():
    pass

def chai_status(cups_left):
    if cups_left == 0:
        return "sorry, chai over"
    return "Chai is ready"

print(chai_status(0))
print(chai_status(5))

def chai_report():
    return 100,  20, 420

sold, remaining, paid = chai_report()
