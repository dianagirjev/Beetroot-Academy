import time

temp = 0
while temp <= 5:
    time.sleep(1)
    print(f"Temp este {temp}")
    temp += 1


temp = 0
while True:
    time.sleep(1)
    print(f"Temp este {temp}")
    if temp > 5:
        break
    temp += 1