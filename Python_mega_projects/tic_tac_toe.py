
l1=[1,2,3,4,5,6,7,8,9]
def show(*l):
    a=0
    for i in range(0,3):
        for j in range(a,a+2+1):
            print(f"|{l[j]}|",end="")
        # print("_ _ _")
        print("")
        a=a+2+1
def check(sign,*l):
    if ((l[0]==sign)and (l[1]==sign)and (l[2]==sign)):
        # print(f"YOU won who type {l[0]}")
        return True
    elif ((l[0]==sign) and (l[4]==sign) and (l[8]==sign)):
        # print(f"You won who type {l[0]}")
        return True
    elif ((l[0]==sign) and (l[3]==sign) and (l[6]==sign)):
        # print(f"You Won who type {l[0]}")
        return True
    elif ((l[3]==sign) and (l[4]==sign) and (l[5]==sign)):
        # print(f"YOu won who type {l[3]}")
        return True
    elif ((l[6]==sign) and (l[7]==sign) and (l[8]==sign)):
        # print(f"You won who type {l[6]}")
        return True
    elif ((l[1]==sign) and (l[4]==sign) and (l[7]==sign)):
        # print(f"You won who type {l[6]}")
        return True
    elif ((l[2]==sign) and (l[5]==sign)and (l[8]==sign)):
        # print(f"You won who type {l[2]}")
        return True
    elif ((l[2]==sign) and (l[4]==sign)and (l[6]==sign)):
        # print(f"You won who type {l[2]}")
        return True
    else:
        return False



show(*l1)
# l.clear()
l = [0,0,0,0,0,0,0,0,0]
print("Now select the position where you want to put X or O")

n = 1
c=n
while n!=10:

    number = input("Enter the position number (1, 2, 3, 4, 5, 6, 7, 8 or 9): ")
    if number not in ["1", "2", "3" ,"4" ,"5","6","7","8","9"]:
        print("Invalid position number. Please enter.")
        continue
   
    sign = input("Enter either X or O: ").upper()
    if sign not in ["X", "O"]:
         print("Invalid sign. Please enter X or O.")
         continue
    
    if number == "1" and l[0]==0:
        l[0] = sign
        print("For understanding")
        show(*l1)
        print("")
        show(*l)
        # n += 1
    elif number == "2"  and l[1]==0:
        l[1] = sign
        print("For understanding")
        show(*l1)
        print("")
        show(*l)
        # n += 1
    elif number == "3" and l[2]==0:
        l[2] = sign
        print("For understanding")
        show(*l1)
        print("")
        show(*l)
        # n += 1
    elif number == "4" and l[3]==0:
        l[3] = sign
        print("For understanding")
        show(*l1)
        print("")
        show(*l)
        # n += 1
    elif number == "5" and l[4]==0:
        l[4] = sign
        print("For understanding")
        show(*l1)
        print("")
        show(*l)
        # n += 1
    elif number == "6" and l[5]==0:
        l[5] = sign
        print("For understanding")
        show(*l1)
        print("")
        show(*l)
        # n += 1
    elif number == "7" and l[6]==0:
        l[6] = sign
        print("For understanding")
        show(*l1)
        print("")
        show(*l)
        # n += 1
    elif number == "8" and l[7]==0:
        l[7] = sign
        print("For understanding")
        show(*l1)
        print("")
        show(*l)
        # n += 1
    elif number == "9" and l[8]==0:
        l[8] = sign
        print("For understanding")
        show(*l1)
        print("")
        show(*l)
        # n += 1
    else:
        print("Position already taken. Please choose a different position.")
    for sign in ["X","O"]:
        if check(sign,*l):
            print(f"{sign},you won")
            break
        else:
            print(f"{sign},please play again")
    if check(sign,*l):
        break
    n=n+1
if check(sign,*l)==False:
    print("Draw Match")



# print("Final board state:", l)
# show(*l)

