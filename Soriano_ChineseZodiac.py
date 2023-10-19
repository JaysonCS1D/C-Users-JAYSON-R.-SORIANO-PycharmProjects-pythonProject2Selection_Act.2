# Enter birth year
birth_year = int(input("Enter your birth year: "))

# Determine what is the Chinese Zodiac sign
if (birth_year - 1900) % 12 == 0:
    zodiac_sign = "Rat"
elif (birth_year - 1900) % 12 == 1:
    zodiac_sign = "Ox"
elif (birth_year - 1900) % 12 == 2:
    zodiac_sign = "Tiger"
elif (birth_year - 1900) % 12 == 3:
    zodiac_sign = "Rabbit"
elif (birth_year - 1900) % 12 == 4:
    zodiac_sign = "Dragon"
elif (birth_year - 1900) % 12 == 5:
    zodiac_sign = "Snake"
elif (birth_year - 1900) % 12 == 6:
    zodiac_sign = "Horse"
elif (birth_year - 1900) % 12 == 7:
    zodiac_sign = "Goat"
elif (birth_year - 1900) % 12 == 8:
    zodiac_sign = "Monkey"
elif (birth_year - 1900) % 12 == 9:
    zodiac_sign = "Rooster"
elif (birth_year - 1900) % 12 == 10:
    zodiac_sign = "Dog"
else:
    zodiac_sign = "Pig"

# Print result
print(f"Your Chinese Zodiac sign is {zodiac_sign}.")
