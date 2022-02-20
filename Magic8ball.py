"""Magic 8-Ball
The Magic 8-Ball is a popular toy developed in the 1950s for fortune-telling or advice seeking.

Write a magic8.py Python program that can answer any “Yes” or “No” question with a different fortune each time it executes."""

import random
name,question = "Reza","Are we living?"
answer=""
random_number=random.randint(1, 9)
print(random_number)
if random_number==1:
  answer="Yes - definitely."
elif random_number==1:
  answer="It is decidedly so."
elif random_number==2:
  answer="Without a doubt."
elif random_number==3:
  answer="Reply hazy, try again."
elif random_number==4:
  answer="Ask again later."
elif random_number==5:
  answer="Better not tell you now."
elif random_number==6:
  answer="My sources say no."
elif random_number==7:
  answer="Outlook not so good."
else:
  answer="Very doubtful."
output=f"""{name} asks: {question}
magic 8-Ball's answer: {answer}""" 
print(output) 
random_number=random.randint(1, 9)
print(random_number)
list_of_answers= ["Yes - definitely","It is decidedly so",'Without a doubt',"Reply hazy","Ask again later","Better not tell you now.","My sources say no","Outlook not so good","Very doubtful."]
answer=list_of_answers[random_number-1]
output=f"""{name} asks: {question}
magic 8-Ball's answer: {answer}""" 
print(output) 
