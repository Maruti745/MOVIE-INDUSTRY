import random
options=['rock','paper','scissors']
computer_choice=random.choice(options)
user_choice=input('enter your choice=').lower()
if user_choice=='rock and computer_choice=='scissors':
print('you won')
elif user_choice=='paper' and computer_choice=='rock':
print('you won')
elif user_choice=='scissors' and computer_choice=='paper':
print('you won')
elif 
user_choice==computer_choice:
print('you tied')
else:
  print(f'you lost.The computer picked {computer_choice}')
  
  
