from ultralytics import YOLO
import cv2
import json
import os

dir_path = 'data'

for file_path in os.listdir(dir_path):
    # check if current file_path is a file
    if os.path.isfile(os.path.join(dir_path, file_path)):
        # add filename to list
        if file_path.endswith('resized.mp4'):
            input_video='data/'+file_path
        # res.append(file_path)

# input video
cap = cv2.VideoCapture(input_video)

# model
model = YOLO("yolo-Weights/yolov8n.pt")

# object classes
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
            "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
            "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
            "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
            "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
            "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
            "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
            "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
            "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
            "teddy bear", "hair drier", "toothbrush"
            ]

detected_frames=[]
frame_count=0

while True:
    success, img = cap.read()
    results = model(img, stream=True)
    frame_count+=1

    print(frame_count)

    # coordinates
    for r in results:
        boxes = r.boxes

        for box in boxes:
            # class name
            cls = int(box.cls[0])

            #found_rec
            if cls<2:
                detected_frames.append(frame_count)
        
    if img is None:
        break
    if cv2.waitKey(1) == ord('q'):
        break

# removing duplicated frames
detected_frames=sorted(set(detected_frames))

# saving detected_frames to json

with open('detected_frames.json', 'w') as f:
    json.dump(detected_frames, f)

cap.release()
cv2.destroyAllWindows()