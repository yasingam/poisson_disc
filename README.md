# poisson_disc
## My implementation/s of Poisson disc sampling over an image
![Alt text](/yasingam/poisson_disc/master/in.tif?raw=true "Optional Title")
### This literally just takes an image and make dots out of it spaces at least a minimum distance apart
#### Yasin's Log 03/04/2020
##### poisson_disc.py added, language - python3
1. The only background I know at this point is random sampling occurs at least a specified distance away from other points
2. As I didn't read existing documentation regarding faster algorithms I just made it up...and it's super slow
3. Consider reading and writing faster code in future
4. You wrote similar code years ago but you forgot why you did what you did. An explanation is to follow here.
5. What follows is a breakdown of what this program does (pertinent lines discussed)
6. An image using PIL and casts it to a numpy array
7. Created a new numpy zero array of the same shape to populate with pixel data
    * Datatype was explicitly cast to 'uint8'
8. An index matrix was created
    * `b = np.indices(a[0], a[1])` creates a matrix where each value is its index
    * `np.column_stack` and `flatten` is used to merge data into a single column
    * Your thought process was that with an index matrix you could measure distance between points
    * This distance is, the very one you learnt at school was employed to calculate this distance: `sqrt((x2 - x1)^2 + (y2 - y1)^2)`
    * You randomly sample an element in your index matrix, then you take the pixel data and put it in the right position in the zero matrix, then apply the distance formulat to the index matric to remove all values that fall within the distance defined by you.
9. This creates a nice visual effect but is super slow on large images
10. The once zero matrix is then exported as an image
11. You should read how other people approach this problem as your method is way too slow - maybe even consider another language
12. For now you make the background black - it makes the image very dark in certain cases. Consider changing this in future to either white or some mean or median colour of the imported image, or a close grey representation.
