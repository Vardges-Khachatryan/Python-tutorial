s = "Hello world!" # տող
print(s)

s1 = """Hello 
world!""" # տողը գրվում է տարբեր տողերից
print(s1)

s2 = "Hello \nworld!" # \n-ից հետո գրվող տարրը տեղափոխվում է հաջորդ տող
print(s2)

s3 = 'Hello "world!"' # տողում ստանում ենք չակերտների մեջ տարր
print(s3)

s4 = "Hello"
s5 = " world"
s6 = s4 + s5 # երկու տողերը միացնում է իրար
print(s6)

s7 = 3*s # երեք անգամ տպում է նույն տողից
print(s7)

print(s[1]) # տպում է տողի երկրորդ տարրը
print(s[:5]) # տպում է տողը առաջին տարրից մինչև վեցերորդ տարրը չվերցրած
print(s[1:5]) # տպում է տողը երկրորդ տարրից մինցև վեցերորդ տարրը չվերցրած

s8 = s.upper() # տողի բոլոր տարրերը դարձնում է մեծատառ, արդյունքը վերադարձնում է
print(s8)

s9 = s.lower() # տողի բոլոր տարրերը դարձնում է փոքրատառ, արդյունքը վերադարձնում է
print(s9)

l = len(s) # որոշում է տողի տարրերի քանակը
print(l)

k = s.split(" ") # տողի տարրեր բաժանում է փակագծերում նշված պարամետրով, և պահում լիստի ձևով
print(k)

c = list(s) # առանձնացնում է տողի յուրաքանչյուր տարր, և պահում լիստի ձևով
print(c)

t = "".join(c) # բոլոր առանձնացված տարրերը միացնում է իրար, ըստ չակերտների մեջ առկա պարամետրի
print(t)
 

