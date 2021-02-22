print(f"""
+=======================================================================+
|      Title: THE GUESS GAME                                            |
|      Author: CypherX                                                  |
|      Description: This guess game asks the user to                    |
|                   create a strong password using 5 trials             |
|                   and play's 3 guess games after with 3 trials each   |
|                   after successfully creating the stong password      |
+=======================================================================+
""")
# CREATE A PASSWORD VALIDATOR FUNCTION THAT RETURNS VALID
# IF ALL STANDARDS (Upercase, Lowercase, Special character)is met
def validatePassword(input_x):
    trentA = ''
    trentB = ''
    trentC = ''
    trentD = ''
    uperAlpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowerAlpha = 'abcdefghijklmnopqrstuvwxyz'
    chars = '!@#$%^&*'
    nums = '0123456789'
    for x in input_x:
        if x in uperAlpha:
            trentA += x
        elif x in lowerAlpha:
            trentB += x
        elif x in chars:
            trentC += x
        elif x in nums:
            trentD += x
        else:
            pass
    if not len(input_x):
        result = "That was Empty😡😡😡"
    elif len(input_x) < 8:
        result = "That password wa not long enough😌"
    elif not len(trentC):
        result = "*There must be a special character😏"
    elif not len(trentB):
        result = "*There must be a lower case😏"
    elif not len(trentA):
        result = "*There must be at least one upper case😏"
    elif not len(trentD):
        result = "*There must be at least one number😏"
    else:
        result = "valid"
    return result
# DEFINE TRIAL GAME FUNCTION
def guess_game(trials, word, stage_number):
    print("Welcome to STAGE",stage_number,'(you have',trials,' trials):')
    while trials > 0:
        user_input = str(input("ENTER YOUR GUESS => "))
        if user_input.lower() == word.lower():
            print("Wow! You win......🤝🥳🥳")
            break
        else:
            print("Oops! That was wrong. You have",trials," trial(s) left🥴")
            trials -= 1

# WELCOME/INSTRUCTIIONS FOR THE USER
print(f"""
Hi Dear, 
Welcome to CypherX Guess Game. 🤓
Before we start, you must create a strong password to prove your 
security conciousness.
Hint: A strong password must contain uppercase/capital letters, 
      lowercase/small letters and at least one special character 
      yet must be over 7 charachters long....... :)😇
Goodluck.
""")

# ACCEPT THE USER INPUT FOR THE PASSWORD
pass_trial = 5

while pass_trial > 0:
    user_pass = str(input('Create Strong Password=> '))
    if validatePassword(user_pass) == 'valid':
        print("Yes! you did it, please proceed to the game. :)")
        break
    else:
        pass_trial -= 1
        print(validatePassword(user_pass)+'. Try again, '+str(pass_trial-1)+' trial(s) left.')

# CALL THE GUESS_GAME() FUNCTION THEN SET ARGUMENT
guess_game(trials=3, word='ETHICAL', stage_number=1)
guess_game(trials=3, word='NIIT', stage_number=2)
guess_game(trials=3, word='HACKTIVIST', stage_number=3)

# THIS IS BUT JUST THE CREDIT
print("")
print("Thank you for playing......")
print(f"""
CREDITS:
    + Enahoro Godwin (CypehrX: Python programer/Ethical hacker/Thinker/Social engineer)👨🏽‍💻🥋🏋🏼‍♀️
    + Michael (Instructor @NIIT_Festac/Python programer/)👨🏽‍💻🏀🏋🏼‍♀️

    ~~~~~~~~~~~~~~TO GOD BE THE GLORY~~~~~~~~~~~~~~~~~~~~~~~~~~
""")




