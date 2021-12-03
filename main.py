from dec import decor_path
import os

filepath = os.path.join('C:/Users/Максим/Desktop', 'logs.txt')

@decor_path(filepath)
def summa(a, b):
    return a + b


one = summa(10, 5)
two = summa(10, 10)
result = summa(one, two)

print('result: ', result)
print('result type: ', type(result))