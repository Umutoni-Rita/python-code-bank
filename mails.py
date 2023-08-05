

try:
   fhand = open('mbox.txt')
except:
   print('File not found')
   exit()

mailCount = {}
for lines in fhand:
   line = lines.rstrip()
   if line.startswith('From'):
      splitLine = line.split()
      email = splitLine[1]
      if email in mailCount:
         mailCount[email] = mailCount[email] + 1
      else:
         mailCount[email] = 1

print(mailCount)