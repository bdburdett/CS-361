# Author: Ben Burdett
# Date: 3/31/2022
# Description: generates pseudo-random numbers 

import random 
from time import sleep


while True:
    sleep(1)
    with open ('prng-service.txt', 'r') as file:
        command = file.read()
        # if line in file is "run" then generate a random number
        if command == 'run':
            my_number = random.randint(1,3)
        else:
            break
        file.close()

    with open ('prng-service.txt', 'w') as file:
        # replace "run" from prng-service.txt with the random number
        file.write(str(my_number))
        file.close()
