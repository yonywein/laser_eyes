‘’’‏ This program is free software. It comes without any warranty, to
‏     * the extent permitted by applicable law. You can redistribute it
‏     * and/or modify it under the terms of the Do What The Fuck You Want
‏     * To Public License, Version 2, as published by Sam Hocevar. See
‏     * http://www.wtfpl.net/ for more details. ‘’’

from PIL import Image as Im
import math

GB_FAC = 6
Y_FAC = 14
DEC_PARAM = 0.0001
ANGLE = 5
POINTX = 595
POINTY = 405

def main():
    im = Im.open('a.jpeg')
    lens_flare(im)
    im.show()
    im.save('a2.jpeg')

def lens_flare(im, px = POINTX, py = POINTY, angle = ANGLE, dec_param = DEC_PARAM, gb_fac = GB_FAC, y_fac = Y_FAC):
    '''return a image with an laser eye in the coordinates specified.
    im - the image
    px - the x coordinate of the center of te eye
    py - the y coordinate of the center of the eye
    angle - the anticlockwise rotation size of the eye (in angles, not radians)
    all other param - look in dec_func documentation
    '''
    imageW = im.size[0]
    imageH = im.size[1]
    
    theta = angle * math.pi / 180
    c, s = math.cos(theta), math.sin(theta)
    
    for x in range(imageW):
        for y in range(imageH):
            printt('\n\n',x,y)
            
            nx = x - px
            ny = y- py
            
            nx = c * nx - s * ny
            ny = s * nx + c * ny
            
            r, g, b = im.getpixel((x,y))
            printt(r,g,b)
            
            r_val = dec_func(nx, ny, 1, y_fac, dec_param) #the 1 is used to say that it's red
            gb_val = dec_func(nx, ny, gb_fac, y_fac, dec_param)
            
            r = adv_ave(255, r, r_val)
            g = adv_ave(255, g, gb_val)
            b = adv_ave(255, b, gb_val)
            
            im.im.putpixel((x,y), (r,g,b))
    return im
          
            
def printt(*args): #used to control the printing
    pass
    #print(*args)
    
def adv_ave(val1, val2, val1_frac):
    #Weighted arithmetic mean of val1 ad val2, the weight of val1 is val1_frac and the weight of val2 is (1 - val1_frac)
    return int(val1_frac*val1 + (1-val1_frac)*val2)

def dec_func(valx, valy, gb_fac, y_fac, dec_param):
    '''The function the used to set the amount of changing in the color, the func is based on bivariate normal distribution
    valx, valy - the coordinates
    gb_fac - used to make the white core effect in the eye, set to 1 in case of the red color
    y_fac - used to strech the eye, 1 defines a circle, all the other values defining ellipses
    dec_param - defins the size of the eye, the lower to param the bigger the eye
    '''
    return math.exp(-1*gb_fac*dec_param*valx**2 -1*gb_fac*y_fac*dec_param*valy**2)
   
if __name__ == '__main__':
    main()
