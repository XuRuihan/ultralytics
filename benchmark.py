from ultralytics import YOLO


model = YOLO('yolo11n.yaml')
model.fuse()

model = YOLO('yolo142n.yaml')
model.fuse()

model = YOLO('yolo143n.yaml')
model.fuse()

model = YOLO('yolo15n.yaml')
model.fuse()

model = YOLO('yolo151n.yaml')
model.fuse()
