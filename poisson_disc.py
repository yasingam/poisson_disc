from PIL import Image
import numpy as np
import os
import random


def poisson_disc(path, r, out_name):

    image = Image.open(image_path)
    #create numpy array from PIL image object
    image_array = np.array(image)

    #create zero matrix to populate pixels
    new_image = np.zeros(np.shape(image_array), dtype='uint8')

    #creating a index matrix - i.e. a matrix where the element is its index
    a = np.shape(image_array)
    b = np.indices((a[0], a[1]))

    #reshapes the matrix to a single column of indices
    c = np.column_stack((b[0].flatten(), np.array(b[1].flatten())))

    while (len(c)>0):
        index = random.randint(0, len(c)-1)
        new_image[c[index][0], c[index][1]] = image_array[c[index][0], c[index][1]]
        dist_formula = np.sqrt(((c[:, 0]-c[index][0])**2 + (c[:, 1]-c[index][1])**2))
        c = c[dist_formula>r]

    out_image = Image.fromarray(new_image)
    out_image.save(out_name)
#r defines distance to sample from



#distance between pixels
distance = 3

#image details
image_name = 'in.tif'
image_path = os.getcwd() + '/' + image_name

#check if image exists - call function if it does
if (os.path.isfile(image_path)==True):
    poisson_disc(image_path, distance, 'out.tif')


