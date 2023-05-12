# /*
#  * Crea un programa que se encargue de calcular el aspect ratio de una
#  * imagen a partir de una url.
#  * - Url de ejemplo: https://raw.githubusercontent.com/mouredev/
#  *   mouredev/master/mouredev_github_profile.png
#  * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
#  *   imagen de 1920*1080px.
#  */

import cv2

ruta = '/Users/sebastiancastillo/Downloads/Mi proyecto (1).png'
im = cv2.imread(ruta)

print(type(im))

print(im.shape)
width = im.shape[0]
heigth = im.shape[1]

print(width/heigth)

print(dir(cv2))
