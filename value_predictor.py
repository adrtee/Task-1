#define list
numbers = [] 

#define functions
#this is the function to obtain input
def inputNum():
    count = 0

    #For the first six entries
    while count < 6:
        #check whether the entry is integer
        try:
            entry=int(input())
            integer = 1
                      
        except:
            integer = 0
            print ("please enter integer only")

        #check whether the entry is greater or equal to the previous one    
        if integer == 1:
            if count == 0:
                numbers.append(entry)
                count = count + 1
            elif entry >= numbers[count-1] and count > 0:
                numbers.append(entry)
                count = count + 1
            else:
                print("Please enter integer greater or equal to the previous entry")

    #Additional entries
    print ("Continue entering increasing integers or enter any alphabet to calculate")
    while count >= 6:
        #check whether the entry is integer
        try: 
            entry=int(input())
            integer = 1
            
        except:
            integer = 0
            if (count % 2) == 0:
                return numbers   
            else:
                print ("The total entry must be a even number, the number of entries is ", count,". Please enter at least 1 more integer") 

        #check whether the entry is greater or equal to the previous one
        if integer == 1:
            if entry >= numbers[count-1]:
                numbers.append(entry)
                count = count + 1
            else:
                print("Please enter integer greater or equal to the previous entry")

#this is the function of calculating average of the two entries in the center of the list      
def findCenter(numbers, l):  
    sum = numbers[int(l/2)-1] + numbers[int(l/2)]
    return float(sum/2)

#main code
print("Enter at least 6 increasing integers and the total entries must be an even number")
numbers = inputNum()
l = len(numbers)
print(numbers)
print("Center =", findCenter(numbers, l))



