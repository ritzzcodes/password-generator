import random
import math

alphabet = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
special = "@#$%&*"

pass_length = int(input("Enter Password Length"))

# length of password by 50-30-20 formula
alphabet_len = pass_length//2
num_len = math.ceil(pass_length*30/100)
special_len = pass_length-(alphabet_len+num_length)


password = []


def generate(length, array, is_alpha=False):
    for i in range(length):
        index = random.randint(0, len(array) - 1)
        character = array[index]
        if is_alpha:
            case = random.randint(0, 1)
            if case == 1:
                character = character.upper()
        password.append(character)


# alphabet password
generate(alphabet_len, alpha, True)
# numeric password
generate(num_length, num)
# special Character password
generate(special_len, special)
# suffle the generated password list
random.shuffle(password)
# convert List To string
gen_password = ""
for i in password:
    gen_password = gen_password + str(i)
print(gen_password)
