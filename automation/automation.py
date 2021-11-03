import re

def numbers():

    f = open("potential-contacts.txt", "r").read()
    numbers = re.findall(r'(\d\d\d-\d\d\d-\d\d\d\d)', f)
    number_content = ''
    for num in sorted(numbers):
        number_content += str(num)
        number_content += f'\n'

    with open('phone_numbers.txt', 'w+') as file:
        file.write(number_content)
    return number_content
		


def email():
    f = open("potential-contacts.txt", "r").read()
    email = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', f)
    email_content = ''
    for em in sorted(email):
        email_content += str(em)
        email_content += f'\n'

    with open('emails.txt', 'w+') as file:
        file.write(email_content)
        return email_content


print(email())
print(numbers())




