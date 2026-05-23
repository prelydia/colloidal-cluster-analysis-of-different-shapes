import ultralytics
from ultralytics import YOLO
from roboflow import Roboflow

model = YOLO('yolov8s-seg.pt')  # load a pretrained model (recommended for training)

rf = Roboflow(api_key="YOUR_ROBOFLOW_API_KEY")
project = rf.workspace("YOUR_ROBOFLOW_WORKSPACE").project("YOUR_PROJECT_NAME")

"""### Training and Deployment"""

# NOTE: hyperparameters such as epochs, device, batch size, and etc.
# should be tuned according to your dataset size and available hardware resources.
model.train(data="PATH_TO_YOUR_DATA.YAML_FILE", epochs=100,
            translate=0.0, shear=0.0, mosaic=0.0, perspective=0.0, warmup_epochs=0, device=[0,1,2,3,4,5,6,7], batch=56, freeze=8)

VERSION = YOUR_VERSION  # e.g. 1, 2, 3 depending on Roboflow project
project.version(VERSION).deploy(model_type="yolov8", model_path="PATH_TO_TRAIN_RESULTS")