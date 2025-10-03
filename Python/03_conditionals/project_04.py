device_status = "active"
temp = 38

if device_status == "active":
    if temp > 35:
        print("temperature is high!!")
    else:
        print("temperature is normal ")
else:
    print("device is offline")