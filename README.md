This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

```
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
```
This project is dedicated to the automatic detection of colloidal cluster structures in microscopy images using a YOLOv8-based deep learning model.
The main goal is to classify and localize clusters of different shapes and configurations, enabling faster and more objective analysis of experimental data.

---

## Model Training

This project provides a training script based on the YOLOv8 framework.
It is used to train an object detection model on a custom dataset of colloidal cluster structures.
The script allows configuration of key training parameters such as epochs, batch size, and image resolution.

---

## Datasets

This work utilizes four separate datasets, each containing labeled microscopy images of colloidal clusters with distinct structural configurations: circular, cuboid, rod-like, and ellipsoidal formations.  
Due to their size, the datasets are stored externally and are not included in this repository.

You can download it here:

## cuboids: https://drive.google.com/file/d/1aP5jiKuuNghNN1M6nd-5ky8SZacmT4rc/view?usp=sharing
## rods: [https://drive.google.com/file/d/15dOkPKKClNxBEnkCdDIcfRJrOehqKGdR/view?usp=sharing](https://drive.google.com/file/d/1L7bkhg8T0ZlD-h3-MobHGC7AcxGLvYRx/view?usp=sharing)
## ellipsoids: https://drive.google.com/file/d/1Aj__Rjjik9Ty26jhvT78bOLXUbphSdVz/view?usp=sharing
## circles: https://drive.google.com/file/d/17P_sTEg-JyOtLliLLZP5BiL57xEW3AO6/view?usp=sharing
---
