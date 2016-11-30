retezec = "-" * 20
print(retezec)

def tah_result(position, sign_player, sign_oponent):
    global retezec
    if position > 21 or position < 1:
        print("You are stupid, this number is not in given range")
        return False
    if retezec[position - 1] == "-":
        retezec = retezec[:position -1] +sign_player + retezec[position:]
        return True
    elif retezec [position - 1] == sign_oponent:
        print("This field is already taken by other player")
        return False
    elif retezec [position - 1] == sign_player:
        print("You already chose this field")
        return False
    else:
        print("wrong one!")
        return False

while True:
    while True:
        position_1 = int(input("Player 1 needs to chose number in range 1-20: "))
        smth1 = tah_result(position_1, "x", "o")
        if smth1 == True:
            break
    print(retezec)

    while True:
        position_2 = int(input("Player 2 needs to chose number in range 1-20: "))
        smth2 = tah_result(position_2, "o", "x")
        if smth2 == True:
            break
    print(retezec)

    if "xxx" in retezec:
        print("Player 1 wins")
        break
    elif "ooo" in retezec:
        print("Player 2 wins")
        break
    if not "-" in retezec:
        print("Nobody wins!")
        break
