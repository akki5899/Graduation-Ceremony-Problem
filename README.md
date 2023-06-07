# Graduation-Ceremony-Problem
***  
## Question : 
              In a university, your attendance determines whether you will be
              allowed to attend your graduation ceremony.
              You are not allowed to miss classes for four or more consecutive days.
              Your graduation ceremony is on the last day of the academic year,
              which is the Nth day.

                Your task is to determine the following:

              1. The number of ways to attend classes over N days.
              2. The probability that you will miss your graduation ceremony.

              Represent the solution in the string format as "Answer of (2) / Answer
              of (1)", don't actually divide or reduce the fraction to decimal
              
              Test Case:
              1. for 5 days: 14/29
              2. for 10 days: 372/773

***  
## Algorithm
  1. Define the class Solution with the constructor __init__ that takes two parameters: __total_numbers_of_days__ and __consecutive_days__.
  2. Check if the input values are valid. If total_numbers_of_days is less than consecutive_days or either value is negative, raise a ValueError with the message "Inputs are invalid."
  3. The graduation_probability method calculates the graduation probability using dynamic programming. It creates a 2D matrix called probability_matrix to store the probabilities
  4. The first loop sets the initial values in the first row of the matrix. Since we cannot miss any classes on the first day, the values are set to 1 for the first consecutive_days columns.
  5. The nested loop iterates through the remaining rows of the matrix, starting from the second row. It calculates the values for each cell based on the previous row's values. The value at __probability_matrix[i][j]__ represents the number of ways to attend classes up to day __i__ without missing __j__ consecutive classes.
  6. The __valid_way_to_attend_class__ variable stores the number of ways to attend all __total_numbers_of_days__ without missing consecutive_days or more classes consecutively. It is obtained from __probability_matrix[self.total_numbers_of_days][0]__, which represents the number of ways to attend all classes without missing any.
  7. The __number_of_way_to_miss_class__ variable stores the number of ways to attend __total_numbers_of_days - 1__ without missing the first class and missing exactly one class somewhere in between. It is obtained from __probability_matrix[self.total_numbers_of_days - 1][1]__.
  8. The output method prints the values of total_numbers_of_days and consecutive_days and then calls the graduation_probability method to calculate and print the graduation probability.

***  
## Usage
1. Run the program in Python.
2. Enter the total number of ways to attend the class when prompted.
3. The program will calculate and display the graduation probability based on the given inputs.

Please note that the input values must be valid. The total number of days must be greater than or equal to the consecutive days, and both values must be non-negative.

