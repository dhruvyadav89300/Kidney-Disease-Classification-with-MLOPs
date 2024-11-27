# Kidney-Disease-Classification-with-MLOPs

I am currently learning MLOps, and this repository contains the code from the tutorial I have been following. In this project, I trained a Deep Learning model to detect kidney diseases. I have used the best coding practices to make the code production-grade.
<br>
There might still be a few errors—if you find any, please leave feedback. Thank you!


<br>
Here are a few things that I did:
- Modular coding for clean and reusable code structure.
- Experiment tracking using MLflow.
- Pipeline tracking and version control with DVC.
- Flask API for model serving.
- Containerized deployment with Docker.


## Workflow

This is the workflow that I followed for creation of every component.
1. Update config.yaml
2. Update secrets.yaml [If Any]
3. Update params.yaml
4. Update the entitiy
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. Update the app.py

## Steps to run

1. Clone the repository
```
git clone https://github.com/dhruvyadav89300/Kidney-Disease-Classification-with-MLOPs.git
cd Kidney-Disease-Classification-with-MLOPs

```

2. Setup a virtual environment

```
conda create -n kidney_classifier python=3.10.0

# Activate the virutal env
conda activate kideny_classifier
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Run the app

```
python app.py
```

### Optional Steps
5. To track pipeline, use

```
dvc pull
```

6. To re-run pipeline, use

```
dvc repro
```