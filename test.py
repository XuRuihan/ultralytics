# from ultralytics import YOLO

# # Load the YOLO11 model
# model = YOLO("yolo11n.yaml")

# # Export the model to TensorRT format
# model.export(format="engine")  # creates 'yolo11n.engine'

# # Load the exported TensorRT model
# tensorrt_model = YOLO("yolo11n.engine")

# # Run inference
# results = tensorrt_model("https://ultralytics.com/images/bus.jpg")

from ultralytics import YOLO
from ultralytics.utils.benchmarks import benchmark
from ultralytics.utils.benchmarks import ProfileModels

#benchmark(model="/home/xsh/YOLO/ultralytics/runs/detect/train9/weights/epoch540.pt", data="coco.yaml", imgsz=640, half=False, format="onnx")
# benchmark(model="yolo142n.yaml", data="coco.yaml", imgsz=640, half=False, format="onnx", device='cuda')

# benchmark(model="/home/xsh/yolo11n.pt", data="coco.yaml", imgsz=640, half=True, format="engine", device='cuda')
# profiler = ProfileModels(["yolo12n.yaml", "yolo142n.yaml", "yolo11n.yaml", "yolo14n.yaml", "yolo145n.yaml", "yolo146n.yaml", "yolo147n.yaml", "yolo148n.yaml", "yolo1471n.yaml"], imgsz=640, device='cuda:1')

profiler = ProfileModels(["yolo147n.yaml", "yolo1471n.yaml", "yolo1472n.yaml", "yolo1473n.yaml"], imgsz=640, device='cuda')
profiler.run()

# model = YOLO("yolo1471.yaml")
# model.fuse()
# model = YOLO("yolo147.yaml")
# model.fuse()

# model = YOLO('/home/xsh/YOLO/ultralytics/runs/detect/train_yolo142n_residual/weights/last.pt')
# model.val(data='coco.yaml', half=False, rect=False, batch=224, workers=16, amp=True, device="0,1")
# # Load the YOLO11 model
# model = YOLO("yolo11n.yaml")

# # Export the model to ONNX format
# model.export(format="onnx")  # creates 'yolo11n.onnx'

# # Load the exported ONNX model
# onnx_model = YOLO("yolo11n.onnx")

# # Run inference
# results = onnx_model("https://ultralytics.com/images/bus.jpg")