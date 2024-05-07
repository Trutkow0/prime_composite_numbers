# Timothy Rutkowski 04/25/2024 timothyRutkowski_lab7-2.py

# This program will get a positive number from the user and determine and display
# what numbers are prime and composite from 2 up to the number entered by the user.
# The program will exit when the user enters a negative number.

# Main function to get a positive number from the user, display prime/composite
# numbers from 2 to the entered number, and continue to loop until a negative
# number is entered
def main():
    while True:
        try:
            num = int(input('\nEnter a positive number (negative number to end): '))
            if num < 0:
                print('\nExiting program.')
                break
            for i in range(2, num + 1):
                display_prime_or_composite(i)
        except ValueError:
            print('Invalid input. Please enter a valid positive number or a ' +
                  'negative number to end.')

# Function to determine if a number is prime            
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Function to display whether a number is prime or composite
def display_prime_or_composite(num):
    if is_prime(num):
        print(f'{num}: Prime')
    else:
        print(f'{num}: Composite')

# Call the main function
if __name__ == "__main__":
    main()
