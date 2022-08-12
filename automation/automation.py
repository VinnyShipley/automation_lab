import re

with open('../assets/potential-contacts.txt') as f:
  text_from_file = f.read()


email_pattern = 8

phone_pattern = r"(\d{3}.\d{3}.\d{4})"

phone_nums = re.findall(phone_pattern, text_from_file)


phone_numbers_raw = []


# Gets phone number in the correct form
for num in phone_nums:
  singular_phone_number = ''
  for number in num:
    if number == ')':
      continue
    if number == '-':
      continue
    if number == '.':
      continue
    if number == '(':
      continue
    joined_nums = singular_phone_number.join(number)
    singular_phone_number += number
    
    # adds the non numerical 
    if len(singular_phone_number) == 3:
      singular_phone_number += '-'
    # if len(singular_phone_number) == 5:
    #   singular_phone_number += '-'
    if len(singular_phone_number) == 7:
      singular_phone_number += '-'
    if len(singular_phone_number) == 12:
      phone_numbers_raw.append(singular_phone_number)
print(phone_numbers_raw)

no_dupe_phone = [*set(phone_numbers_raw)]


with open('../assets/phone_numbers.txt', 'w') as f:
  for nums in no_dupe_phone:
    f.write(nums + '\n')