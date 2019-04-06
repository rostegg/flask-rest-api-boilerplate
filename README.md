# Tiny Flask REST API boilerplate

## How to run?
For fast deploy, build `docker-compose build` or just run `run-docker.sh` script.  
For standart execute, just run `run-env.sh` script or install requirement (`pip install -r requirements.txt`) and run `run.py`, if you don't want to use virtualenv

#### Add Environment Variables
Just create `config.env` file in root folder, and write variables like: `VARIABLE_NAME="value"` and load to necessary config in `config.py`
More about Flask configuration variables you can read [here](http://flask.pocoo.org/docs/1.0/config/)
