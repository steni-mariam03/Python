# -*- coding: utf-8 -*-


# **Chapter 1 Exercises**

Exercise 1-1 (hello.py)
Use any editor (Notepad, vi, Nano, etc) or IDE to write a "Hello, world" python script named hello.py.
Run the script from the command line.
Open the script in your IDE and run it from there.
TIP In PyCharm, you can right-click (Ctrl-click on Mac) the script’s tab and select Run
"""

print("Hello, world")

"""Exercise 1-2 (spam.py)
Use PyCharm (or your favorite IDE) to create a script named spam.py that will output "SPAM SPAM
SPAM!". Run it from the IDE, and then run it from the command line.
"""

a="SPAM "
print(a*3)

"""# **Chapter 2 Exercises**

Exercise 2-1 (string_fun.py)
Start with the file string_fun.py, which is provided in the top folder of the student files. The variable
name is set to "john jacob jingleheimer schmidt". Using that variable,
• Print name as-is
• Print name in upper case
• Print name in title case
• Print number of occurrences of 'j' in name
• Print length of name
• Print position (offset) of "jacob" in name
"""

name = "john jacob jingleheimer schmidt"
print("Name :", name)
print("Upper case:", name.upper())
print("Title case:", name.title())
print("Number of 'j's:", name.count('j'))
print("Length of name:", len(name))
print("Position of 'jacob':", name.find('jacob'))

"""# **Chapter 3 Exercises**

Exercise 3-1 (c2f.py)
Write a Celsius to Fahrenheit converter. Your script should prompt the user for a Celsius temperature,
the print out the Fahrenheit equivalent.
What the user types:
python c2f.py
(or run from PyCharm/Spyder etc)
The program prompts the user, and the user enters the temperature to be converted.
The formula is F = ((9 * C) / 5 ) + 32. Be sure to convert the user-entered value into a float.
Test your script with the following values: 100, 0, 37, -40
"""

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = ((9 * celsius) / 5) + 32
print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit.")

"""Exercise 3-2 (c2f_batch.py)
Create another C to F converter. This time, your script should take the Celsius temperature from the
command line and output the Fahrenheit value. What you will type:
python c2f_batch.py 100
(or run from PyCharm/Spyder etc)
Test with the values from c2f.py.
These two programs should be identical, except for the input.
"""

import sys

def c2f_cmd(argv=None):
    argv = sys.argv if argv is None else argv
    if len(argv) < 2:
        print("Usage: c2f_batch.py <Celsius>")
        return
    c = float(argv[1])
    print(((9 * c) / 5) + 32)

c2f_cmd(["c2f_batch.py", "32"])

"""# **Chapter 4 Exercises**

Exercise 4-1 (c2f_loop.py)
Redo c2f.py to repeatedly prompt the user for a Celsius temperature to convert to Fahrenheit and then
print. If the user just presses Return, go back to the top of the loop. Quit when the user enters "q".
TIP Read in the temperature, test for "q" or "", and only then convert the temperature to a
float.
"""

while True:
    temp = input("Enter temperature in Celsius: ")
    if temp.lower() == 'q':
        print("Exiting the converter.")
        break
    elif temp == '':
        continue
    celsius = float(temp)
    fahrenheit = ((9 * celsius) / 5) + 32
    print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit.")

"""Exercise 4-2 (guess.py)
Write a guessing game program. You will think of a number from 1 to 25, and the computer will guess
until it figures out the number. Each time, the computer will ask "Is this your number? "; You will enter
"l" for too low, "h" for too high, or "y" when the computer has got it. Print appropriate prompts and
responses.
TIP
1. Start with max_val = 26 and min_val = 0
2. guess is always (max_val + min_val)//2 Note integer division operator
3. If current guess is too high, next guess should be halfway between lowest and current
guess, and we know that the number is less than guess, so set max_val = guess
4. If current guess is too low, next guess should be halfway between current and
maximum, and we know that the number is more than guess, so set min_val = guess
TIP If you need more help, see next page for pseudocode. When you get it working for 1 to 25,
try it for 1 to 1,000,000. (Set max_value to 1000001).
Bonus Exercise (guessx.py)
Get the maximum number from the command line or prompt the user to input the maximum, or both
(if no value on command lines then prompt)

Pseudocode for guess.py
MAXVAL=26
MINVAL=0
while TRUE
GUESS = int((MAXVAL + MINVAL)//2)
prompt "Is your guess GUESS? "
read ANSWER
if ANSWER is "y"
PRINT "I got it!"
EXIT LOOP
if ANSWER is "h"
MAXVAL=GUESS
if ANSWER is "l"
MINVAL=GUESS
"""

max_val = 26
min_val = 0

while True:
    guess = (max_val + min_val) // 2
    answer = input(f"Is this your number? {guess} (enter 'l' for too low, 'h' for too high, 'y' for yes): ")

    if answer.lower() == 'y':
        print("I got it!")
        break
    elif answer.lower() == 'h':
        max_val = guess
    elif answer.lower() == 'l':
        min_val = guess
    else:
        print("Please enter 'l', 'h', or 'y'.")

"""# **Chapter 5 Exercises**

Exercise 5-1 (pow2.py)
Print out all the powers of 2 from 0 through 31.
Use the ** operator, which raises a number to a power.
"""

for i in range(0, 32):
    print(f"2^{i} = {2**i}")

"""Exercise 5-2 (sequences.py)
ctemps is a list of Celsius temperatures. Loop through ctemps, convert each temperature to Fahrenheit,
and print out both temperatures
"""

file_path = "/content/sequences.txt"
ctemps = []
current_list = None

with open(file_path, 'r') as f:
    for line in f:
        line = line.strip()
        if line == '':
            continue
        if line.startswith('# ctemps'):
            current_list = 'ctemps'
            continue
        elif line.startswith('# fruits'):
            current_list = None
            continue
        if current_list == 'ctemps':
            ctemps.append(int(line))

print("Celsius to Fahrenheit:")
for c in ctemps:
    f_temp = ((9 * c) / 5) + 32
    print(f"{c} Celsius = {f_temp} Fahrenheit")

"""Exercise 5-3 (sequences.py)
Use a list comprehension to copy the list fruits to a new list named clean_fruits, with all fruits in
lower case and leading/trailing white space removed. Print out the new list.
HINT: Use chained methods (x.spam().ham())
"""

file_path = "/content/sequences.txt"
fruits = []
current_list = None

with open(file_path, 'r') as f:
    for line in f:
        line = line.strip()
        if line == '':
            continue
        if line.startswith('# fruits'):
            current_list = 'fruits'
            continue
        elif line.startswith('# ctemps'):
            current_list = None
            continue
        if current_list == 'fruits':
            fruits.append(line)

clean_fruits = [x.strip().lower() for x in fruits]
print(clean_fruits)

"""Exercise 5-4 (sieve.py)
FOR ADVANCED STUDENTS
The "Sieve of Eratosthenes" is an ancient algorithm for finding prime numbers. It works by starting at
2 and checking each number up to a specified limit. If the number has been marked as non-prime, it is
skipped. Otherwise, it is prime, so it is output, and all its multiples are marked as non-prime.
Write a program to implement this algorithm. Specify the limit (the highest number to check) on the
script’s command line. Supply a default if no limit is specified.
Initialize a list (maybe named is_prime) to the size of the limit plus one (use * to multiply a single-item
list). All elements should be set to True.
Use two nested loops.
The outer loop will check each value (element of the array) from 2 to the upper limit. (use the range())
function.
If the element has a True value (is prime), print out its value. Then, execute a second loop iterates
through all the multiples of the number, and marks them as False (i.e., non-prime).
No action is needed if the value is False. This will skip the non-prime numbers.
TIP Use range() to generate the multiples of the current number.
NOTE In this exercise, the value of the element is either True or False — the index is the
number be checked for primeness.
See next page for the pseudocode for this program:

Pseudocode for sieve.py
if # command line args == 1
get LIMIT from command line
else
set LIMIT to 50
Initialize IS_PRIMES list to size LIMIT+1, with all TRUE values
for NUM from 2 to LIMIT+1
if IS_PRIME[NUM]
output NUM
for M from NUM to LIMIT+1, counting by NUM
IS_PRIME[M] = FALSE
"""

import sys

if len(sys.argv) > 1 and sys.argv[1].isdigit():
    limit = int(sys.argv[20])
else:
    limit = 50

is_prime = [True] * (limit + 1)

for n in range(2, limit + 1):
    if is_prime[n]:
        print(n)
        for m in range(n * 2, limit + 1, n):
            is_prime[m] = False

"""# **Chapter 6 Exercises**

Exercise 6-1 (line_no.py)
Write a program to display each line of a file preceded by the line number. Allow your program to process one or more files specified on the command line. Be sure to reset the line number for each file.
TIP Use enumerate().
Test with the following commands:
python line_no.py DATA/tyger.txt
python line_no.py DATA/parrot.txt DATA/tyger.txt
Test with other files, as desired
"""

file_paths = [
    "/content/alt.txt",
    "/content/bob.txt"
]

for filename in file_paths:
    print(f"\nProcessing file: {filename}")
    with open(filename, 'r') as file:
        for lineno, line in enumerate(file, start=0):
            print(f"{lineno}: {line.rstrip()}")

"""Exercise 6-2 (alt_lines.py)
Write a program to create two files, a.txt and b.txt from the file alt.txt. Lines that start with 'a' go in
a.txt; the other lines (which all start with 'b') go in b.txt. Compare the original to the two new files.
"""

file_path = "/content/alt.txt"
file_path1 = "/content/a.txt"
file_path2 = "/content/b.txt"
with open(file_path, 'r') as infile:
    with open(file_path1, 'w') as a_file, open(file_path2, 'w') as b_file:
        for line in infile:
            line = line.strip()
            if line.startswith('a') or line.startswith('A'):
                a_file.write(line + '\n')
            elif line.startswith('b') or line.startswith('B'):
                b_file.write(line + '\n')

print("Contents of alt.txt:")
with open(file_path, 'r') as file:
    print(file.read())

print("\nContents of a.txt:")
with open(file_path1, 'r') as file:
    print(file.read())

print("\nContents of b.txt:")
with open(file_path2, 'r') as file:
    print(file.read())

"""Exercise 6-3 (count_alice.py, count_words.py)
A. Write a program to count how many lines of alice.txt contain the word "Alice". (There should be
392).
TIP Use the in operator to test whether a line contains the word "Alice"

"""

file_path = "/content/alice.txt"
with open(file_path, 'r') as file:
    count = 0
    for line in file:
        if 'Alice' in line:
            count += 1

print(f'The word "Alice" appears in {count} lines.')

"""B. Modify count_alice.py to take the first command line parameter as a word to find, and the
remaining parameters as filenames. For each file, print out the file name and the number of lines
that contain the specified word. Test thoroughly
FOR ADVANCED STUDENTS (icount_words.py) Modify count_words.py to make the search case-
insensitive
"""

search_word = input("Enter the word to search for: ").strip().lower()

file_paths = [
    "/content/alice.txt",
    "/content/bob.txt"
]

for filename in file_paths:
    with open(filename, 'r') as file:
        count = 0
        for line in file:
            if search_word in line.lower():
                count += 1
    print(f"{filename}: {count} lines contain the word '{search_word}'")

"""# **Chapter 7 Exercises**

Exercise 7-1 (file_date.py)
Write a script which accepts one or more filenames on the command line, and prints out each file
name with its date of last modification in the format 'Mar 12, 2013'.
"""

import os
from datetime import datetime

file_paths = [
    "/content/alice.txt",
    "/content/fruit2.txt",
    "/content/sample_data"
]

for filename in file_paths:
    mod_time = os.path.getmtime(filename)
    dt = datetime.fromtimestamp(mod_time)
    formatted_date = dt.strftime('%b %d, %Y')
    print(f"{filename}: {formatted_date}")

"""Exercise 7-2 (get_file_size.py)
Write a script that accepts one or more files on the command line, and prints out the size, one file per
line. If any argument is a directory, print out a warning message.

"""

import os

file_paths = [
    "/content/alice.txt",
    "/content/alt.txt",
    "/bin"
]

for filename in file_paths:
    if os.path.isdir(filename):
        print(f"Warning: {filename} is a directory")
    elif os.path.isfile(filename):
        size = os.path.getsize(filename)
        print(f"{filename}: {size} bytes")
    else:
        print(f"Error: {filename} not found")

"""Exercise 7-3 (for_usage.py)
Write a script to count how many times a for loop is used in all .py files under py3intro (the top folder
of the student files).


"""

import os

base_dir = '/content/sample_data/Fiserv'

total_for_count = 0

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.py'):
            file_path = os.path.join(root, file)
            file_for_count = 0
            with open(file_path, 'r') as f:
                for line in f:
                    line_strip = line.strip()
                    if line_strip.startswith('for '):
                        file_for_count += 1
                        total_for_count += 1
            print(f"{file_path}: {file_for_count} 'for' loops")

print(f"\nTotal 'for' loops found: {total_for_count}")

"""Exercise 7-4 (copy_pfiles.py)
Write a script to copy all files that start with 'p' from the DATA folder into the TEMP folder.
TIP use shutil


"""

import os
import shutil

source_dir = '/content/sample_data/Fiserv'
dest_dir = '/content/TEMP'

os.makedirs(dest_dir, exist_ok=True)

for filename in os.listdir(source_dir):
    src_file = os.path.join(source_dir, filename)
    dst_file = os.path.join(dest_dir, filename)
    if os.path.isfile(src_file) and filename.lower().startswith('p'):
        shutil.copy2(src_file, dst_file)
        print(f"Copied {filename} to TEMP")

"""# **Chapter 8 Exercises**

Exercise 8-1 (scores.py)
A class of students has taken a test. Their scores have been stored in testscores.dat. Write a program
named scores.py to read in the data (read it into a dictionary where the keys are the student names
and the values are the test scores). Print out the student names, one per line, sorted, and with the
numeric score and letter grade. After printing all the scores, print the average score.
TIP Be sure to convert the numeric score to an integer when storing it in the dictionary.
Table 20. Grading Scale
95-100 A
89-94 B
83-88 C
75-82 D
< 75 F
"""

def get_grade(score):
    if score >= 95:
        return 'A'
    elif score >= 89:
        return 'B'
    elif score >= 83:
        return 'C'
    elif score >= 75:
        return 'D'
    else:
        return 'F'

scores = {}

file_path = "/content/testscores.dat.txt"
with open(file_path, 'r') as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) == 2:
            name, score = parts
            scores[name] = int(score)

print("Name\tScore\tGrade")
for name in sorted(scores.keys()):
    score = scores[name]
    grade = get_grade(score)
    print(f"{name}\t{score}\t{grade}")

avg_score = sum(scores.values()) / len(scores)
print(f"\nAverage Score: {avg_score:.2f}")

"""Exercise 8-2 (shell_users.py)
Using the file named passwd, write a program to count the number of users using each shell. To do
this, read passwd one line at a time. Split each line into its seven (colon-delimited) fields. The shell is
the last field. For each entry, add one to the dictionary element whose key is the shell.
When finished reading the password file, loop through the keys of the dictionary, printing out the shell
and the count.

"""

file_path = "/content/passwd.txt"
shell_count = {}
with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        fields = line.split(':')
        if len(fields) < 7:
            continue
        shell = fields[-1]
        shell_count[shell] = shell_count.get(shell, 0) + 1

for shell, count in shell_count.items():
    print(f"{shell}: {count}")

"""Exercise 8-3 (common_fruit.py)
Using sets, compute which fruits are in both fruit1.txt and fruit2.txt. To do this, read the files into sets
(the files contain one fruit per line) and find the intersection of the sets.
What if fruits are in both files, but one is capitalized and the other isn’t?

"""

def read_fruits(filename):
    with open(filename, 'r') as f:
        return set(line.strip().lower() for line in f)

fruits1 = read_fruits('fruit1.txt')
fruits2 = read_fruits('fruit2.txt')

common_fruits = fruits1 & fruits2

print("Fruits in both files:")
for fruit in sorted(common_fruits):
    print(fruit)

"""Exercise 8-4 (set_sieve.py)
FOR ADVANCED STUDENTS Rewrite sieve.py to use a set rather than a list to keep track of which
numbers are non-prime. This turns out to be easier – you don’t have to initialize the set, as you did
with the list

"""

limit = 50
non_primes = set()
primes = []

for num in range(2, limit + 1):
    if num not in non_primes:
        primes.append(num)
        for multiple in range(num * 2, limit + 1, num):
            non_primes.add(multiple)

print("Primes up to", limit, ":")
print(primes)

"""# **Chapter 9 Exercises**

Exercise 9-1 (dirty_strings.py)
Using the existing script dirty_strings.py, implement the function named cleanup(). This function
accepts one string as input and returns a copy of the string with whitespace removed from the
beginning and the end, and all upper case letters changed to lower case.
The code to loop over a list of "dirty" strings and call the function is already in place. All you have to do
is remove the pass statement and put your code in the cleanup() function.
"""

def cleanup(s):
    cleaned = s.strip().lower()
    return cleaned

dirty_list = [" Apple ", " BANANA", "  Cherry  ", "MANGO  ", "  Guava"]

print("Cleaned strings:")
for item in dirty_list:
    result = cleanup(item)
    print(result)

"""Exercise 9-2 (c2f_func.py)
Define a function named c2f() that takes one number as a parameter, and then returns the value
converted from Celsius to Fahrenheit. Test your function by calling it with the values 100, 0, 37, and -40
one at a time.
Example
f = c2f(100)
print(f)
f = c2f(-40)
print(f)
"""

def c2f(c):
    return ((9 * c) / 5) + 32

print(c2f(100))
print(c2f(0))
print(c2f(37))
print(c2f(-40))

"""Exercise 9-3 (calc.py)
Write a simple four-function calculator. Repeatedly prompt the user for a math expression, which
should consist of a number, an operator, and another number, all separated by whitespace. The
operator may be any of "+","-", "/", or "*". For example, the user may enter "9 + 5", "4 / 28", or "12 * 5".
Exit the program when the user enters "Q" or "q". (Hint: split the input into the 3 parts – first value,
operator, second value).
Write a function for each operator (named "add", "subtract", etc). As each line is read, pass the two
numbers to the appropriate function, based on the operator, and get the result, which is then output to
the screen. The division function should check to see whether the second number is zero, and if so,
return an error message, rather than trying to actually do the math.
NOTE Expect an expression like "5 + 4" which you can split on whitespace
FOR ADVANCED STUDENTS
Add more math operations; test the input to make sure it’s numeric (although in real life you
should use a try block to validate numeric conversions).
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

while True:
    expr = input("Enter an expression (or 'q' to quit): ").strip()
    if expr.lower() == 'q':
        break

    parts = expr.split()
    if len(parts) != 3:
        print("Invalid format. Use: number operator number")
        continue

    a, op, b = parts

    if not (a.replace('.', '', 1).isdigit() and b.replace('.', '', 1).isdigit()):
        print("Please enter valid numbers.")
        continue

    a = float(a)
    b = float(b)

    if op == '+':
        result = add(a, b)
    elif op == '-':
        result = subtract(a, b)
    elif op == '*':
        result = multiply(a, b)
    elif op == '/':
        result = divide(a, b)
    else:
        result = "Invalid operator. Use +, -, *, or /."

    print("Result:", result)