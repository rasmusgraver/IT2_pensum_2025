tall = 0
while tall < 1E6:
    t = str(tall)
    if tall > 1000 and t[0] == "1" and t[1] == "1" and t[2] == "1" and t[3] == "1":
        break
    tall += 7

print("FERDIG. Tallet er", tall)