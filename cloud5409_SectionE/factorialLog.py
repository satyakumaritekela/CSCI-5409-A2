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

# function of factorial of a given number
def factOfN(n):
    factorial = 1
    if int(n) >= 1:
        for i in range (1, int(n) + 1):
            factorial = factorial * i
        return factorial
    
# open the text file and calculating the factorial of the respective numbers
with open('input.txt', 'r') as TextFile:
    for n in TextFile:
        # find the factorial of the number
        factorialOfN = factOfN(int(n))
        startTime = time.time()
        for i in range(int(n) * 7654):
            pass
        # append the request to the requestId list
        request = rand.randint(1, 100000)
        endTime = time.time()
        requestId.append(request)
        print(endTime - startTime)
        timeTaken.append(endTime - startTime)
        N.append(int(n))
        result.append(factorialOfN)
  
# creating columns       
data = {'request ID' : requestId, 'time' : timeTaken, 'N' : N, 'result' : result}

df = pd.DataFrame(list(zip(requestId,timeTaken,N,result)), columns = ['request ID','time', 'N', 'result'])

# loading data to csv
df.to_csv('FibonacciLog.csv', index = False)

df = pd.read_csv('FibonacciLog.csv')

#Generate a graph for time taken by tasks in factorial operation

df = pd.DataFrame(list(zip(df['N'].tolist(),df['time'].tolist())),columns=['N','Factorial Time'])

df.plot(kind='bar',x='N',y=['Factorial Time'])

plt.legend(loc='lower right')

plt.title('Factorial Time')
plt.xlabel('N value')

plt.ylabel('Time')

plt.show()