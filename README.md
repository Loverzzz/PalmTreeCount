# Object Detection Using YOLOv8 for Palm Tree Detection

This repository demonstrates the process of training a YOLOv8 model for palm tree detection from large images using a sliding window approach. The project involves training a custom YOLOv8 model and using it for object detection in large images, followed by post-processing to combine the detected patches back into the original image.

## Table of Contents
- [Installation](#installation)
- [Dataset Preparation](#dataset-preparation)
- [Model Training](#model-training)
- [Sliding Window Detection](#sliding-window-detection)
- [Post-Processing](#post-processing)
- [Result Visualization](#result-visualization)

## Installation

To run this project, you need to install the required dependencies. The necessary libraries are listed below:

1. Install the required Python packages:
   ```bash
   pip install ultralytics
   pip install torch torchvision matplotlib
   
2. Ensure you have a compatible version of PyTorch installed with GPU support if you plan to use GPU for faster training.

3. Dataset Preparation
The dataset should be structured as follows:
   ```
    dataset/
        ├── images/
        │   ├── train/
        │   ├── val/
        ├── labels/
        │   ├── train/
        │   ├── val/
   ```
train: Folder containing images for training.
val: Folder containing images for validation.
labels/train: Folder containing labels for training.
labels/val: Folder containing labels for validation.

5. Dataset Configuration
Ensure that your dataset paths are correctly set in the data.yaml configuration file:
     ```
     train: path/to/train/images
      val: path/to/val/images
      nc: 1  # Number of classes (1 for palm tree)
      names: ['palmtree']  # Class name
     ```
6. Model Training
Initialize the YOLO model with a pre-trained weight:
  ```
  from ultralytics import YOLO
  
  model = YOLO('yolov8s.pt')  # Pre-trained YOLOv8 model
  ```
7. Start training the model:
```
model.train(
    data='path/to/data.yaml',  # Path to your dataset configuration
    epochs=50,  # Number of epochs
    imgsz=512,  # Image size
    batch=16,  # Batch size
    name='palm_tree_model',  # Name of the trained model
    single_cls=True  # Only one class (palm tree)
)
```
8. Sliding Window Detection
To detect objects in large images, we use a sliding window approach. This approach divides large images into smaller chunks with overlapping regions and performs detection on each chunk.
    ```
    def sliding_window(image, window_size=(512, 512), step_size=256):
        """
        Split a large image into smaller windows with overlap.
        """
        (h, w) = image.shape[:2]
        for y in range(0, h - window_size[1], step_size):
            for x in range(0, w - window_size[0], step_size):
                yield (x, y, image[y:y + window_size[1], x:x + window_size[0]])
    ```
9. Post-Processing
After detection, the results are combined back into the original image. The final image includes a label showing the total number of detected palm trees.
    ```
    def combine_image_pieces_with_text(original_image_path, cropped_images_folder, total_detections, window_size=(512, 512), step_size=256):
        """
        Combine cropped image pieces into the original image and add detection text.
        """
        # Combine image pieces and add text with total detections
        ...
    ```
10. Result Visualization
After processing, the image with combined detections is displayed and saved:
    ```
      cv2.imshow("Gambar Gabungan Final", cropped_image)
      cv2.imwrite(output_path, cropped_image)
    ```

  
