#several ways: Exhaustive, Bisection, Newton-Raphson

#newton-raphson guess and check method

epsilon = 0.000001
y = 25

guess = y/2.0

while abs(guess*guess - y) >= epsilon:
    #print((guess**2)-y)
    guess = guess - (((guess**2) -y)/(2*guess))
    print((guess**2)-y)
    
    
print("Square root of " + str(y) + "is about " + str(guess))
      
