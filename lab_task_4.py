# Task 1 --luhan algorithm
card_number=[4,7,8,2,7,8,0,0,0,1,6,1,6,4,0,1]
limit=16
x=card_number.pop()
card_number.reverse()
for i in range(len(card_number)):
    if i%2==0:
        card_number[i]*=2
    if card_number[i]>9:
        card_number[i]-=9
for i in range(len(card_number)):
    x+=card_number[i]
if x%10==0:
    print("valid")
else:
    print("invalid")


# Task 2 --Remove Punctuations

import string
def remove_punction():
    s=input("enter a string: ")
    cleand_input=""
    for char in s:
        if char not in string.punctuation:
            cleand_input+=char
    print(cleand_input)
remove_punction()


# task 3 Sort text in Alphabetical Order
def sort(word):
    d=len(word)
    for  i in range(d -1):
        for j in range(d-i-i):
            if word[j] > word[j+1]:
                word[j],word[j+1]=word[j+1],word[j]
    return word
s=input(str("enter a string: "))
word=s.split()
sorted_word=sort(word)
print("".join (sorted_word))


