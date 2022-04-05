# Author: Ben Burdett
# Date: 3/31/2022
# Description: generates pseudo-random numbers 

import random 
from time import sleep


while True:
    sleep(10)
    with open ('prng-service.txt', 'r') as file:
        command = file.read()
        # if line in file is "run" then generate a random number
        if command == 'run':
            print('Reads prng-service.txt, erases it, and writes a random number to it...')
            my_number = random.randint(1,3)
        else:
            print('waiting for command...')
            continue
        file.close()

    with open ('prng-service.txt', 'w') as file:
        # replace "run" from prng-service.txt with the random number
        file.write(f'{my_number}')
        file.close()
