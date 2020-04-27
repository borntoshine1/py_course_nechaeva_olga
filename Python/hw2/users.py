from faker import Faker

def users_addres(length: int=100):
    fake = Faker()
    data = ''

    for i in range(length):
        data += (fake.name() + ' ' + fake.email() + '\n')

    return data
