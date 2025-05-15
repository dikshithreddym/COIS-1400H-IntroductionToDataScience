# Name: Dikshith Reddy M
# Student Number : 0789055
# Date of Submission: 29th Jan, 2024

# Python code to explore the behavior of floating-point arithmetic errors over iterations
# and compare it with the precision of decimal arithmetic using the Decimal type from the decimal package.


# Part 2: Estimating the error
# Removed the print statement inside the loop and checked the behavior for 10, 100, and 1000 iterations
#OBSERVATIONS
#we observe that as the number of iterations increases, the cumulative error (difference between the calculated sum and the correct result) also increases. However, the rate of increase in error is not constant, and the error doesn't grow as fast as the number of iterations.
#Based on these observations, we can estimate the number of iterations needed for the error to be as large as the number added (0.1 in this case). The estimates for the required number of iterations are exceedingly large, indicating that it would take a significant number of iterations for the cumulative error to be as large as the number being added (0.1).


# Part 3: Estimating the scope of the problem
# Found two more numbers between 0 and 1 with incorrect results for 100 iterations
# Also found two numbers for which the result is correct
# Explanation: The discrepancies observed are due to the inherent limitations of floating-point arithmetic in computers, where not all decimal numbers can be represented accurately in binary.
#OBSERVATION
#The behavior of floating-point numbers and the discrepancies you observe when adding them repeatedly are rooted in how these numbers are represented and computed in computer systems. Floating-point numbers are represented in a format that can cover a vast range of values (from very small to very large) by storing a base number and an exponent. However, this format does not have the precision to represent all decimal numbers exactly.
#When you add a floating-point number repeatedly, the small errors in its representation can accumulate. The numbers for which you get correct results are likely those that can be represented more accurately in the binary system used by computers. For instance, numbers that are exact powers of 2 can be represented more precisely.



# Part 4: One potential solution
# Used the decimal package to perform the same operations with higher precision
# Checked the error behavior for 10, 100, and 1000 iterations using decimals
# Compared the results with Python's default floating datatype
# Explanation: The Decimal type from the decimal module provides a high level of precision and avoids the issues associated with binary floating-point representation. It's particularly useful for applications where precision is crucial.
#OBSERVATION
#Using the Decimal type for 10, 100, and 1000 iterations, we observe that the calculated sums are exactly equal to the correct results, with a difference of 0.0 in all cases. This indicates that there is no error accumulation over iterations when using Decimal, in stark contrast to the behavior observed with Python's default floating-point datatype.
#The reason for this discrepancy is rooted in the design and purpose of the decimal module. The Decimal type in the decimal module provides for more precise arithmetic and avoids many of the issues associated with binary floating-point arithmetic. 

from decimal import Decimal, getcontext

# Set the precision for Decimal operations
getcontext().prec = 28

# Function to find incorrect results for floating-point numbers
def find_incorrect_results(start, end, increment, iterations):
    incorrect_results = []
    
    for number in [start + i * increment for i in range(int((end - start) / increment) + 1)]:
        sum = 0
        toAdd = number
        
        for i in range(iterations):
            sum += toAdd
        
        difference = abs(sum - iterations * toAdd)
        
        if difference > 0:  # if there's any discrepancy
            incorrect_results.append({
                'number_added': toAdd,
                'iterations': iterations,
                'calculated_sum': sum,
                'correct_result': iterations * toAdd,
                'difference': difference
            })
            
            # Stop after finding two incorrect results
            if len(incorrect_results) == 2:
                break
    
    return incorrect_results

# Function to find incorrect results for decimal numbers
def find_incorrect_results_decimal(start, end, increment, iterations):
    incorrect_results_decimal = []
    
    for number in [start + i * increment for i in range(int((end - start) / increment) + 1)]:
        sum_decimal = Decimal('0')
        toAdd_decimal = Decimal(str(number))
        
        for i in range(iterations):
            sum_decimal += toAdd_decimal
        
        difference_decimal = abs(sum_decimal - Decimal(str(iterations)) * toAdd_decimal)
        
        if difference_decimal > 0:  # if there's any discrepancy
            incorrect_results_decimal.append({
                'number_added': toAdd_decimal,
                'iterations': iterations,
                'calculated_sum_decimal': sum_decimal,
                'correct_result_decimal': Decimal(str(iterations)) * toAdd_decimal,
                'difference_decimal': difference_decimal
            })
            
            # Stop after finding two incorrect results
            if len(incorrect_results_decimal) == 2:
                break
    
    return incorrect_results_decimal

# Function to check the behavior of the error using decimals
def check_error_behavior_decimal(iterations_list):
    results_decimal = []

    for iterations in iterations_list:
        sum_decimal = Decimal('0')
        toAdd_decimal = Decimal('0.1')
        
        for i in range(iterations):
            sum_decimal += toAdd_decimal
        
        difference_decimal = abs(sum_decimal - Decimal(str(iterations)) * toAdd_decimal)
        
        results_decimal.append({
            'iterations': iterations,
            'calculated_sum_decimal': sum_decimal,
            'correct_result_decimal': Decimal(str(iterations)) * toAdd_decimal,
            'difference_decimal': difference_decimal
        })

    return results_decimal



# Execute the functions to demonstrate the observations
incorrect_results = find_incorrect_results(0, 1, 0.01, 100)
incorrect_results_decimal = find_incorrect_results_decimal(0, 1, 0.01, 100)
error_behavior_decimal = check_error_behavior_decimal([10, 100, 1000])

# Output the results for review
print('Incorrect Results for Floating-Point:', incorrect_results)
print('Incorrect Results for Decimal:', incorrect_results_decimal)
print('Error Behavior for Decimal:', error_behavior_decimal)
