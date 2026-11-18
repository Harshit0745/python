import random
def game_win(user,computer):
    if user == computer:
        return None

    #snake vs water
    if user=="s" and computer=="w":
        return True
    if user=="w" and computer=="s":
        return False
    #water vs gun
    if user=="w" and computer=="g":
        return True
    if user=="g" and computer=="w":
        return False
    #snake vs gun
    if user=="s" and computer=="g":
        return False
    if user=="g" and computer=="s":
        return True


rand_no=random.randint(1,3)
print("computer's turn: snake(s),water(w),gun(g)")
if rand_no==1:
    computer="s"
elif rand_no==2:
    computer="w"
else:
    computer="g"

user=input("you turn: snake(s),water(w),gun(g)").lower()
if user not in ["s", "w", "g"]:
    print("Invalid choice!")
else:
    result=game_win(user,computer)
    print(f"\nyour choice:{user}")
    print(f"\ncomputer choice:{computer}")
    if result is None:
       print("It is a draw")
    elif (result):
       print("You Win!!!")
    else:
       print("You Lose!!!")
    