# Question 1 

def is_two(n):
    if n == 2 or n == '2':
        return True 
    else: 
        return False 

is_two('2')
is_two(2)
is_two(4)
is_two('8')

# Question 2 

def is_vowel(x):
    if x.lower() in('a', 'e', 'i', 'o', 'u'):
        return True 
    else: 
        return False

# OR Class solution

def is_vowel(x):
    if type(x) == str:
        result = x.lower() in ['a', 'e', 'i', 'o', 'u']
        return result
    else: 
        return False

is_vowel('a')
is_vowel('E')
is_vowel('o')
is_vowel('8')
is_vowel('t')

# Question 3 

def is_consonant(x):
    if x.isdigit() or is_vowel(x):
        return False
    else:
        return True 

# OR Class solution

def is_consonant(x):
    if type(x) == str:
        only_letters = x.isalpha()
        return only_letters and not is_vowel(x)
    return False

is_consonant('x')
is_consonant('T')
is_consonant('9')
is_consonant('a')
is_consonant('p')
is_consonant('u')

# Question 4 

def capitalize_word(str):
    if is_consonant(str[0]):
        return str.capitalize()
    else: 
        return str


capitalize_word('upper')
capitalize_word('tonsil')
capitalize_word('red')
capitalize_word('apple')

# Or Class Solution

def cap_start_consonant(string):
    if type(string) != str:
        return False
    first_letter = string[0]
    if is_consonant(first_letter):
        string = string.capitalize()
    return string

cap_start_consonant('upper')
cap_start_consonant('tonsil')
cap_start_consonant('red')
cap_start_consonant('apple')

# Question 5

# if you want percent input to be a decimal

def calculate_tip(percent, total):
    return percent * total

calculate_tip(.19, 34.50)
calculate_tip(.20, 100)
calculate_tip(.21, 76)

#OR if you want percent input to be an interger

def calculate_tip(percent, total):
    return (percent/100) * total

calculate_tip(19, 34.50)
calculate_tip(20, 100)
calculate_tip(21, 76)

#OR Class solution

def calculate_tip(bill, tip_percentage=0.2):
    if tip_percentage < 0 or tip_percentage > 1:
        return 'the tip percentage must be between 0 and 1'
    tip_amount = tip_percentage * bill
    return tip_amount

calculate_tip(34.50, .19)
calculate_tip(100, .30)
calculate_tip(76, 21)

# Question 6 
# Uses my calcuate_tip solution 
def apply_discount(price, discount):
    return price - calculate_tip(discount, price)

apply_discount(100, .20)
apply_discount(50, .50)
apply_discount(1000, .10)

# Or class solution

def apply_discount(price, discount_percentage):
    discount = price * discount_percentage
    return price - discount 

apply_discount(20, .5)

# Question 7 

def handle_commas(x):
    return int(x.replace(',', ''))

handle_commas('1,000,500')
handle_commas('500,789,234')
handle_commas('78,000')

# Question 8 

def get_letter_grade(grade):
    if 90 <= grade <= 100:
        return "A"
    elif 80 <= grade <= 89:
        return "B"
    elif 70 <= grade <= 79:
        return "C"
    elif 60 <= grade <= 69:
        return "D"
    else:
        return "F"

get_letter_grade(76)
get_letter_grade(91)
get_letter_grade(56)

# Question 9

def remove_vowels(somestring):
    if type(somestring) != str:
        return False
    output = ''
    for letter in somestring:
        if is_consonant(letter):
            output += letter
    return output

remove_vowels('hunger')
remove_vowels('angry')
remove_vowels('helicopter')

# Question 10

def remove_special_characters(str):
    return ''.join([x for x in str if x.isidentifier() or x == ' '])
def normalize_name(str):
    return remove_special_characters(str).lower().strip().replace(' ', '_')


normalize_name('First Name')
normalize_name('% Completed')
normalize_name('&# Hello There Innis')

# Class solution

def normalize_name(string):
    output = ''
    string = string.lower()
    for character in string:
        if character.isidentifier() or character == ' ':
            output += character 
    output = output.strip()
    output = output.replace(' ', '_')
    return output 


# Question 11 

def cumulative_sum(str):
     cu_list = []
     length = len(str)
     cu_list = [sum(str[0:x:1]) for x in range(0, length+1)]
     return cu_list[1:]


    cumulative_sum([1, 1, 1])
    cumulative_sum([1, 2, 3, 4])


# Or Class solution 

def cumulative_sum(somenums):
    output = []
    for i, num in enumerate(somenums):
        sum_so_far = sum(somenums[:i + 1])
        output.append(sum_so_far)
    return output 


