
# 🦕 Evaluating and Fine-tuning Grounding DINO

In this project the new state of the art object localization and classification model Grounding DINO is evaluated and fine-tuned on a specific dataset. 

Grounding DINO is a transformer based object detection model [DETR model] for open-set object detection. Built by extending a closed-set detector DINO by performing vision-language modality fusion at multiple fases: feature enhancer, langauage-guided query selection module, cross-modality decoder.

The model has a dual-encoder-single-decoder architecture.

The dataset is called Ot & Sien ++. Which is a collection of children's book illustration published before the 1880. The ++ stands for the improvement and corrected mistakes on the original dataset and to make it ML ready. This is done by H. Wang and S. Khademi.

The goal of the dataset is to aid the development of automatic visual object detection in these children's books. This can be of value for librarians and humanity researchers who study the illustrations in these books.

New object detection models struggle with this dataset because the models are trained on real life images, not on illustrations.

This project aims to solve that struggle by fine-tuning Grounding DINO on Ot & Sien ++.

## Notebooks
* Demo
* EDA of Ot & Sien ++
* Evaluation
    * Evaluating Grounding DINO
    * Evaluating on PASCAL VOC 2012
    * Evaluating on Clipart
* Fine-tuning

_Note: all notebooks are developed in Google Colab and therefore it is recommended to use them in Google Colab, otherwise problems might arise._

### Demo
This notebook is a demo to run the GroundingDINO model on a single image. To use this notebook yourself, the following things need to be changed:
* The image path to the image you want to run the model on
* The prompt to give GroundingDINO. It is recommended use "." to seperate different objects you want to detect.


### EDA of Ot & Sien ++

This notebook performs an exploratory data analysis on the Ot & Sien ++ dataset. It counts all the classes in the dataset and checks which classes do not occur. This is done separately for the train, validation and test set since the Ot & Sien ++ dataset is already split into these sets. Lastly 9 images a plotted to show what type of images are in the dataset

To use the notebook, under 'Define all classes in dataset and dataset to analyse' in the code block the 'data_directory'variable must be changed to where your dataset is located.

### Evaluation
#### Evaluating Grounding DINO
This notebook is used to measure the performance of GroundingDINO on the Ot&Sien dataset. The model is evaluated by looking at the mAP, the confusion matrix, the APs of the frequent classes, detection accuracy and classification accuracy. At the end, you can also compare two versions of the model on a single image and look at the model predictions of certain classes.


#### Evaluating on PASCAL VOC 2012
This notebook is used to measure the performance of GroundingDINO on the PASCAL VOC dataset. Because DINO is trained on pictures it is important to know the decrease in performance when using illustrations. The model is evaluated by looking at the mAP, the confusion matrix, the APs of the classes.

#### Evaluating on Clipart
This notebook is used to measure the performance of GroundingDINO on the Clipart1k dataset. The model is evaluated by looking at the mAP, the confusion matrix, the APs of the classes, detection accuracy and classification accuracy. At the end, there is also a visualization of the annotations on a single image.


### Fine-tuning

This notebook provides the training code to fine-tune Grounding DINO on the Ot & Sien ++ dataset. 

When using the notebook make sure to change the 'data_directory' variable under 'Data Preprocessing and Loading'. And change the 'amount_of_batches' to set the amount of batches used for each epoch.

Under 'Grounding DINO Implementation' -> 'Run model' the specific layers can be defined to freeze and unfreeze to fine-tune the model. The default is set to the linear layers in the decoder block of the model.

Tune the amount of epochs and learning rate to your liking.

## Used Datasets
* Ot & Sien ++ 

    https://data.4tu.nl/datasets/d1f3ca5c-f1e4-48f5-9a04-0564572d2b9c/1

* Clipart

    https://paperswithcode.com/dataset/clipart1k
* PASCAL VOC

    http://host.robots.ox.ac.uk/pascal/VOC/

## Project Requirements

The requirements are Google Colab and the python libraries mentioned in the requirements.txt file. If any library is not found by Colab add the line '!pip install x', whith x being the missing library.

## Results

This is one of the results of the evaluation of the untrained Grounding DINO model:

![alt text]([http://url/to/img.png](https://github.com/Linuxable/capstone/blob/main/example-results/detclass_acc.png))


## Future Recommendations
For future work in this project several things can be done.
1. When released, use the official training code for Grounding DINO to fine-tune the model on Ot & Sien ++
2. Explore model improvements by data preprocessing. For example using data augmentation to increase the dataset
3. If possible, create a loss function looking at the amount of classes Grounding DINO predicted and the amount of true labels in an image.
4. Further investigate which layers should be frozen for fine-tuning.

## Authors
The authors of this project are:
* Jaap Donkers - J.E.Donkers@student.tudelft.nl
* Otto Brouwers - O.R.Brouwers@student.tudelft.nl
* Lars de Hoop - L.deHoop@student.tudelft.nl
* Niels Braam - N.V.C.Braam@student.tudelft.nl
* Job Ruijters - J.A.V.Ruijters@student.tudelft.nl
* Abel de Lange - A.L.deLange@student.tudelft.nl
