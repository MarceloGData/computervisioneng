from ultralytics import YOLO
import cv2


model = YOLO('yolo11n.pt')

cap = cv2.VideoCapture('http://192.168.0.44:81/stream')

ret = True
while ret:
	ret, frame = cap.read()
	if ret:
		detections = model(frame)

		for bbox in detections[0].boxes.xyxy:
			x1, y1, x2, y2 = bbox
			cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)

		cv2.imshow('frame', frame)
		cv2.waitKey(1)
