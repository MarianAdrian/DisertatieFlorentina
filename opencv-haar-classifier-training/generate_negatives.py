from PIL import Image
import random

width = 44
heigth = 20

skin_tone_R = 191
skin_tone_G = 165
skin_tone_B = 140

def _set_zeroes(number):
    ret_val = ''
    nr_cifre = 0
    while number>0:
        nr_cifre = nr_cifre + 1
        number = int(number/10)
    for index in range(1, 5-nr_cifre):
        ret_val = ret_val+'0'
    return ret_val

def _generate_images(nr_images):
    
    for count in range(1, nr_images+1):
        heigth = random.randrange(2, 20)*10
        width = int(heigth*2.2)
        img = Image.new( 'RGB', (width, heigth), "black") # create a new black image
        pixels = img.load() # create the pixel map
        ran_R = random.randrange(-1*int(skin_tone_R*0.05),int(skin_tone_R*0.05))
        ran_G = random.randrange(-1*int(skin_tone_G*0.05),int(skin_tone_G*0.05))
        ran_B = random.randrange(-1*int(skin_tone_B*0.05),int(skin_tone_B*0.05))
        for i in range(img.size[0]):    # for every pixel:
            for j in range(img.size[1]):
                r = random.randrange(-1*5,5)
                g = random.randrange(-1*5,5)
                b = random.randrange(-1*5,5)
                pixels[i,j] = (skin_tone_R + ran_R + r, skin_tone_G + ran_G + g, skin_tone_B + ran_B + b) # set the colour accordingly
        img_name = 'negative_images/' +_set_zeroes(count) + str(count) + '.jpg'
        img.save(img_name)
        print(str(count) + ' of ' + str(nr_images))

_generate_images(630)
