sentence = input('Enter any sentence\n')
wordslist = sentence,split()
result =''
for word in wordslist:
    result += word.upper()+' '
print(result)
