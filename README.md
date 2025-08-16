# Enhanced YOLO （基于YOLO11的优化版本）

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


本仓库在YOLO11的架构上进行了多项优化，显著提升模型推理速度和检测精度。目前改进实验还在进行中。

## ✨ 主要改进
### Micro design
1. 使用ConvNeXt结构：YOLO11系列模型使用了稠密的3x3卷积，模型各层的通道数非常小，限制了模型的表达能力。ConvNeXt结构使用了稀疏的depthwise卷积，在同等参数量和计算量下可以增加各层通道数，从而提升性能。
2. 使用了简化的C2f结构，在保持性能的前提下适当降低了一部分模型的参数量。

### Macro design
1. 模型的深度增加了一倍，显著提升了模型的性能上限


## 🛠️ 使用方法

### 安装环境
在 [**Python>=3.8**](https://www.python.org/) 环境中安装本文档 `ultralytics` 包，包括所有[依赖项](https://github.com/ultralytics/ultralytics/blob/main/pyproject.toml)，并确保 [**PyTorch>=1.8**](https://pytorch.org/get-started/locally/)。

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ultralytics?logo=python&logoColor=gold)](https://pypi.org/project/ultralytics/)
![PyTorch 1.8+](https://img.shields.io/badge/PyTorch-1.8%2B-orange)
```shell
pip install -e .
```

### 准备数据
请按ultralytics的格式准备检测框数据。参考[Ultralytics 文档](https://docs.ultralytics.com/)。


### 训练
1. 直接调用本目录下的`train.py`文件

    ```shell
    python train.py
    ```

2. 或者，使用自定义的训练参数
    ```python
    from ultralytics import YOLO

    model = YOLO('yolo143n.yaml')

    # Train the model
    results = model.train(
        data='coco.yaml',
        epochs=600, 
        batch=256, 
        imgsz=640,
        scale=0.5,  # S:0.9; M:0.9; L:0.9; X:0.9
        mosaic=1.0,
        ixup=0.0,  # S:0.05; M:0.15; L:0.15; X:0.2
        copy_paste=0.1,  # S:0.15; M:0.4; L:0.5; X:0.6
        device="0,1",
        save_period=10,
        workers=16,
        resume=True,
    )

    # Evaluate model performance on the validation set
    metrics = model.val()
    # # Perform object detection on an image
    # results = model("path/to/image.jpg")
    # results[0].show()

    # 对图像执行目标检测
    results = model("path/to/image.jpg")  # 对图像进行预测
    results[0].show()  # 显示结果

    # 将模型导出为 ONNX 格式以进行部署
    path = model.export(format="onnx")  # 返回导出模型的路径
    ```

