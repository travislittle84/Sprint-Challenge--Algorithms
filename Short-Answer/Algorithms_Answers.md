#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Reduces to O(n^3)

a = 0
    while (a < n * n * n):      O(n^3) - the while loop will grow exponentially by 3 powers
      a = a + n * n             O(1)   - operation will always take same amount of time no matter val of n
    
    

b)  Reduces to O(n^2) - the two O(n) operations reduce to O(n^2) - due to the nested while loop inside the for loop

sum = 0
    for i in range(n):          O(n)
      j = 1                     O(1)
      while j < n:              O(n)
        j *= 2                  O(1)
        sum += 1                O(1)

    

c)  Reduces to O(log n)

    def bunnyEars(bunnies):
        if bunnies == 0:                    O(1)
            return 0                        O(1)

        return 2 + bunnyEars(bunnies-1)     O(log n) - run time peaks at beginning but flattens as the function goes because of the -1

    

## Exercise II

Goal: find out which floor the eggs will start to break

Plan: 
    - Drop an egg on each floor 0 though n.
    - When an egg breaks, stop the loop and return the current floor number.

Big O Complexcity:
    - With this iterative solution, this function will be O(n)
    - A recursive bianary approach could be used, which would be O(log n) - if I have time
    I will come back and write out a recursive approach

function find_floor_where_eggs_break(n, f):                                     # O(n)

    floors = range(0, n) # array, each element representing a floor             # O(1)

    - helper function takes current floor and checks to see if it matches f (floor where eggs break)
    - if it matches, return true for egg breaking, return false for egg no breaking
    function drop_egg(floor):
        if floor == f: (f represents the floor where eggs drop)                 # O(1)
            return True # the egg broke                                         # O(1)
        else:
            return Flase # the egg did not break                                # O(1)

    for floor in floors:                                                        # O(n)
        if drop_egg(floor) == True: # dropped the egg and it broke              # O(1)
            return floor # return the floor where the egg broke and stop loop   # O(1)
        # egg did not break, to up to next floor and drop another egg.

    return -1 # If we get here then the eggs will never break                   # O(1)



