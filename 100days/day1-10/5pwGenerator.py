import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

input_letters = int(input("How many letters would you like in your password?\n"))
input_numbers = int(input("How many numbers would you like?\n"))
input_special_characters = int(input("How many special characters would you like?\n"))

def generate_password(letters_count, numbers_count, special_characters_count):
    password_list = []
    
    for _ in range(letters_count):
        password_list.append(random.choice(letters))
    
    for _ in range(numbers_count):
        password_list.append(random.choice(numbers))
    
    for _ in range(special_characters_count):
        password_list.append(random.choice(special_characters))
    
    random.shuffle(password_list)
    
    password = ''.join(password_list)
    return password

print(generate_password(input_letters, input_numbers, input_special_characters))