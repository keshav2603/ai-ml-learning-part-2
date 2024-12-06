questions = [
    ["What is the correct file extension for Python files?", 
     "A) .pyth", "B) .pt", "C) .py", "D) .python", 
     "c"
    ],
    ["Which of the following is the correct syntax to output 'Hello, World' in Python?", 
     "A) echo 'Hello, World'", "B) print('Hello, World')", "C) printf('Hello, World')", "D) cout << 'Hello, World'", 
     "b"
    ],
    ["What is the correct way to create a function in Python?", 
     "A) function myFunction()", "B) def myFunction()", "C) create myFunction()", "D) function:myFunction()", 
     "b"
    ],
    ["How do you insert comments in Python code?", 
     "A) // This is a comment", "B) <!-- This is a comment -->", "C) # This is a comment", "D) % This is a comment", 
     "c"
    ],
    ["Which operator is used for exponentiation in Python?", 
     "A) ^", "B) **", "C) *", "D) %", 
     "b"
    ],
    ["What is the output of the following code: print(2 + 3 * 4)?", 
     "A) 20", "B) 14", "C) 18", "D) 12", 
     "b"
    ],
    ["Which of the following is a mutable data type in Python?", 
     "A) Tuple", "B) String", "C) List", "D) Integer", 
     "c"
    ],
    ["What will be the result of this code: print(type('Hello'))?", 
     "A) <class 'int'>", "B) <class 'list'>", "C) <class 'str'>", "D) <class 'tuple'>", 
     "c"
    ],
    ["Which keyword is used to define a class in Python?", 
     "A) def", "B) class", "C) object", "D) define", 
     "b"
    ],
    ["How can you convert a string 'x = 123' to an integer in Python?", 
     "A) int(x)", "B) str(x)", "C) float(x)", "D) eval(x)", 
     "a"
    ]
]
prices = (
    10,
    100,
    1000,
    10000,
    50000,
    100000,
    150000,
    200000,
    1000000,
    10000000
)


print("welcome to our KBC show!!!\n")

def displayQuestion(questionNo):
    print(f"{questionNo}) {questions[questionNo][0]}")
    print(questions[questionNo][1])
    print(questions[questionNo][2])
    print(questions[questionNo][3])
    print(questions[questionNo][4])
    
def checkAnswer(questionNo, answer):
    if(answer == questions[questionNo][5]):
        return True
    else:
        return False

moneyWin = 0
currentQuestion = 1
while(True):
    if(currentQuestion == 11):
        print("Congratulations! You have answered all questions correctly and won the grand prize of $10,000,000!")
        break

    displayQuestion(currentQuestion-1)
    ans = input("Enter your answer : \n").lower().strip()
    result = checkAnswer(currentQuestion-1, ans)
    if(result):
        moneyWin = prices[currentQuestion-1]
        print(f"your ans is correct and total money won : ${moneyWin}")
        currentQuestion=currentQuestion+1
    else:
        print(f"you lost your ans is incorrect and money you won ${prices[currentQuestion-2]}")
        
        break



