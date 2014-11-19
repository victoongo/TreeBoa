## week 5
# Assignment
largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    
    if num == "done" : 
        break
    else:
        try:
            num = int(num)
            if largest is None:
                largest = num
            elif largest < num:
                largest = num
            if smallest is None:
                smallest = num
            elif smallest > num:
                smallest = num
        except: 
            print "Invalid input"        
            continue
    #print num

print "Maximum is", largest
print "Minimum is", smallest


## week 6
# Lecture
fruit = 'banana'
x = fruit[1]
fruit[1:3]
fruit[:]
x = fruit[1:]
fruit[:3]

for l in fruit:
    print l

a = 'there'
b = 'hello' + ' ' + a
print b

if 'n' in fruit:
    print 'found it'

hi = 'Hi!'
hil = hi.lower()
print hil
print "Hi There!".lower()

dir(hi)

pos = fruit.find('n')
print pos
posz = fruit.find('z')
print posz

fruit2 = fruit.replace('n','z')
print fruit2

greet = '  hi, dude! '
greet.lstrip()
greet.rstrip()
greet.strip()
sentence = "hi there"
sentence.startswith('h')

d = 'haha me@duke.edu 30298204932'
atpos = d.find('@')
print atpos
sppos = d.find(' ',atpos)
print sppos
ad = d[atpos+1:sppos]
print ad

# Assignment: 
# 6.5 Write code using find() and string slicing (see section 6.10) 
# to extract the number at the end of the line below. Convert the extracted 
# value to a floating point number and print it out.
text = "X-DSPAM-Confidence:    0.8475"
sppos = text.find(' ')
text2 = text[sppos:]
num = text2.strip()
fnum = float(num)
print fnum

## week 7
# external
import os
os.getcwd()
os.chdir('/home/victor/Projects/TreeBoa/informatics/')

# lecture
str1 = 'x\ny'
print len(str1) # 3, not 4, character length

fhandle = open('code/curl1.py','r')
print fhandle
line_count = 0
for line in fhandle:
    print line
    line_count = line_count + 1
print 'line count = ', line_count

fhandle = open('code/curl1.py','r')
content = fhandle.read()
print len(content)

fh = open('code/mbox.txt')
for line in fh:
    line = line.rstrip()
    if line.startswith('From)
        print line # print statment adds a new line automatically. 
for line in fh:
    line = line.rstrip()
    if not line.startswith('From') # if not 'From' in line 
        continue
    print line # print statment adds a new line automatically. 

# Assignment:
# 7.1 Write a program that prompts for a file name, then opens that file and 
# reads through the file, and print the contents of the file in upper case. 
# Use the file words.txt to produce the output below.
# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.strip().upper()
    print line
    
# Assignment
# 7.2 Write a program that prompts for a file name, then opens that file and 
# reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines 
# and compute the average of those values and produce an output as shown below.
# You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt 
# when you are testing below enter mbox-short.txt as the file name.
# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open('mbox-short.txt')
x = 0
ct = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        x = x + float(line[20:].rstrip())
        ct = ct + 1
        #print line 
        #print x
        #print ct
av = x / ct
print "Average spam confidence:", av
