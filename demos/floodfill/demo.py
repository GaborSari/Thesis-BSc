import cv2
import numpy

img = cv2.imread('./demo.jpg', cv2.IMREAD_GRAYSCALE)
img = numpy.bitwise_not(img)
print(img.shape)
print(numpy.max(img))

cv2.imshow('img', img)
im_floodfill = img.copy()
# Mask used to flood filling.
# Notice the size needs to be 2 pixels than the image.
h, w = img.shape[:2]
mask = numpy.zeros((h + 2, w + 2), numpy.uint8)

# Floodfill from point (0, 0)
cv2.floodFill(im_floodfill, mask, (0, 0), 255, 10, 10)

# Invert floodfilled image
im_floodfill_inv = cv2.bitwise_not(im_floodfill)

# Combine the two images to get the foreground.

flooded = cv2.bitwise_or(img, im_floodfill_inv)
cv2.imshow('flooded', flooded)
cv2.imwrite('./result.jpg', flooded)
res = cv2.waitKey(0)
