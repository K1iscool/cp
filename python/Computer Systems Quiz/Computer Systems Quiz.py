import random



#sub




#main

questions = []
file = open("L9Questions.txt","r")

for line in file:
    line = line.strip()
    questions.append(line)

file.close()
#random.shuffle(questions)

    
questions_number = 1

for question in questions:
    parts = question.split(",")
    q = parts[0]
    correct_answer = parts[1]
    
    
print(questions)