l = ["A","B","C","D","E","F"]  # Լիստ

for i in l: # Ցիկլ, որտեղ i-ին վերագրվում է l լիստի տարրերը
    print(i)

for i in range(len(l)): #  Ցիկլ, որտեղ i-ին վերագրվում է l լիստի տարրերի ինդեքսները
    print(i)

for i in range(1,5,1): # Ցիկլ, որտեղ i-ին վերագրվում է l լիստի տարրերի ինդեքսները սկսած 1-ից մինչև 5(չներառյալ)
    print(i)

for i in range(len(l)): 
    print(l[i])

a = 10

while a <= 20: # Ցիկլ, որը կաշխատի մինչև նշված պայմանի բավարարելը
    print("OK")
    a+=1
    break # Ցիկլը դադարում է առաջին պտույտից հետո
