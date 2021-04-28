# Strreamlit_DDos

# Project Name
> Classify the type of Distributed Dos attack.



This is project is about a Distributed Denial of Service attack classification.It is a multi-class classification project which helps to classify with help of the input parameters.


![](header.png)

## Overview
This is a Streamlit web app which tells  the  type  of  attack.


**##Problems faced and  how i dealt with it..**
The dataset consist of  multiple classes in the output variable.Also the dataset was imbalanced dataset(I.e in the dataset there were many  rows which had output variable value as normal.Due to such bias towards one class which may give incorrect results as output so to solve the problem we used the class weight method.)

## Motivation
I learned machine learning models both types supervised as well unsupervised machine learning algorith.It is important to show the model working using  a real world app using the flask framework.





##Image


![alt text](https://github.com/Amit9888/Strreamlit_DDos/blob/master/Capture.PNG?raw=true)


## packages used

numpy
pandas


##Steps done:;
1.Data reading and understanding the data types/Shape of the data.
2.Data preprocessing steps such as applying one hot encoding to categorical features and standarizing the numerical variables.
3.Handling imbalance multiclass data using providing class-weight to prevent bias towards classes with more values.
4.Applying various machine learning models for the class prediction


