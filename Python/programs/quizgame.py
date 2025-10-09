questions = ("how many element are there in the periodic table ?",
"which animal lays the largest eggs ?",
"what is the most abundant gas in the Earth's atmosphere?",
"How many bones are in the human body?",
"which plant in the solar system is the hottest?")

options = (("A. 27", "B. 118", "C. 87"),
           ("A. Ostrich", "B. Whales", "C. Tiger"),
           ("A. nito", "B. Oxy", "C. heli"),
           ("A. 306", "B. 206", "C. 300"),
           ("A. Mercury", "B. Mars", "C. Jupiter")
           )

answers = ("B", "A", "A", "B", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-"*20)
    print("Here is your question")
    print(question);
    for option in options[question_num]:
        print(option);
    
    while 1:
        guess = input("type your answer here: ").upper()
        if guess == "":
            print("you havent answer the question")
        else:
            break

    if guess == answers[question_num]:
        guesses.append("true");
        print("CORRECT!")
        score += 1;
    else:
        print("INCORRECT")
        print(answers[question_num] + " is the answer")
    question_num += 1;


print("-"*10)
print(f"Your score is: {score}")