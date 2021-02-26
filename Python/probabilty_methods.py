import math as math
import random as random

class Number:
    number = int()
    def __init__(self):
       pass
    
    def get_number(self): 
        ''' Getter for number '''
        self.number = int(input('Введите желаемое число'))
        return self.number

    def Ferm_test(self,num:int):
        '''
        Входные данные: нечетное число n≥5;
            Выходные данные: "число n составное", " число n вероятно
            простое".
            1. Выбирается случайное целое число a, 2<=a<=n-2.
            2. Вычисляется r = a^(n-1)(mod n) .
            3. При r=1 тест дает ответ, что "число n вероятно простое".
            Иначе " число n составное ".
        '''
        a  = random.randint(2,num-2)
        r = int((a**(num-1))%num)
        if r ==1:
            print( "Число {0} вероятно простое".format(num))
        else:
            print( "Число {0} составное".format(num))

    def R_M_test(self,k:int,num:int):
        '''
        k - Количество испитаний
        1. Представить n-1 в виде n-1=2^s  число r - нечетное.
        2. Выбирается случайное целое число a, 2<=a<=n-2.
        3. Вычислить y = a^r(mod n)
        4. При y != 1 и y != n-1 выполнить следующие действия:
                    4.1 Пусть j=1
                    4.2 Если j<=s-1 и y≠n-1
                            4.2.1 Положить y=y^2 (mod n)
                            4.2.2 При y=1 результат: " число n составное "
                            4.2.3 Увеличить j на 1
                    4.3 При y != n-1 результат: " число n составное ".
        5. Результат: " число n вероятно простое "
        '''
       
        if num == 2:
            print("True")
        if num % 2 == 0:
           print("False")
        r,s =0,num-1
        while s%2 ==0:
            r+=1
            s//=2
            for _ in range(k):
             a = random.randrange(2, num - 1)
             x = pow(a, s, num)
            if x == 1 or x == num - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, num)
                if x == num - 1:
                    break
            else:
               print( 'Число {0} вероятно простое'.format(num))
        print( 'Число {0} составное'.format(num))


test =  Number()
num = test.get_number()
print('\n')
choice = int(input('Выберите желаемый тест : \n 1. Тест Ферма \n 2. Тест Рабина - Миллера \n'))
while choice !=1 and choice !=2:
    print('Неверная команда!')
if choice == 1:
    test.Ferm_test(num)
else:
   test_num =  int(input('Введите число проверок : '))
   test.R_M_test(test_num,num)