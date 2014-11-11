# week 1
print("Dr. Chuck rocks! 23165423134546")

# week 5
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