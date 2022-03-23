print("Hello I'm Laura")

number = 3
if number>0:
    print("The number is greater than zero")
else:
    print("The number is smaller than zero")

text1 = 'Laura'
print(text1[1:3])

text2 = 'Pusz'

result = text1 + " " + text2
print(result)

text3 = text1*10
print(text3)

print(len(text3))

fp = open("words")
print(fp.read())
fp.close()

