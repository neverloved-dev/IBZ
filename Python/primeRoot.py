import math

class Input:
    @staticmethod
    def count_digits(n):
        if n == 0:
            return 0
        return 1 + n.count_digits(n // 10)

    @staticmethod
    def binary_input():
        binary = int(input("Введите число в двоичном виде (до 10 символов): "),2)
        try:
             binary == 0
        except Warning:
               print("Число слишком мало! Необходимо вводить числа строго больше нуля!")
        else:
            print("Необходимо вводить число только в двоичном виде!")
        try:
            digits = int(math.log10(binary)) + 1 > 10 # Проверяем если введенное число больше 10 значеиний
        except IndexError:
            print("Число слишком большое")
        return binary

    @staticmethod
    def decimal_input():
        decimal = int(input("Введите число в десятичном виде : "))
        try:
            decimal == 0
        except Warning:
            print("Число слишком мало! Необходимо вводить числа строго больше нуля!")
        except ValueError:
            print("Нужно вводить только числа")
        return decimal

    @staticmethod
    def hex_input():
        num = input("Введите 16 - ричное число :  ")
        try:
            hex = int(num, 16)  # interpret the input as a base-16 number, a hexadecimal.
        except ValueError:
            print("Вы не ввели 13-ричное число")
        return  hex

    @staticmethod
    def convert_binary_to_decimal(value):
      return int(value,2)

    @staticmethod
    def convert_hex_to_binary(value):
        return int(value,16)

class Prime:
    def __init__(self):
        pass

    @staticmethod
    def GCD(a,b): #НОД
        while a!=b:
            if a>b:
                a = a-b
            else:
                b = b - a
        return a
    # проверка на простоту тут  и на первообразность
    @staticmethod
    # Возврат первообразного корня для введенного числа
    def prime_root(value):
      required_set = set(num for num in range(1,value) if Prime.GCD(num,value)==1)
      for g in range(1,value):
          real_set = set(pow(g,powers)%value for powers in range(1,value))
          if required_set == real_set:
              return g


def main():
    print('Start')
    while True:
        menu = int(input('Введите 2, 10, 16 для начала ввода'))
        if menu == 2:
         dec_convert =  Input.convert_binary_to_decimal(Input.binary_input())
         prime_root = Prime.prime_root(dec_convert)
         print("Простое корень: {0}".format(prime_root))
        elif menu == 10:
          dec_convert =  Input.decimal_input()
          prime_root = Prime.prime_root(dec_convert)
          print("Простое корень: {0}".format(prime_root))
        elif menu == 16:
          hex_convert = Input.convert_hex_to_binary(Input.hex_input())
          prime_root = Prime.prime_root(hex_convert)
          print("Простое корень: {0}".format(prime_root))
        else:
            break

if __name__ == '__main__':
    main()
