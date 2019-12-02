# Predict python

[![License MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![HitCount](http://hits.dwyl.io/nirdizati-research/predict-python.svg)](http://hits.dwyl.io/nirdizati-research/predict-python)

Master

[![Build Status](https://travis-ci.org/nirdizati-research/predict-python.svg?branch=master)](https://travis-ci.org/nirdizati-research/predict-python)
[![codecov](https://codecov.io/gh/nirdizati-research/predict-python/branch/master/graph/badge.svg)](https://codecov.io/gh/nirdizati-research/predict-python)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/nirdizati-research/predict-python.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/nirdizati-research/predict-python/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/nirdizati-research/predict-python.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/nirdizati-research/predict-python/context:python)
[![Maintainability](https://api.codeclimate.com/v1/badges/98fd94d6a3d53c3f9182/maintainability)](https://codeclimate.com/github/nirdizati-research/predict-python/maintainability)

Django backend server for machine learning on event logs.

## Requirements

install docker

install pycharm enterprise, NOT community


## Docker Compose
Please follow the [instructions in the video](https://youtu.be/gmxGOpjh2g0)
On first run to setup the database, you can run:
```bash
docker-compose up -d db
docker-compose run progetto_padova bash -c "python3 manage.py makemigrations; python3 manage.py migrate"
```

Create python [interpreter](https://www.jetbrains.com/help/pycharm/using-docker-compose-as-a-remote-interpreter.html?_ga=2.113029511.2074599546.1573637729-943915304.1573220787#debug) with the docker composer  

Create run configuration using the python interpreter



Eventually, to update the project when introducing changes in the code:
```bash
docker-compose build
```


### Note on CUDA enabled systems
As this project detects when a compatible GPU is present in the system and tries to use it, please add a 
```CUDA_VISIBLE_DEVICES=0``` flag as an environment variable if you encounter problems.


## Contributors
- [@stebranchi](https://github.com/stebranchi) Stefano Branchi
- [@dfmchiara](https://github.com/dfmchiara) Chiara Di Francescomarino 
- [@TKasekamp](https://github.com/TKasekamp) Tõnis Kasekamp 
- [@fmmaggi](https://github.com/fmmaggi) Fabrizio Maggi
- [@WilliamsRizzi](https://github.com/WilliamsRizzi) Williams Rizzi
- [@HitLuca](https://github.com/HitLuca) Luca Simonetto
