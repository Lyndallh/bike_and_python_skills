from PIL import Image
big_jump_img = Image.open("big_jump.png")
practice_jump_img = Image.open("practice_jump.png")
practice_session_img = Image.open("practice_session.png")
chopper_img = Image.open("chopper.png")
rockstar_img = Image.open("rockstar.png")


bikes_you_own = int(input("How many bikes do you own?\n"))
bikes_you_should_own = bikes_you_own + 1
print (f"The correct number of bikes to own is {bikes_you_should_own} bikes\n")


can_land_big_jump = False
attempted_big_jump = False
all_practices = 0


print("That big jump looks fun...BUT...\nUntil you have mastered small jumps, you shouldn't attempt big jumps")

big_jump_img.show()
while attempted_big_jump == False: 
    # Keep asking if are going to attempt the big jump until you have attempted the big jump
    attempted_big_jump = input('Are you going to attempt the big jump now? y/n :\n').lower().strip() == 'y'
    if attempted_big_jump == True:
         break # jump has been attempted, no need to ask again
    
    # Jumping coach said to take it slow and practice - at least 50 times - before taking it to the next level
    while all_practices in range (0,49):
        print("You chose to do a practice session on a small jump")
        practice_jump_img.show()
        num_practices = input("How many practice jumps did you do in this session? \n")
        increment = int(num_practices)
        all_practices = (increment+all_practices)
        if all_practices < 50:
            print(f"Good work {all_practices} small jumps down, another {50-all_practices} to go before you have mastered small jumps\n")
            practice_session_img.show()
            # But impatience...
            attempted_big_jump = input('Are you going to attempt the big jump now? y/n :\n').lower().strip() == 'y'
            if attempted_big_jump == True:
                break  # Impatience monster has been fed

    if all_practices >= 50: # coach will be pleased
         print(f"Your total practice jumps are {all_practices}\nNow you're ready to try the big jump")
         can_land_big_jump = True
         
if attempted_big_jump == True:
    print(f"You ride fast toward the jump and since you have practiced {all_practices} times...\n....\n......\n.......")
    big_jump_img.show()
    # can_land_big_jump = input('Did you land the big jump? y/n :').lower().strip() == 'y'
    if can_land_big_jump == True:
            print("You did it, amazing! You are a rock star!\n\n\n")
            rockstar_img.show()
    elif can_land_big_jump == False:
            print("Damn, you crashed hard - get to the chopper!\n\n\n")
            chopper_img.show()