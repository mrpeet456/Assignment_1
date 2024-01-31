def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def compute_factorials(numbers):
    return [factorial(num) for num in numbers]

def main():
    try:
        
        input_numbers = [int(x) for x in input("Enter comma-separated numbers: ").split(',')]
        
        
        factorials = compute_factorials(input_numbers)
        
        print("Factorials:", ', '.join(map(str, factorials)))

    except ValueError:
        print("Invalid input. Please enter valid integers separated by commas.")

if __name__ == "__main__":
    main()
