from ultralytics import YOLO


for scale in ["n", "s", "m", "l", "x"]:
    print("-" * 40 + f" Model scale: {scale} " + "-" * 40)

    model = YOLO(f'yolo11{scale}.yaml')
    model.fuse()

    model = YOLO(f'yolo149{scale}.yaml')
    model.fuse()

    model = YOLO(f'yolo1491{scale}.yaml')
    model.fuse()

    model = YOLO(f'yolo1492{scale}.yaml')
    model.fuse()

    model = YOLO(f'yolo1493{scale}.yaml')
    model.fuse()
