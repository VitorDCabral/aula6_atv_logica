str = input("Digite uma palavra: ")
li = list(str) 
ln = len(li) 
revStr = ""
i = ln - 1

while i >= 0:
    revStr = revStr + li[i]
    i = i - 1
str = str.lower()
revStr = revStr.lower()

if str == revStr:
    print(str, ", é um PALINDROMO!")
else:
    print(str, ", não é PALINDROMO!")