import re

with open('../assets/potential-contacts.txt') as f:
  text_from_file = f.read()

phone_pattern = r"(\d{3}.\d{3}.\d{4})"

# finding phone number digits
phone_nums = re.findall(phone_pattern, text_from_file)

#list where the phone number digits will live
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
    
    # adds the non numerical characters to phone number for structuring
    if len(singular_phone_number) == 3:
      singular_phone_number += '-'
    if len(singular_phone_number) == 7:
      singular_phone_number += '-'
    if len(singular_phone_number) == 12:
      phone_numbers_raw.append(singular_phone_number)


#gets rid of repeats
no_dupe_phone = [*set(phone_numbers_raw)]

#writes to the file
with open('../assets/phone_numbers.txt', 'w') as f:
  for nums in no_dupe_phone:
    f.write(nums + '\n')