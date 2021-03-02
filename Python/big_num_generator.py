import random


def generate_random_number(number_length: int = 9) -> int:
    result: list = []
    for _ in range(0, number_length):
        result.append(f"{random.randint(0, 9)}")
        if result[0] == '0':
            result[0] = f"{random.randint(0, 9)}"
    return int(''.join(result))


def checking_number_prime(number: int = 10) -> bool:
    divisor = 2
    while number % divisor != 0:
        divisor += 1
    return divisor == number


if __name__ == '__main__':
    while True:
        user_input = input('enter the length of the number: ')
        if user_input.isdigit():
            random_number = generate_random_number(int(user_input))
            if checking_number_prime(number=random_number):
                print(random_number, '- prime number')
            else:
                print(random_number, '- composite number')