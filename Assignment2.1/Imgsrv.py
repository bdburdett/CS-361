# Author: Ben Burdett
# Date: 3/31/2022
# Description: returns the ith image from image-service.txt

from time import sleep

while True:
    sleep(10)

    with open('image-service.txt', 'r') as file:
        print('Awaiting number...')
        number_in_line = file.read()
        if number_in_line.isdigit():
            print('Generating image...')
            img_num = (int(number_in_line) % 3) + 1
            # erases it, and writes an image path to it
            with open('image-service.txt', 'w') as file:
                file.write(f'./images/{img_num}.jpg')
