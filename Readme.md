# Clahe Implementation

### -What is Clahe
CLAHE is a variant of Adaptive histogram equalization (AHE) which takes care of over-amplification of the contrast. CLAHE operates on small regions in the image, called tiles, rather than the entire image. The neighboring tiles are then combined using bilinear interpolation to remove the artificial boundaries.
This algorithm can be applied to improve the contrast of images.

### Prerequestives
Add the image on which you want to implement the clahe inside the root folder 
Now we can change either update the line 3 of the main.py file with the name of the image or we can change the name of the image as image-input.jpg
