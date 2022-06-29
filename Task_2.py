# Напишите функцию, которая проверяет: является ли слово палиндромом

def pol(s):
    for i in range(len(s) // 2 + 1):
        if s[i] != s[-1]:
            return False
        else:
            return True

s = input("Введите слово: ")
print(pol(s))