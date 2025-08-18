from ultralytics import YOLO


for scale in ["n", "s", "m", "l", "x"]:
    print("-" * 40 + f" Model scale: {scale} " + "-" * 40)

    model = YOLO(f'yolo11{scale}.yaml')
    model.fuse()

    model = YOLO(f'yolo14{scale}.yaml')
    model.fuse()

    model = YOLO(f'yolo142{scale}.yaml')
    model.fuse()

    model = YOLO(f'yolo143{scale}.yaml')
    model.fuse()

<<<<<<< HEAD
model = YOLO('yolo152n.yaml')
model.fuse()

print("")

model = YOLO('yolo11s.yaml')
model.fuse()

model = YOLO('yolo14s.yaml')
model.fuse()

model = YOLO('yolo142s.yaml')
model.fuse()

model = YOLO('yolo144s.yaml')
model.fuse()

model = YOLO('yolo151s.yaml')
model.fuse()

model = YOLO('yolo152s.yaml')
model.fuse()

print("")

model = YOLO('yolo11m.yaml')
model.fuse()

model = YOLO('yolo14m.yaml')
model.fuse()

model = YOLO('yolo142m.yaml')
model.fuse()

model = YOLO('yolo144m.yaml')
model.fuse()

model = YOLO('yolo151m.yaml')
model.fuse()

model = YOLO('yolo152m.yaml')
model.fuse()


print("")

model = YOLO('yolo11l.yaml')
model.fuse()

model = YOLO('yolo14l.yaml')
model.fuse()

model = YOLO('yolo142l.yaml')
model.fuse()

model = YOLO('yolo144l.yaml')
model.fuse()

model = YOLO('yolo151l.yaml')
model.fuse()

model = YOLO('yolo152l.yaml')
model.fuse()


print("")

model = YOLO('yolo11x.yaml')
model.fuse()

model = YOLO('yolo14x.yaml')
model.fuse()

model = YOLO('yolo142x.yaml')
model.fuse()

model = YOLO('yolo144x.yaml')
model.fuse()

model = YOLO('yolo151x.yaml')
model.fuse()

model = YOLO('yolo152x.yaml')
model.fuse()
=======
    model = YOLO(f'yolo15{scale}.yaml')
    model.fuse()

    model = YOLO(f'yolo151{scale}.yaml')
    model.fuse()
>>>>>>> f9e2c16882e0a4584b09260455550b904576012f
