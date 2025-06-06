import os 
import logging 
from pathlib import Path 


logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name="cnnClassifier"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init_.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init_.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath=Path(filepath)  #provides path according to os

    filedir,filename=os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating Directory :{filedir} for file :{filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass #creating empty file only
            logging.info(f"creating empty file :{filepath}")
    
    else:
        logging.info(f"{filename} is already exists")
    


