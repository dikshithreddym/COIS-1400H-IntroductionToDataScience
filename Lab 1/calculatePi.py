# Name: Dikshith Reddy M
# Student Number : 0789055
# Date of Submission: 21st Jan, 2024

# Description : This code estimates the value of Pi using the Monte Carlo method.
#               It simulates random points within a unit square and determines the proportion that falls inside a quarter circle inscribed within the square.
#               By multiplying this proportion by 4, it approximates the value of Pi.
#               The accuracy of the estimation improves with the number of iterations (random points used).
#               The result, an estimated value of Pi, is printed to the console. The code also demonstrates the use of
#               basic Python constructs, including loops, conditional statements, and the random number generation.

# Observation: As the number of iterations (random points used) increases, the estimation of Pi generally becomes more accurate.
#              This is due to the Law of Large Numbers, which suggests that as a sample size grows, its mean gets closer to the average of the whole population.
#              However, increasing the number of iterations also increases the computational time.

import random  # Used for generating random numbers
import math  # Provides access to mathematical functions like sqrt()
import time  # Used for seeding the random number generator with the current time

inside = 0  # Counter for the number of points inside the quarter circle
outside = 0  # Counter for the number of points outside the quarter circle (within the square)
iterations = 1000000  # Number of random points to be generated

# Seeding the random number generator to ensure different results on each run
random.seed(int(round(time.time() * 1000)))

# Main loop for generating random points and determining if they are inside the quarter circle
for i in range(iterations):
    # select two random numbers between 0 and 1
    x = random.random()  # Random x-coordinate
    y = random.random()  # Random y-coordinate
    
    # calculate distance from origin (0,0) to the point (x,y)
    distance = math.sqrt(x**2 + y**2)  # Euclidean distance
   
    # increment the appropriate counter based on the position of the point
    if distance <= 1:  # Point is inside the quarter circle
        inside += 1
    else:  # Point is outside the quarter circle but inside the square
        outside += 1
    
# calculate the value of Pi 
# Ratio of points inside quarter circle to total points times 4 gives an estimate of Pi
pi_estimate = 4 * (inside / iterations)

# print result
# Display the estimated value of Pi
print(f"Estimated Value of Pi: {pi_estimate}")
