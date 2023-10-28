# what is the runtiem of the below code?
def foo(array):
    sum = 0 #O(1)
    product = 1 #O(1)
    for i in array: #O(N)
        sum += i #O(1)
    for i in array: #O(N)
        product *= i #O(1)
    print("Sum ="+str(sum)+", Product = "+str(product)) #O(1)
    #Tc = O(N)
    
# Ques 2 -> what is the runtime of the belw code?
def printPairs(array):
    for i in array:   #O(n)
        for j in array:  # (O(n(O(n)))
            print(str(i)+","+str(j))
            #Tc -> O(n*n)
            
#  Ques 3what is the runtime of the belw code?
def printunorderedPairs(array):
    for i in range(0, len(array)):   #O(n-1)
        for j in range(i+1, len(array)):  # (O(n(O(n-1)))
            print(array[i]+","+array[j])
            #Tc -> O(n*(n-1)/2)-> n^2/2-n/2

# Ques 4-> what is the runtime of the below code?
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i] < arrayB[j]:
                print(str(arrayA[i]) + "," + str(arrayB[j]))
            # TC -> O(ab)
    # Ques 5-> what is the runtime of the below code   
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            for k in range(0, 100000):
                print(str(arrayA[i]) + "," + str(arrayB[j]))
            # TC -> O(ab)

   # Ques 6-> what is the runtime of the below code  
def reverse(array):
    for i in range(0, int(len(array)/2)):#-> O(n/2)
        other = len(array)-i-1      #O(1)
        temp = array[i]        #O(1)
        array[i]= array[other] #O(1)
        array[other]=temp#O(1)
    print(array)  #O(1)
    # TC = O(N)
    
    