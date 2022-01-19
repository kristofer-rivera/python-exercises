
# Movie rental situation
# Assigning values to the movies based on rental duration.

little_mermaid = 3
brother_bear = 5
hercules = 1

# P represents price. 
p = 3

# Calculation of total cost

total_cost = (p * little_mermaid) + (p * brother_bear) + (p * hercules) 
print(total_cost)

# Contracting situation
# Assigning pay values 

google_pay = 400
amazon_pay = 380 
facebook_pay = 350

google_hours = 6
facebook_hours = 10
amazon_hours = 4


# Pay calculation
total_pay = (google_pay * google_hours) + (amazon_pay * amazon_hours) + (facebook_pay * facebook_hours) 
print(total_pay)


# Student enrollment situation

class_not_full = True 
schedule_not_full = False
student_can_enroll = class_not_full and schedule_not_full
print(f'Can the student enroll? \n {student_can_enroll}')  

# Product offer situation 

is_premium_member = True 
more_than_two_items = False 

offer_not_expired = True 
discount_valid = offer_not_expired and (is_premium_member or more_than_two_items)
print(discount_valid)


# Pasword situation

username = 'codeup'
password = 'notastrongpassword'

password_is_long_enough = len(password) >= 5
username_is_short_enough = len(username) <= 20
username_and_password_are_different = username != password
username_has_spaces = username != username.strip()
password_has_spaces = password != password.strip()

username_good = username_is_short_enough and username_and_password_are_different and (not username_has_spaces)
password_good = password_is_long_enough and username_and_password_are_different and (not password_has_spaces) 

valid_credentials = username_good and password_good 

print('Username good?')
print(username_good)
print('Password good?')
print(password_good)
print('credentials valid?')
print(valid_credentials)









