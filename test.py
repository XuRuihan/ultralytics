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

#benchmark(model="/home/xsh/YOLO/ultralytics/runs/detect/train9/weights/epoch540.pt", data="coco.yaml", imgsz=640, half=False, format="onnx")
benchmark(model="/home/xsh/YOLO/ultralytics/runs/detect/train_yolo142n/weights/best.pt", data="coco.yaml", imgsz=640, half=False, format="onnx", device='cuda')
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