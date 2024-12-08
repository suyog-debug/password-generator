print('welcome to password generator!')
small_letter_alphabet=('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
capital_letter_alphabet=('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
symbol=('!', '@', '#', '$', '%', '^', '<', '>', '?', '/', '[]', '=', ';', '-', '()')
number=('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
input_small_letter_alphabet=int(input('how many alphabet do you want in your password? '))
input_capital_letter=int(input('how many capital letter alphabet do you want in your password? '))
input_symbol=int(input('how many symbols do you want in your password? '))
input_number=int(input('how many numbers do you want in your password?'))
password=[]
import random
for i in range(1, input_small_letter_alphabet+1):
    random_alphabet=random.choice(small_letter_alphabet)
    password+=random_alphabet
for y in range(1, input_capital_letter+1):
    random_capital_letter=random.choice(capital_letter_alphabet)
    password+=random_capital_letter
for j in range(1, input_symbol+1):
    random_symbol=random.choice(symbol)
    password+=random_symbol
for k in range(1, input_number+1):
    random_number=random.choice(number)
    password+=random_number
random.shuffle(password)
final_password=''.join(password)
print(f'your final password is {final_password}')