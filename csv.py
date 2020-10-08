olym= [("s", 25,"long jump"),
("a", 26,"research"),
("m", 25, "Smoke")]

file = open('covid.csv','w')
file.write('Name,Age,Game')

print('Name','Age', 'Game')
for i in olym:
    #row= ','.join([i[0], i[1], i[2]])
    row= '{},{},{}'.format(i[0], i[1], i[2])
    file.write('\n')
    file.write(row)


file.close()

file= open('emotion_words.txt','r')
emotions=[]
emotions= [i.split()[0]for i in file]
print(emotions)