echo [$(date)]: "START" 
echo [$(date)]: "creating env with python 3.8 version" 
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "activating the environment" 
source activate ./env     #since we are creating env in source sh file we need to activate conda env with this command - source activate <env name>
echo [$(date)]: "installing the dev requirements" 
pip install -r requirements_dev.txt
echo [$(date)]: "END" 