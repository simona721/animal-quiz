print("Wellcome to quiz game !!")
print('NOTE: if your spelling is incorrect then it is considered as wrong answer')
score = 0
question_no = 0
playing = input('Do you want to play ? ').lower()
if playing == 'yes':
    question_no += 1
    ques = input(f'\n{question_no}.Which animal has black stripes? ').lower()
    if ques == 'zebra':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> zebra')

# ------1
    question_no += 1
    ques = input(f"\n{question_no}.Which animal is a man's best friend? ").lower()
    
    if ques == 'dog':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> dog')

# -----2
    question_no += 1
    ques = input(f'\n{question_no}.Which animal has 9 lives? ').lower()
    
    if ques == 'cat':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> cat')

# -----3
    question_no += 1
    ques = input(f'\n{question_no}.Which animal is the king of the jungle? ').lower()
    
    if ques == 'lion':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> lion')


# -----4
    question_no += 1
    ques = input(f'\n{question_no}.Which animal sleeps in winter? ').lower()
    
    if ques == 'bear':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> bear')


# ------5 

else:
    print('thank you you are out of a game.')
    quit()

print(f'\nnumber of question is {question_no}')
print(f'your score is {score}')
try:
    percentage = (score *100)/question_no
except ZeroDivisionError:
    print('0% quetions are correct')

print(f'{percentage}% questions are correct.')


