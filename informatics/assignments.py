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


## Week 8
# Lecture
x = 2
x = 4
print x
print [1,24,76]
print ['red','yellow','blue']
print ['red',24,43.2]
print [1,[3,4],32]
print []
fruit = 'Banana'
fruit[0] = 'b'
print fruit
x = fruit.lower()
lotto = [1,2,3,5,9]
lotto[2] = 34
friends = ['Jose','Glenn','Sally']
print len(friends)
print range(len(friends))
for friend in friends:
    print 'happy', friend
for i in range(len(friends)):
    friend = friends[i]
    print 'happy', friend
a = [1,2,3]
b = [4,5,6]
c = a + b
print c
t = [2,23,34,56,67]
t[1:3]
x = list()
type(x)
dir(x)

stuff = list()
stuff.append('book')
stuff.append(99)
print stuff
2 in t
3 not in t
friends.sort()
print friends
print len(t)
print max(t)
print min(t)
print sum(t)
print sum(t)/len(t)

total = 0 
count = 0
while True:
    inp = raw_input('Enter a number:')
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count + 1

average = total / count
print 'Average:', average

numlist = list()
while True:
    inp = raw_input('Enter a number:')
    if inp == 'done':break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print 'Average:', average

abc = 'With three wods'
stuff = abc.split()
print stuff
print len(stuff)
print stuff[0]
for w in stuff:
    print w
    
line = 'A lot          of spaces'
etc = line.split()
print etc
line = 'first;second;third'
thing = line.split()
print thing
print len(thing)
thing = line.split(';')
print thing
print len(thing)

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):continue
    words = line.split()
    print words[2]
    email = words[1]
    pieces = email.split('@')
    url = pieces[1]
    print url


# Assignment 8.4
# 8.4 Open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words using the split() function. 
# The program should build a list of words. For each word on each line check to 
# see if the word is already in the list and if not append it to the list. 
# When the program completes, sort and print the resulting words in alphabetical order.
# You can download the sample data at http://www.pythonlearn.com/code/romeo.txt
fname = raw_input("Enter file name: ")
fh = open('romeo.txt')
lst = list()
for line in fh:
    words = line.split()
    for word in words:
        if word in lst:continue
        lst.append(word)
lst.sort()
print lst
#print line.rstrip()

# Assignment 8.5
# 8.5 Open the file mbox-short.txt and read it line by line. When you find a line 
# that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the 
# line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.
# You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    if line.startswith('From '):
        words = line.split()
        print words[1]
        count = count + 1
print "There were", count, "lines in the file with From as the first word"


## Week 9
# Lecture: dictionaries
purse = dict()
purse['money'] = 12
purse['candy'] = 3
print purse
print purse['candy']
purse['candy'] = purse['candy'] + 2
print purse

lst = list()
lst.append(21)
lst.append(123)
print lst
lst[0] = 23
print lst

ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print ddd
ddd['age'] = 23
print ddd

jjj = {'chuck':1, 'fred':42, 'jan':100} # no order
print jjj
ooo = {}
print ooo

ccc = dict()
print ccc['csev']

print 'csev' in ccc

counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print counts

if name in counts:
    print counts[name]
else:
    print 0
    
print counts.get(name,0)

counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
    counts[name] = counts.get(name,0) + 1
print counts

counts = dict()
print 'Enter a line of text:'
line = raw_input('')
words = line.split()
print 'Words:',words
print 'Counting...'
for word in words:
    counts[word] = counts.get(word,0) + 1
print 'Counts',counts
for key in counts:
    print key, counts[key]
print list(counts)
print counts.keys()
print counts.values()
print counts.items()
for aaa,bbb in counts.items():
    print aaa,bbb

import os
os.getcwd()
os.chdir('/home/victor/Projects/TreeBoa/informatics/')
#name = raw_input("Enter file:")
#handle = open(name,'r')
handle = open('mbox-short.txt','r')
text = handle.read()
words = text.split()
counts = dict()
for word in words:
    counts[word] = counts.get(word,0) + 1 
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print bigword,bigcount

# 9.4 Write a program to read through the mbox-short.txt and figure out who 
# has the sent the greatest number of mail messages. The program looks for 
# 'From ' lines and takes the second word of those lines as the person who sent 
# the mail. The program creates a Python dictionary that maps the sender's mail 
# address to a count of the number of times they appear in the file. After the 
# dictionary is produced, the program reads through the dictionary using a 
# maximum loop to find the most prolific committer.
name = 'mbox-short.txt'
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        word = words[1]
        print word
        counts[word] = counts.get(word,0) + 1 

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print bigword,bigcount


## Week 10
# Lecture tuples (like lists but with paramphasis rather than square brackets)
l  = list()
dir(l)
t = tuple()
dir(t)
(x, y) = (4, 'fred')
print y
(a, b) = (99, 98)
print a
a, b = (99, 98)
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
    print k, v
tups = d.items()
print tups
(0, 1, 3434) < (0, 3, 4)

d = {'a':10, 'b':1, 'c':22}
t = d.items()
t
t.sort()
t
t = sorted(d.items())
t
for k, v in sorted(d.items()):
    print k, v
    
tmp = list()
for k,v in d.items():
    tmp.append((v,k))
print tmp
tmp.sort(reverse=True)
print tmp
print sorted([(v,k) for k,v in d.items()])

fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
lst = list()
for k,v in counts.items():
    lst.append((v,k))
lst.sort(reverse=True)
for v,k in lst[:10]:
    print k,v

# 10.2 Write a program to read through the mbox-short.txt and figure out the 
# distribution by hour of the day for each of the messages. You can pull the hour 
# out from the 'From ' line by finding the time and then splitting the string 
# a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, 
# sorted by hour as shown below. Note that the autograder does not have support 
# for the sorted() function.
#name = raw_input("Enter file:")
name = 'mbox-short.txt'
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split(':')
        word = words[0][len(words[0])-2:len(words[0])]
        counts[word] = counts.get(word,0) + 1
lst = counts.items()
lst.sort()
for k,v in lst:
    print k,v