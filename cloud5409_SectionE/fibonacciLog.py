'''
Created on Feb. 26, 2020

@author: satya
'''
import pandas as pd
import random as rand
import time
import matplotlib.pyplot as plt

# creating lists for displaying log
requestId = []
timeTaken = []
N = []
result = []
nums = [] 

# function of a fibonacci for a given number
def fibOfN(n):
    if n < 0: 
        pass
    elif n == 0: 
        return 0
    elif n == 1: 
        return 1
    else: 
        return fibOfN(n-1)+fibOfN(n-2)
    
#read all the numbers from 
with open("input.txt") as file:
    for n in file:
        nums.append(int(n))

# open the text file and calculating the fibonacci of the respective numbers
with open('input.txt', 'r') as TextFile:
    i = 0
    for n in TextFile:
        r  = ''
        # finding the fibonacci of the respective number
        fibonacciOfN = fibOfN(int(n))
        startTime = time.time()
        for j in range(nums[i]):
            r = r + str(fibOfN(j))
            if nums[i]-1 != j:
                r  = r + ','
        for x in range(int(n) * 5786):
            pass
        # append the request to the requestId list
        request = rand.randint(1, 100000)
        endTime = time.time()
        requestId.append(request)
        print(endTime - startTime)
        timeTaken.append(endTime - startTime)
        N.append(int(n))
        result.append(r)
        i = i + 1
  
# creating columns      
data = {'request ID' : requestId, 'time' : timeTaken, 'N' : N, 'result' : result}

df = pd.DataFrame(list(zip(requestId,timeTaken,N,result)), columns = ['request ID','time', 'N', 'result'])

# loading data to csv
df.to_csv('FibonacciLog.csv', index = False)

df = pd.read_csv('FibonacciLog.csv')

#Generate a graph for time taken by tasks in fibonacci operation

df = pd.DataFrame(list(zip(df['N'].tolist(),df['time'].tolist())),columns=['N','Fibonacci Time'])

df.plot(kind='bar',x='N',y=['Fibonacci Time'])

plt.legend(loc='lower right')

plt.title('Fibonacci Time')

plt.xlabel('N value')

plt.ylabel('Time')

plt.show()


