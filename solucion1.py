#We can know how many possible combinations of ways to climb up a stair of n
#steps there is by using the Fibonacci Sequence

#The Fibonacci Sequence is the series of numbers where
#the next number is found by adding up the two numbers before it:

def climbStairs(n):
  if (n < 3):       #If the number is below 3 then the number of ways to climb up
                    #the stair is the same as the number of steps 
    return n
  first = 1         #Else we start on the first two steps (1+2)
  second = 2
  for i in range(2, n):     #And we keep iterating, adding the next step to
                            #the result (1+2)+3,(2+3)+4,(3+4)+5...etc
    current = first + second
    first = second
    second = current
    
  return second


result=climbStairs(10)
print("The possible number of ways to climb up the stair is: " + str(result))

