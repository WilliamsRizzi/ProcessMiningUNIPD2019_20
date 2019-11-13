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

## Docker Compose

On first run to setup the database, you can run:
```bash
docker-compose up -d db
docker-compose run progetto_padova python3 manage.py migrate
```



To run the project:
```commandline
docker-compose up progetto_padova
```

To update the project when introducing changes in the code:
```commandline
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
