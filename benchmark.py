from ultralytics import YOLO


for scale in ["n", "s", "m", "l", "x"]:
    print("-" * 40 + f" Model scale: {scale} " + "-" * 40)

    model = YOLO(f'yolo11{scale}.yaml')
    model.fuse()

    model = YOLO(f'yolo14{scale}.yaml')
    model.fuse()

    model = YOLO(f'yolo142{scale}.yaml')
    model.fuse()

    model = YOLO(f'yolo145{scale}.yaml')
    model.fuse()

    model = YOLO(f'yolo147{scale}.yaml')
    model.fuse()
