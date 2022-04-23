# Author: Ben Burdett
# Date: 3/31/2022
# Description: https://youtu.be/oqEkeIo0LGo

# 1.	UI calls PRNG Service by writing the word "run" to prng-service.txt
# 2.	PRNG Service reads prng-service.txt, erases it, and writes a pseudo-random number to it
# 3.	UI reads prng-service.txt to get the pseudo-random number 
# 4.	UI writes the pseudo-random number to image-service.txt
# 5.	Image Service reads image-service.txt, erases it, and writes an image path to it
# 6.	UI reads image-service.txt then displays the image (or path) to the user

import tkinter as tk
from PIL import Image
from time import sleep


root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=450)
canvas.grid(columnspan=3, rowspan=3)

# instructions
instructions = tk.Label(root, text="Generate a random image by pressing the button")
instructions.grid(columnspan=3, column=0, row=1)

# browse
browse_image = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_image, command=lambda:open_file(), bg='black', bd=3, fg="white", height=3, width=20)
browse_image.set('Click Here')
browse_btn.grid(column=1, row=2)

def open_file():
    # Step 1
    with open('prng-service.txt', 'w') as file:
        file.write('run')
        print('Writing the word "run" to prng-service.txt...')
        
    sleep(10)    
    # Step 3
    with open('prng-service.txt', 'r') as file:
        number_in_line1 = file.read()
        print('Reading prng-service.txt to get random number...')   

    sleep(10) 
    # Step 4
    with open('image-service.txt', 'w') as file:
        file.write(f'{number_in_line1}')
        print('Writing random number to image-service.txt...')

    sleep(10)  
    # Step 6
    with open('image-service.txt', 'r') as file:
        image = file.read()
        im = Image.open(rf"{image}")
        im.show()
        print('Reading image-service.txt, await display...')


tk.mainloop()

