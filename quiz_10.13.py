# COMP9021 20T3 - Rachid Hamadi
# Quiz 3 *** Due Friday Week 5 @ 10.00pm

# Prompts the user for an arity (a natural number) n and a word.
# and underscores.
# inductive definition:

import sys
import string

def is_valid(word, arity):
    word_new = word.replace(' ','')
    valid_sysbol = ['(',')',',','_']

    for i in range(len(word_new)):
        if word_new[i] not in valid_sysbol and word_new[i] not in string.ascii_lowercase and word_new[i] not in string.ascii_uppercase:
            return False
        if word_new.count('(') != word_new.count(')'):
            return False
        if arity == 0 and word_new.count('(') != 0:
            return False

    word_stack = []
    create_string = ''
    
    for i in range(len(word_new)):
        if word_new[i] == '(':
            if create_string != '':
                word_stack.append(create_string)
                word_stack.append('(')
            else:
                word_stack.append('(')
                #print(word_stack)
            create_string = ''
            
        elif word_new[i] == ',':
            if create_string != '':
                word_stack.append(create_string)     
               # print(word_stack)
            create_string = ''
            
        elif word_new[i] == ')':
            if create_string != '':
                word_stack.append(create_string)     
                #print(word_stack)
            create_string = ''            
           
            arity_string = ''
            for j in range(arity+1):
                try:
                    arity_string = word_stack.pop()
                except:
                    return False
              #  print(arity_string)
              #
#            while arity_string != '(' and word_stack != []:
#               arity_string = word_stack.pop()
#               print(arity_string)
        else: 
            create_string += word_new[i]
           # print(create_string)
            
        
    if create_string != '' and arity == 0:
        word_stack.append(create_string)
    
    if len(word_stack) == 1:
        return True
    else:
        return False
    

    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE

try:
    arity = int(input('Input an arity : '))
    if arity < 0:
        raise ValueError
except ValueError:
    print('Incorrect arity, giving up...')
    sys.exit()
word = input('Input a word: ')
if is_valid(word, arity):
    print('The word is valid.')
else:
    print('The word is invalid.')
