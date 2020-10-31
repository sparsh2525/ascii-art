from PIL import Image
import sys,os

gscale1 = "@%0#*+=-:. "
gscale2 = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\\"^`". '

#test code ayy lmao, pls ignore
'''
img=Image.open(sys.argv[1],mode='r')
w,h=img.size
aspect_ratio=h/w
size=200
img=img.resize((size,int(aspect_ratio*size*0.55)))
img=img.convert('L')
pixels=img.getdata()
char_string=[gscale2[int(pixel/3.7)] for pixel in pixels]
char_string=[''.join(char_string[i:i+size]) for i in range(0,len(char_string),size)]
char_string='\n'.join(char_string)
with open('art.txt','w') as f:
    f.write(char_string)
'''

def resize_image(img,size=150):
    w,h=img.size
    aspect_ratio=h/w
    img=img.resize((size,int(aspect_ratio*size*0.55)))
    return img

def convert_bw(img):
    return img.convert('L')

def convert_ascii(img,scale,size):
    factor=25 if scale==gscale1 else 3.7
    pixels=img.getdata()
    char_string=[scale[int(pixel/factor)] for pixel in pixels]
    char_string=[''.join(char_string[i:i+size]) for i in range(0,len(char_string),size)]
    char_string='\n'.join(char_string)
    return char_string

def write_to_file(char_string):
    with open('art.txt','w') as f:
        f.write(char_string)

def open_txt():
    try:
        os.startfile('art.txt')
    except Exception:
        print('Error opening result text')


def img_open():
    img=None
    try:
        img=Image.open(sys.argv[1],mode='r')
    except Exception:
        print("Image not found. Please pass in image file name in cmd line.")
        exit()
    return img

def main():
    img=img_open()
    try:
        scale=gscale1 if input("Enter choice for char string to be used (1 for 10 char, 2 for 69 char): ")=='1' else gscale2
        size=int(input("Enter width size (Default is 150): "))
    except Exception:
        size=150
    img=convert_bw(resize_image(img,size))
    write_to_file(convert_ascii(img,scale,size))
    open_txt()

if __name__ == "__main__":
    main()

    

