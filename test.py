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

#benchmark(model="yolo143s.yaml", data="coco.yaml", imgsz=640, half=False, format="onnx")
benchmark(model="yolo143s.yaml", data="coco.yaml", imgsz=640, half=False, format="onnx", device='cuda')
# # Load the YOLO11 model
# model = YOLO("yolo11n.yaml")

# # Export the model to ONNX format
# model.export(format="onnx")  # creates 'yolo11n.onnx'

# # Load the exported ONNX model
# onnx_model = YOLO("yolo11n.onnx")

# # Run inference
# results = onnx_model("https://ultralytics.com/images/bus.jpg")