# Brain Tumor Diagnosis using YOLOv8

## Project Overview
This project implements an automated brain tumor detection and classification system using deep learning. The system detects and classifies brain tumors into three categories: Meningioma, Glioma, and Pituitary tumors using the YOLOv8 pre-trained model.

## Dataset
The dataset is acquired from Kaggle and categorized into three tumor types:
1. **Meningioma** - Tumors arising from the meninges (membranes surrounding the brain)
2. **Glioma** - Tumors arising from glial cells in the brain
3. **Pituitary** - Tumors in the pituitary gland

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        INPUT: MRI IMAGES                         │
│                     (.jpeg, .png formats)                        │
└────────────────────���────────────────────┬───────────────────────┘
                                          │
                    ┌─────────────────────▼─────────────────────┐
                    │        DATA PREPROCESSING                 │
                    │  ┌──────────────────────────────────────┐ │
                    │  │ 1. Bilateral Filtering (Denoising)  │ │
                    │  │    - Reduces noise while preserving  │ │
                    │  │      image edges                     │ │
                    │  │    - Quality metric: PSNR            │ │
                    │  └──────────────────────────────────────┘ │
                    │  ┌──────────────────────────────────────┐ │
                    │  │ 2. Histogram Equalization            │
                    │  │    - Distributes pixel intensity     │
                    │  │    - Improves contrast               │
                    │  └──────────────────────────────────────┘ │
                    └─────────────────────┬─────────────────────┘
                                          │
                    ┌─────────────────────▼─────────────────────┐
                    │   YOLOv8 PRETRAINED MODEL                │
                    │  ┌──────────────────────────────────────┐ │
                    │  │ • Feature Extraction                 │ │
                    │  │ • Object Detection                   │ │
                    │  │ • Classification                     │ │
                    │  └──────────────────────────────────────┘ │
                    └─────────────────────┬─────────────────────┘
                                          │
                    ┌─────────────────────▼─────────────────────┐
                    │    TRAINING & VALIDATION                  │
                    │  • Train/Test Split                       │
                    │  • Model Fine-tuning                      │
                    │  • Performance Evaluation                 │
                    └─────────────────────┬─────────────────────┘
                                          │
┌─────────────────────────────────────────▼───────────────────────┐
│                     CLASSIFICATION RESULTS                       │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────┐   │
│  │   MENINGIOMA     │  │     GLIOMA       │  │  PITUITARY   │   │
│  │   Accuracy: 99%  │  │  Accuracy: 95%   │  │ Accuracy: 99%│   │
│  └──────────────────┘  └──────────────────┘  └──────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

## Data Preprocessing

### 1. Bilateral Filtering (Denoising)
- **Purpose**: Reduces noise while preserving edge information
- **Quality Metric**: PSNR (Peak Signal-to-Noise Ratio) is used to evaluate denoising effectiveness
- **Advantage**: Maintains sharp boundaries between tumor and healthy tissue

### 2. Histogram Equalization
- **Purpose**: Distributes pixel intensity across the image
- **Benefit**: Enhances contrast and improves visibility of tumor features
- **Result**: Better input for the neural network

## Model Training & Evaluation

### Architecture
- **Model**: YOLOv8 (Pre-trained)
- **Task**: Real-time object detection and classification
- **Input**: Preprocessed brain MRI images
- **Output**: Tumor type classification with confidence scores

### Training Process
1. Data loading and augmentation
2. Model initialization with pre-trained weights
3. Fine-tuning on brain tumor dataset
4. Validation on holdout test set

## Results & Performance

| Tumor Type | Accuracy |
|-----------|----------|
| Meningioma | 99% |
| Glioma | 95% |
| Pituitary | 99% |

## Project Files

- `finalyear-checkpoint.ipynb` - Main notebook with complete pipeline (preprocessing, training, evaluation)
- `Untitled0.ipynb` - Additional experimentation notebook
- `Final year rpoject Proposal.docx` - Project proposal document
- `README.md` - This file

## Technologies Used

- **Deep Learning Framework**: YOLOv8
- **Image Processing**: OpenCV, Bilateral Filtering
- **Data Analysis**: NumPy, Pandas
- **Visualization**: Matplotlib, Seaborn
- **Development Environment**: Jupyter Notebook

## Getting Started

1. Clone the repository
2. Install required dependencies
3. Prepare your dataset (place MRI images in appropriate directories)
4. Run the Jupyter notebooks to preprocess data and train the model
5. Evaluate results on test images

## Future Improvements

- Implement ensemble methods combining multiple models
- Expand to additional tumor types
- Deploy as web application for clinical use
- Implement grad-CAM visualization for model interpretability
- Optimize model for inference speed

## Dataset Citation

Dataset sourced from Kaggle - Brain Tumor MRI Dataset

## Author

Abel59-KR

## License

This project is open source and available under appropriate licensing.
