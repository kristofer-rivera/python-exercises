# Question 1 - Conditional Basics
# A.

day = input("Enter the day: ")
if day.lower() == 'monday':
    print('Today is Monday!')
else:
    print('Today is not Monday.')

# B. 

day = input("Enter the day: ")
if day.lower() in('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'):
    print('Today is a weekday.')
else:
    print('Today is a weekend.')

# C.

hours_worked = 43
hourly_rate = 25

if hours_worked <= 40:
    paycheck = hours_worked * hourly_rate
    print(paycheck)
else:
    paycheck = (hours_worked - 40) * 1.5 * hourly_rate + (40 * hourly_rate)
    print(paycheck)

# Question 2 - Loop Basics 
# A. 

i = 5
while i <= 15:
    print(i)
    i += 1

i = 0
while i <= 100:
    print(i)
    i += 2

i = 100
while i >= -10:
    print(i)
    i -= 5

i = 2
while i <= 100_000_000:
    print(i)
    i **= 2

##
i = 100
while i >= 5:
    print(i)
    i -= 5

# B. 

number = int(input("Enter a number: "))
for i in range(1,11):
    print(str(number) + " x " + str(i) + " = " + str(i * number))

for n in range(1,10):
    print(str(n) * n)

# C. 

while True:
    number = input("Enter an odd number between 1 and 50: ")
    print("\n")
    
    if number.isdigit():
        if int(number) % 2 == 1 and int(number) < 50:
            break

print("Number to skip is: " + str(number))
print("\n")

for n in range(1, 50, 2):
    if n == int(number):
        print("Yikes! Skipping number: ", number)
        continue
    print("Here is an odd number: ", n)


# D. 

while True:
    pos_number = input("Enter a positive number: ")

    if pos_number.isdigit():
        if int(pos_number) > 0:
            break

for n in range(0, int(pos_number) + 1):
    print(n)

# E. 

while True:
    pos_int = input("Enter a positive interger: ")

    if pos_int.isdigit():
        if int(pos_int) > 0:
            break

for n in range(int(pos_int), 0, -1):
    print(n)


# Question 3 - Fizzbuzz

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)

# Question 4 - Table of Powers

powers_table = True

while powers_table:
    number = int(input("Enter an interger: "))
    print("\n")
    print("Here is your table!")
    print("\n")
    print("number | squared | cubed")
    print("------ | ------- | -----")
    for i in range(1,number+1):
        first = str(i)
        square = str(i ** 2)
        cube = str(i ** 3)
        print(first + " " * (7-len(first)) + "| ", end="")
        print(square + " " * (8-len(square)) + "| ", end="")
        print(cube)
    powers_table = input("Would you like to continue? (Y/N)") == "Y"


# Question 5 - Number grades into letter grades

grades = True

while grades:
    grade = input("Enter a numerical grade from 0 to 100: ")
    grade = int(grade)

    if grade >= 88:
        print("A")
    elif grade >= 80:
        print("B")
    elif grade >= 67:
        print("C")
    elif grade >= 60:
        print("D")
    else:
        print("F")
    grades = input(f'Would you like to enter another grade? ("Y/N"):') == "Y"

# Qestion 6 - List of dictionaries 

books = [{"title": "Outliers", "author": "Malcolm Gladwell", "genre": "Sociology"}, 
{"title": "Blink", "author": "Malcolm Gladwell", "genre": "Sociology"}, 
{"title": "How to Win Friends and Influence People", "author": "Dale Carnegie", "genre": "Sociology"},
{"title": "Dune", "author": "Frank Herbert", "genre": "Science Fiction"},
{"title": "Ender's Game", "author": "Orson Scott Card", "genre": "Science Fiction"},
{"title": "Sapiens", "author": "Yuval Noah Harari", "genre": "Science"}, 
{"title": "Dracula", "author": "Bram Stoker", "genre": "Classics"},
{"title": "The Count of Monte Cristo", "author": "Alexandre Dumas", "genre": "Classics"}]

for book in books:
    [print(key, ': ', book[key]) for key in book]
    print('------')
 
# Genre prompt

genre = input("Which Genre?: ")
for book in books:
    if book["genre"] == genre:
        print(book["title"])
   
# OR 
picked_genre = input('Please pick a genre and I will return the titles of that genre on shelf. \n')
matches = []
for book in books:
    if book['genre'].lower() == picked_genre.lower():
        matches.append(book['title'])
if matches == []:
    print('no books in that genre available. please check back later')
else:
    print(f'I have the following titles in the genre {picked_genre}')
    [print(match) for match in matches]

















