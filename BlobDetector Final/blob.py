import cv2
import numpy as np;

def nothing(x):
    pass

# Read image
im = cv2.imread("blob.jpg", cv2.IMREAD_GRAYSCALE)

cv2.namedWindow('Keypoints')

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

cv2.createTrackbar('UmbralMin', 'Keypoints', 10, 255, nothing)
cv2.createTrackbar('UmbralMax', 'Keypoints', 200, 255, nothing)
cv2.createTrackbar('Area', 'Keypoints', 1500, 3000, nothing)
cv2.createTrackbar('Circunf', 'Keypoints', 1, 10, nothing)
cv2.createTrackbar('Convexidad', 'Keypoints', 87, 100, nothing)
cv2.createTrackbar('Inercia', 'Keypoints', 1, 100, nothing)


while(1):

    # Change thresholds
    a = cv2.getTrackbarPos('UmbralMin','Keypoints')
    b = cv2.getTrackbarPos('UmbralMax','Keypoints')
    params.minThreshold = a
    params.maxThreshold = b

    # Filter by Area.
    area = cv2.getTrackbarPos('Area','Keypoints')
    params.filterByArea = True
    params.minArea = area

    # Filter by Circularity
    circunferencia = cv2.getTrackbarPos('Circunf','Keypoints')
    params.filterByCircularity = True
    params.minCircularity = float(circunferencia)/10

    # Filter by Convexity
    convexidad = cv2.getTrackbarPos('Convexidad','Keypoints')
    params.filterByConvexity = True
    params.minConvexity = float(convexidad)/100
            
    # Filter by Inertia
    inercia = cv2.getTrackbarPos('Inercia','Keypoints')
    params.filterByInertia = True
    params.minInertiaRatio = float(inercia)/100

    # Create a detector with the parameters
    ver = (cv2.__version__).split('.')
    if int(ver[0]) < 3 :
            detector = cv2.SimpleBlobDetector(params)
    else : 
            detector = cv2.SimpleBlobDetector_create(params)

    # Detect blobs.
    keypoints = detector.detect(im)

    # Draw detected blobs as red circles.
    ##cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ##ensures
    # the size of the circle corresponds to the size of blob

    im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv2.imshow("Keypoints",im_with_keypoints)    

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

# Show blobs
#cv2.imshow("Keypoints", im_with_keypoints)

cv2.destroyAllWindows()
