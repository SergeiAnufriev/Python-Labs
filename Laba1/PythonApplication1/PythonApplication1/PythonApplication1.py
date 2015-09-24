newline = '\r\n'

print ('Laboratornay rabota  1')
print ('Razrabotal student gr.101211 ' + newline)
name = input ("What is your name?" + newline)
print ('Hello ' + str(name) + '! ' + newline)
gruppa = str(input ("What is your gruppa?" + newline))
print ('gr', gruppa + newline)
save = input ("Vvedite svoy lybimuy frazu:" + newline)
print ('Vacha lybimuy frazu sohranena v otdelnom dokumente')

f = open ('texst.txt', 'w') 
f.write ('Laboratornay rabota  1' + '\n')
f.write (name + ' gr ')

f.write (gruppa + '\n')
f.write (save + '\n')
f.close
