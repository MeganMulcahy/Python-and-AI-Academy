first_name = 'Meg'
last_name = 'M'
language = 'Python'
formated_string = 'I am %.2s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)

a = 4
b = 3.3

print('{} + {} = {:.2f}'.format(a, b, a + b))
print('{} - {} = {:.2f}'.format(a, b, a - b))
print('{} * {} = {:.2f}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {:.2f}'.format(a, b, a % b))
print('{} // {} = {:.2f}'.format(a, b, a // b))
print('{} ** {} = {:.2f}'.format(a, b, a ** b))

language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
pto = language[0:6:2] #
print(pto) # Pto
print(language[::-1]) # !dlroW ,olleH
print(language.endswith('on')) # False
print(language.count('y'))
print(language.count('y', 7, 14)) 
print(language.count('th'))

challenge = 'thirty\tdays\tof\tpython'
print(challenge.strip(' t'))
print(challenge.replace('\t', ''))
print(challenge.split('\t'))
print(challenge.split())
print(challenge.split(' '))

print(challenge.expandtabs())
print(challenge.expandtabs(10))
print(challenge.find('y'))
print(challenge.find('th'))
print(challenge.rfind('y'))  # finds last version
print(challenge.rfind('th'))
sub_string = 'da'
print(challenge.rindex(sub_string)) 
print(challenge.isalnum())
challenge = '30DaysPython'
print(challenge.isalnum()) # True

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'

acronym = "".join(word[0].upper() for word in web_tech)
print(acronym)
