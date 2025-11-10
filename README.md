# Assistive OpenCV: Leveraging Machine Learning based ETA’s for Visually Impaired People
### Real-Time Navigation Support using YOLOv8s + OpenCV + Voice Guidance

This project aims to enhance mobility and independence for visually impaired individuals by assisting them in navigating real-world environments safely. The system uses **YOLOv8s** (with transfer learning) to detect obstacles in real-time and provides **audio navigation instructions**, enabling hands-free guidance.

---

## Features
- Real-time **object detection** on live camera feed  
- Detects common campus obstacles:
  - bike, car, cycle, light post, objects, pathhole, scooty, stairs, tree
- **Voice-based navigation feedback** (e.g., *"Move Right"*, *"Stop"*, *"Turn Left"*)
- Works in **dynamic outdoor and indoor environments**
- Lightweight YOLOv8s model ⇒ **fast + optimized for real-time**
- Can be deployed on **laptops, Raspberry Pi, Jetson, or mobile (future)**

---

## Dataset
- Custom dataset captured at **ABV-IIITM Gwalior campus**
- Total images: **670**
- Annotated using **Roboflow**
- Preprocessed and augmented (rotation, brightness, contrast, flip)
- Resized to **512 × 512**
- Train/Val/Test split: `70% / 20% / 10%`

---

## Model
- Model: **YOLOv8s**
- Training: Transfer Learning from pretrained COCO weights
- Framework: **Ultralytics YOLO + OpenCV**
- Parameters: **11.1M**
- Compute Cost: **28.7 GFLOPs**

### Performance Metrics
| Metric | Score |
|-------|-------|
| Precision | **87.6%** |
| Recall | **82.9%** |
| F1-Score | **85.2%** |
| mAP (0.50-0.95) | **55.8%** |

---

### Outputs
<img width="500" height="500" alt="Screenshot 2025-11-10 014018" src="https://github.com/user-attachments/assets/0a2b4fbe-6719-4d2e-8563-67a7f89155f6" />
<img width="500" height="500" alt="Screenshot 2025-11-10 014238" src="https://github.com/user-attachments/assets/73637e68-78e0-402a-a4d6-81cd80b32e8f" />
<img width="500" height="500" alt="Screenshot 2025-11-10 014435" src="https://github.com/user-attachments/assets/69f6d6e3-bbe5-40f9-bd53-7a6012c2aff4" />

### Thank you
Abhinandan Mandal
