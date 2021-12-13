# MessyBridges

One of the classes I have taken at University of St. Thomas is Computer Visualization. This class
focus was image manipulation and learning about how images are perceieved to the computer. Python
was the main language used for this class due to a lot of helpful tools python has to offer when 
it comes to array manipulation.

This program had two main functions. One was to take an image and flip the image every 180-degrees
or so. The second function was to take a blurry image, or image with noise, and either make it more
clear or reduce the noise. An image with noise can mean a few different things, in this instance it
refers to a static like filter over an image. An example of what this looks like is when a you'd 
flip to a wrong channel on your TV and the screen will be a static gray with a bunch of pixels 
moving around. Except in this situation, it is a still image.

## Flipping an Image

As mentioned before, images to a computer is a 2d-array of values. The values are set in a fixed
range, this range is a spectrum between black (0) and white (255). A value of 125, for example,
would look gray if read.
To Flip an image, we take this 2d-array and flip the values across the y-axis.

## Reducing Noise

To reduce an images noise, there are a few ways of doing so, one example of how this is down in
this program is putting the image through a median filter. A median filter is the process of taking
an array value index of the image, and assigning it the average value of its neighbors. The amount
of neighbors taken from the index is called the "kernel". Increasing the kernel size can make the 
pixel or index value more accurate, however, it can also make the image more blury because these 
values are an average to each other. If the values of these indices are closer together then the
color would look about the same, creating a blurry affect on the image.
