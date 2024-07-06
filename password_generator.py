#PASSWORD GENERATOR - TASK 3 - CODSOFT
#password generator through user defined length and complexity

import random

def passwgen(length,cmplex):    #function definition
    password=""
    if cmplex == 'weak':
        l=[ int(val) for val in range(65,91)]         # weak - only alphabets
        l+=[int(val) for val in range(97,123)]
    elif cmplex == 'medium':
        l=[ int(val) for val in range(65,91)]         # medium - only alphanumeric characters
        l+=[int(val) for val in range(97,123)]
        l+=[ int(val) for val in range(48,58)]
    elif cmplex == 'strong':
         l=[ int(val) for val in range(65,91)]       # strong - only alphanumeric characters and special characters
         l+=[int(val) for val in range(97,123)]
         l+=[ int(val) for val in range(33,58)]
    else:
        print("Entered an Invalid Operation..Please Try again..!!")

    while length>0:
        password += chr(random.choice(l))
        length-=1
        random.shuffle(l)                    #random shuffle to get better combination of characters and complexity level


    print("The Generated Password for {} length and {} complexity is :".format(length,cmplex))
    print(password)
    print("""

""")


length=int(input("Enter your Password's Length :"))
print("""

** for 'EASY' enter 'weak'
** for 'MODERATE' enter 'medium'
** for 'DIFFICULT' enter 'strong'

  >>> values are case-sensitive <<<

""")


cmplex=input("Enter password's Complexity Level :")

passwgen(length,cmplex)      #function call

print(" --- PROCESS COMPLETED ---") 
