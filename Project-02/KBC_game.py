#Day-13: KBC Quiz Game 
#Topics:Lists,Tuples,Loops,Conditionals,score logic
print("\n" + "="*30)
print(" Welcome to KAUN BANEGA CROREPATI ")
print("="*30 + "\n")
questions = ["How many states in India?:",
            "How many players in Rugby game?:",
            "What is the capital of nagaland:?",
            "Who was the first president of India?:",
            "Who is the current Chief Minister of Uttar Pradesh?:",
            "Who wrote the national Anthem of India?:",
            "How many bones are present in human body?:",
            "Who wrote the national song of India?:",
            "What is the duration of national anthem of India?:",
            "Which gas destroying the Ozone layer?:"]
options = [("A.27","B.29","C.28","D.30"),
           ("A.7","B.8","C.9","D.10"),
           ("A.Kohima","B.Gangtok","C.Dispur","D.Itanagar"),
           ("A.Rajendra Prasad","B.Jawaharlal Nehru","C.Mahatma Gandhi","D.APJ Abdul Kalam"),
           ("A.Adityanath Yogi","B.Kejriwal","C.Dinesh Sharma","D.Keshav Prasad maurya"),
           ("A.Bankim Chnadra chatterji","B.rabindranath tagore","C.Netaji","D.Chandrashekhar Azad"),
           ("A.209","B.206","C.211","D.210"),
           ("A.Bankim Chnadra chatterji","B.rabindranath tagore","C.Netaji","D.Chandrashekhar Azad"),
           ("A.52 sec","B.45 sec","C.54 sec","D.59 sec"),
           ("A.CFCs","B.Co2","C.N2","D.O2"),]
answers = ("C","A","A","A","A","B","B","A","A","A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("\n" + "=*30")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter(A,B,C,D):").upper()
    while guess not in ["A","B","C","D"]:
        print("Invalid input","Please enter a correct input")
        guess = input("Enter(A,B,C,D):").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Congratulations! Your Answer is Correct.")
    else:
        print("Oops! Your Answer is incorrect.")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("=============================")
print("      RESULTS      ")
print("=============================")

print("Answers:",end= " ")
for answer in answers:
    print(answer , end=" ")
print()

print("Guesses:", end= " ")
for guess in guesses:
    print(guess , end= " ")
print()

score = int((score/len(questions)*100))
print(f"Your Score is:{score}%")