#  Դասավորել լիստը աճման կարգով
#  l = [1,9,8,5,4,7,8,5,6,3]

"""
con = True
while con:
    con = False

    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
            con = True
print(l)

"""
#======================================================

# Լրացնել լիստի պակասող տարրերը
# l = [1,2,5,8,9,15,20]

# տարբերակ 1

"""
maxl = l[0]
minl = l[0]
k = []
for i in range(len(l)):
    if maxl < l[i]:
        maxl = l[i]
    if minl > l[i]:
        minl = l[i]
for j in range(minl, maxl+1):
    k+=[j]
print(k)

"""

# տարբերակ 2

"""
k = []

for i in range(len(l)-1):
    if l[i+1] - l[i] == 1:
        k += [l[i]]
    else:
        x = l[i+1] - l[i]
        for j in range(x):
            k+=[l[i] + j]
k+=[l[-1]]
print(k)

"""
#=================================================

# Տպել տողի բառերը առանձին իրար տակ, ու հաշվել դրանց քանակը

# t = "Hi. my name is Vardges Khachatryan"

"""
k = ""
c = 0
for i in range(len(t)):
    if t[i] != " " and t[i] != ".":
        k+=t[i]
        if i == len(t) - 1:
            print(k)
            c += 1
    else:
        if k != "":
            c += 1
            print(k)
            k = ""
print(c)

"""

# Նույն արդյունքը արդեն ֆունկցիա կիրառելով

"""
c = 0
t = t.split(" ")

for i in t:
    c += 1
    print(str(i))
print(c)

"""

#================================================

# Փոխել լիստի և տողի համապատասխան տարրերը

# V - D
# t = "Hi. my name is Vardges Khachatryan"

"""
t = t[:t.index("V")] + "D" + t[t.index("V") + 1:]
print(t)

"""
# Կամ կիրառելով ֆունկցի
"""
t = list(t)

t[t.index("V")] = "D"
print("".join(t))
"""
#=======================================================

# Ներմուծել n և կառուցել n չափանի մատրիքս

"""
n = int(input("N: "))

l = []

for i in range(1,n+1):
    l+=[[]]
    for j in range(n):
        l[i]+=[j]
print(l)

"""
#================================================
# Գեներացնել n չափանի password

"""

import string
import random

def pass_gen(lenght_pass):
    all_let = string.ascii_letters # ֆունկցիան պարունակում է բոլոր մեծատառ և փոքրատառ տառերը
    all_num = string.digits # ֆունկցիան պարունակում է բոլոր թվանշանները
    all_char = all_let + all_num
    passW = ""
    for i in range(lenght_pass):
        passW += random.choice(all_char) # ֆունկցիան պատահական ընտրում է որևէ տարր 
    return passW


def main():
    while True:
        lenght_pass = input("N: ")

        try:
            lenght_pass = int(lenght_pass)
        except Exception as e:
            print(e)
            continue

        full_pass = pass_gen(lenght_pass)
        print(full_pass)

main()

"""
#========================================================

# Գուշակել թիվը

"""

import random

def number1():
    num = random.randint(1,20)
    return num

def main():
    number2 = number1()
    count = 1
    while True:
        print("Guess number ")
        n = input("N: ")

        try:
            n = int(n)
        except:
            print("Use only numbers")
            continue
            
        if n == number2:
            print("You win from {} time".format(str(count)))
            break
        elif n < number2:
            print("Go up")
        elif n > number2:
            print("Go down")
        count +=1
        print("=================================================")
main()
"""