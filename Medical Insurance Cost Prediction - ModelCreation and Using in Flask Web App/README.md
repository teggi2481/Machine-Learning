# Liver Disease Prediction Project
This project focuses on building a machine learning model to predict liver disease based on patient medical attributes. Early detection of liver disease is crucial as it allows timely medical intervention and reduces risks of severe liver failure.

The dataset consists of patient records with both demographic and clinical features. The target variable (Dataset) indicates whether the patient is likely to have liver disease (1) or not (2).

### Attributes in the Dataset:

- Age: Age of the patient (years)
- Gender: Male / Female
- Total_Bilirubin: Total bilirubin level in the blood
- Direct_Bilirubin: Direct bilirubin level
- Alkaline_Phosphotase: Alkaline phosphotase enzyme level
- Alamine_Aminotransferase: Alamine aminotransferase enzyme level
- Aspartate_Aminotransferase: Aspartate aminotransferase enzyme level
- Total_Protiens: Total proteins in the blood
- Albumin: Albumin protein level
- Albumin_and_Globulin_Ratio: Ratio of albumin to globulin
- Dataset (Target): 1 → Patient has liver disease, 2 → No liver disease

The goal of this project is to analyze, preprocess, and build machine learning models that can accurately classify whether a patient is at risk of liver disease.


## Problem Statement
This data set contains 416 liver patient records and 167 non liver patient records collected from North East of Andhra Pradesh, India. The "Dataset" column is a class label used to divide groups into liver patient (liver disease) or not (no disease). This data set contains 441 male patient records and 142 female patient records.

Use these patient records to determine which patients have liver disease and which ones do not.

## Dataset
[Liver Disease Dataset](https://www.kaggle.com/uciml/indian-liver-patient-records)


## Technology used
- Python
- Machine Learning
- Pandas
- Numpy
- Scikit-learn
- Flask
- HTML
- CSS
- Pycharm
- Heroku

  
## Running Tests

To run app, run the following command

```bash
  python app.run
```

   
## Deployment

To deploy this project run following command in the project folder

```bash
  git bash open
```

Create .git file
```bash
  git init
```
Track all the files
```bash
  git add .
```
Cheacking file track or not
```bash
  git status
```
Store as separate version
```bash
  git commit -m 'message'
```
### Deployment on Heroku

Heroku login on git bash

```bash
  heroku login
```
Create new app

```bash
  heroku create
```
Push Code
```bash
  git remote -v
```
Push code to Master Branch
```bash
  git push heroku master
```