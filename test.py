s = input('문자열을 입력하시오: ')
vowels = "aeiouAEIOU"
result  = ""
for letter in s:
    if letter not in vowels:
        print(letter, end="")