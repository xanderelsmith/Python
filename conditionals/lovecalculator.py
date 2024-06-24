print('The love Calculator is calculating your score...')
name1=input( 'What is your name')
name2=input( 'What is the second name')
combinedname=name1+name2
lowerCaseValue=combinedname.lower()
t=lowerCaseValue.count('t')
r=lowerCaseValue.count('r')
u=lowerCaseValue.count('u')
e=lowerCaseValue.count('e')
firstNum=t+r+u+e

l=lowerCaseValue.count('l')
o=lowerCaseValue.count('o')
v=lowerCaseValue.count('v')
e=lowerCaseValue.count('e')
secondNum=l+o+v+e

totalValue=int(str(firstNum)+str(secondNum))

if totalValue <30:
    print(f'Your score is {totalValue}')
elif totalValue<90:
    print(f'Your score is {totalValue}')

    
    


