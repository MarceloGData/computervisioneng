from yolov9 import Yolov9


model = Yolov9('object-detection')

model.train(data='data.yaml', epochs=150)
