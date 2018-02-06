word_list = ['hello','world','my','name','is','Anna']
char = 'o'
newvar = ''

for i in range(0, len(word_list), 1):
    if word_list[i].find(char) > 0:
        newvar = newvar + word_list[i]

print newvar
