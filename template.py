import os
from pathlib import Path
import logging #to log information during runtime
# logging.basicConfig(level=logging.INFO,format='[%*(asctime)s]:%(message)s:')
logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(message)s')

#project structure
project_name="textSummarizer"
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/conponents/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",

]
for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath) #for splitting ex:config/config.yaml->('config','config.yaml')
    
    if filedir !=" ":   #if directory not exists create it
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating a directory:{filedir} for the file:{filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):  #checking if the file is present and the data in the file is present by using the method called getsize()
        with open(filepath,"w") as f:
            pass        #else create a new file with the filename as mentioned
            logging.info(f"Creating  an new file:{filepath}")
    
    else:       #logging if the file already exists 
        logging.info(f"{filename} already exists")