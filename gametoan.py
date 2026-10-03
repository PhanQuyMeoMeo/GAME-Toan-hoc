import random
import operator

def cauhoi_ngaunhien():
    operators ={
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }

    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    operation = random.choice(list(operators.keys()))
    answer = operators.get(operation)(num_1, num_2)
    print(f'ket qua cua {num_1} {operation} {num_2}')
    return answer

def hoicauhoi():
    answer = cauhoi_ngaunhien()
    guess = float(input('nhap ket qua: '))
    return guess == answer

def game():
    score = 0
    while True:
        if hoicauhoi() == True:
            score += 1
            print('chinh xac !')
        else:
            print('sai')
            break
    print(f'======== Game Over ========\ndiem cua ban la {score}\nco gang hon nhe!')

game()
