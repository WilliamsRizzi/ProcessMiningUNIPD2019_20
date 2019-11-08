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

## Running in a new environment
The docker build is available @ https://hub.docker.com/r/nirdizatiresearch/predict-python/ in any case if you prefer to setup your environment on your own you can refer the [Dockerfile](Dockerfile).

## Docker Compose

On first run to setup the database, you can run:
```commandline
docker-compose run progetto_padova python manage.py migrate
```

To run the project:
```commandline
docker-compose up progetto_padova
```

To update the project when introducing changes in the code:
```commandline
docker-compose build
```

## Run an instance of the project
If you are familiar with docker-compose the [docker-compose](docker-compose.yml) file is available, otherwise if you use PyCharm as IDE run the provided configurations.

Finally, from the command line you can use the following sample commands to interact with our software.

Start server with
```commandline
python manage.py runserver
```

Run tests with one of the following
```commandline
python manage.py test
./manage.py test
```

NB: always run a redis-server in background if you want your server to accept any incoming post requests!

Start by running migrations and adding sample data
```commandline
python manage.py migrate
python manage.py loaddata <your_file.json>
```

### Note on CUDA enabled systems
As this project detects when a compatible GPU is present in the system and tries to use it, please add a 
```CUDA_VISIBLE_DEVICES=0``` flag as an environment variable if you encounter problems.


## Contributors
- [@stebranchi](https://github.com/stebranchi) Stefano Branchi
- [@dfmchiara](https://github.com/dfmchiara) Chiara Di Francescomarino 
- [@TKasekamp](https://github.com/TKasekamp) Tõnis Kasekamp 
- [@mrsonuk](https://github.com/mrsonuk) Santosh Kumar
- [@fmmaggi](https://github.com/fmmaggi) Fabrizio Maggi
- [@WilliamsRizzi](https://github.com/WilliamsRizzi) Williams Rizzi
- [@HitLuca](https://github.com/HitLuca) Luca Simonetto
