---
title: "Brain Tumor Classification"
date: 2021-03-01
tags:
 - Python
 - Jupyter Notebook
 
excerpt: "CNN model to classify Brain Tumors of types Meningioma, Glioma & Pituitary"
header:
  overlay_image: "/Projects/Brain Tumor Classification/assets/image_1.png"
  overlay_filter: 0.3 # same as adding an opacity of 0.3 to a black background
  teaser: "/Projects/Brain Tumor Classification/assets/image_1.png"
  actions:
    - label: "Go to GitHub Repository"
      url: "https://github.com/sanjayjaras/sanjayjaras.github.io/tree/master/Projects/Brain%20Tumor%20Classification"
---


# Brain Tumor Classification
Images are used in various fields to make the problem easier to understand. Image processing techniques are most widely used in medical imaging to identify the affected area through an X-ray, computed tomography scan(CT scan), MRI scan(Magnetic resonance images).
These images used to detect, identify, and locate the infections, abnormal growths from the human body. Heart diseases, Cancer, Brain tumor, Blood clotting, these are some of the abnormalities that can be found by medical imaging techniques. We can use different machine
learning techniques to classify different types of brain tumors by using MRI. The convolutional neural network (CNN) is a class of deep learning neural networks that are highly effective with image classifications. 

With every year, the number of patients with a brain tumor is increasing. There are two classes of brain tumors, primary and secondary tumors. Primary tumors have several types; one of the frequently found is a meningioma type. It is very challenging to locate, detect, and select
the infected tumor portion in the brain from the MRI (Magnetic resonance images). This tedious and time-consuming job requires radiologists and medical field experts. The accuracy of this task is mainly subject to the experience and expertise of the person performing this task. So, if we use a machine learning model to perform this task, it will help to overcome the shortcomings of the person involved in performing this task. So, I think if we can automate this process of classifying the tumors by using machine learning algorithms, it will improve the accuracy of the results and cost due to the expertise required. If we correctly classify the tumors, the specific treatment to that type of tumor can be applied. The accurate data about type and position assists in planning the surgical process for its extraction. An estimated 700,000 Americans are living with a brain tumor. Out of all brain tumors, approximately 69.8% of tumors are benign and 30.2% are malignant. An estimated 87,240 people will receive a primary brain tumor diagnosis in 2020.
Types of brain tumors: For this implementation, I have considered following brain tumor type. 
1. Meningioma: The meningioma type of tumors seen near the top-outer part of the brain. Meningioma is slowly growing noncancerous tumors that cause seizures and visual problems. This type of tumors accounting for 37.6% of all tumors, and 53.3% of all nonmalignant tumors.
   
  <img src="/Projects/Brain Tumor Classification/assets/image_2.png" alt="Meningioma" />

2. Glioma: Glioma is an abnormal growth in glial cells present around the neurons in the brain. Gliomas (such as glioblastoma, ependymomas, astrocytomas, and oligodendrogliomas), which make up 81% of malignant brain tumors in adults.
   <img src="/Projects/Brain Tumor Classification/assets/image_3.png" alt="Glioma" />

3. Pituitary: Pituitary tumors grow in pituitary glands that affect body functions. Some pituitary tumors result in too many of the hormones that regulate important functions of your body. Some pituitary tumors can cause your pituitary gland to produce lower levels of hormones.

<img src="/Projects/Brain Tumor Classification/assets/image_4.png" alt="Pituitary" />

I followed the following approach comprising image preprocessing like noise removal, cropping the image, extraction, augmentation, and classification of the MRI images. Convolution neural networks are a breakthrough in image recognition. They’re most commonly used to
analyze visual imagery and are frequently working behind the scenes in image classification. In my approach, I used vector with size 65536 for each image, rather than using 3-dimensional arrays for images. As per my observation, it is taking less time for training with a vector. I have
transformed RGB images to grayscale. This image transformation changes 3 RGB channels to only one channel, reduces the memory footprint, and training time.

<img src="/Projects/Brain Tumor Classification/assets/image_5.png" alt="plot-1" />
<img src="/Projects/Brain Tumor Classification/assets/image_6.png" alt="plot-2" />

