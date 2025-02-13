def is_palindrome(n):
    return str(n) == str(n)[::-1]

def file_check():
    try:
        
        print("Checking for numbers.txt...")
        if not os.path.exists("numbers.txt"):
            print("Error: numbers.txt not found.")
            return

        # This is to open and read the file also process the numbers as well as print the output if the number is palindrome or not
        print("Reading file...")
        with open("numbers.txt") as file:
            for i, line in enumerate(file, 1):
                nums = list(map(int, line.strip().split(',')))
                total = sum(nums)
                print(f"Line {i}: {', '.join(map(str, nums))}; sum = {total} - {'Palindrome' if is_palindrome(total) else 'Not a palindrome'}")
    except Exception as e:
        print("Error:", e)
        
file_check()
