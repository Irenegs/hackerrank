regex_integer_in_range = r"^[^(0|\D)]\d{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=.\1)"	# Do not delete 'r'.
#pattern3 = re.compile(r"([A-Z])[A-Z]*([A-Z])[A-Z]*\2")

import re
P = input()

print (len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
print (len(re.findall(regex_alternating_repetitive_digit_pair, P)))
print(*re.findall(regex_alternating_repetitive_digit_pair, P))

#enla repetición alternada hay que conseguir que sí admita 1113242
