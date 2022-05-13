#name = "Hello world"

#for i in name:
#    print(i)

#for i in range(1,6):
#    print(name)



#a = 1

#while a < 10:
#    print(a)
#    a+=1
#    break
    

#a = 1

#while a <= 10:
#    if a != 3:
#        print(a)
#    a+=1

a = "Hi, my 'ss' name is Vardges Khachatryan"

k = " "

for i in range(len(a)):
    if a[i] != " " and a[i] != ",":
        k+=a[i]
        if i == len(a) - 1:
            print(k)
    else:
        if k != " ":
            print(k)
        k = " "
    
    

for i in a:
    print(i)

