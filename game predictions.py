#Game predictions
#there are four contestants ( bob, maggi, panther and cena)

questions = (" who do you think will win the race?:",
             
             "Do you think there can be a tie in the race?:")

options =(("A. bob", "B. maggi", "C. panther", "D. cena" "E. not sure"),
          ("A. yes", "B. no", "C. Not sure" ))
answers =("E" , "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------------")
    print(questions)
    for option in options[question_num]:
        print(option)
    guess = input("enter(A,B,C,D,E):").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print ("correct!")
    else:
        print("incorrect!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1
