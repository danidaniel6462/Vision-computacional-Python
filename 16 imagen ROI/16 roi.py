import cv2
import numpy as np
import matplotlib.pyplot as plt

bild = cv2.imread('Koala.jpg', cv2.IMREAD_COLOR)
roi=bild[15:300,330:550]
bild  [35:320,30:250]=roi
cv2.imshow('original',bild)

alphabild=cv2.imread('Koala.jpg',cv2.IMREAD_UNCHANGED)
graybild=cv2.imread('Koala.jpg',cv2.IMREAD_GRAYSCALE)

titles=['Original','ALPHA','GRAY','ROI']
final =(bild,alphabild,graybild,roi)
for i in xrange (4):
    plt.subplot(2,2,i+1)
    plt.imshow(final[i])
    plt.colorbar()
    plt.grid()
    plt.xticks([]),plt.yticks([])

plt.show

cd=cv2.waitKey(0)
cv2.destroyAllWindows()
