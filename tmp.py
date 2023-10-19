import cv2

  
# reading the vedio 
source = 'data/tmp_resized.mp4'
 
fourcc = cv2.VideoWriter_fourcc(*'h264')
# fourcc = cv2.VideoWriter_fourcc(*'MPEG')

output = cv2.VideoWriter(   "data/output.avi", fourcc, 30, (628,384)) 

cap = cv2.VideoCapture(source)
ct=0
while True:

  try:

    # Capture a frame from the video feed
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # # Apply a blur to the grayscale image
    # blur = cv2.GaussianBlur(gray, (9, 9), 0)

    # # Threshold the blurred image
    # thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY_INV)[1]

    # Display the original, grayscale, blurred, and thresholded images
    # cv2.imshow('Original Image', frame)
    # cv2.imshow('Grayscale Image', gray)
    # cv2.imshow('Blurred Image', blur)
    # cv2.imshow('Thresholded Image', thresh)
    output.write(gray) 
    
    ct+=1
    print(ct)
    # Wait for a key press and check if the 'q' key was pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  except:
    break

output.release() 
cap.release() 