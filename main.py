import random
import time
from datetime import datetime
from time import sleep

def GetNum(i):
    string = ''
    for i in range(2**i):
        string += '1'
    return '0b'+ string

def bruteForce(i):
    start = datetime.now()
    receivedKey = 0
    while receivedKey != randKeys[i]:
        receivedKey += 1
    print('Время потрачено на нахождение {}: {}'.format(randKeys[i], datetime.now() - start))

keys = []
for i in range(3, 13):
    keys.append((2**i, int(GetNum(i), 2)))
    print('При ключе {} бит пространство ключей'.format(keys[i-3][0]), keys[i-3][1], 'бит')

randKeys = []
for i in keys:
    randKeys.append(random.randint(0, i[1]))

print('\nРандомно сгенерированные ключи: ')
for i in randKeys:
    print(i)

print('\nBrute Force:')

for i in range(0, len(randKeys)):
    bruteForce(i)



