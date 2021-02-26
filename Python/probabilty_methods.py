import math as math
import random as random

class Number:
    number = int()
    def __init__(self,number):
        number = self.number
    
    def get_number(self):
        return number

    def set_number(self,int: value):
        number = self.value 
        return number

    def Ferm_test(self):
        '''
        Входные данные: нечетное число n≥5;
            Выходные данные: "число n составное", " число n вероятно
            простое".
            1. Выбирается случайное целое число a, 2<=a<=n-2.
            2. Вычисляется r = a^(n-1)(mod n) .
            3. При r=1 тест дает ответ, что "число n вероятно простое".
            Иначе " число n составное ".
        '''
        test_number = get_number()
        a  = int(random.random(2,test_number-2)) # random.random() возвращает float
        r = int((a**(test_number-1))%test_number)
        if r ==1:
            return "Число {} вероятно простое",format(test_number)
        else:
            return "Число {} составное",format(test_number)  

    def R_M_test(self,k):
        '''
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
        tested = get_number()
        if tested == 2:
            return True
        if tested % 2 == 0:
            return False
        r,s =0,tested-1
        while s%2 ==0:
            r+=1
            s//=2
            for _ in range(k):
                a = random.randrange(2, tested - 1)
                x = pow(a, s, tested)
                if x == 1 or x == tested - 1:
                    continue
                for _ in range(r - 1):
                    x = pow(x, 2, tested)
                    if x == tested - 1:
                        break
                else:
                    return False
            return True