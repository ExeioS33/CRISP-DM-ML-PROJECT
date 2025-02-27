docker run -it --rm -p 8888:8888 -v "${PWD}":/home/jovyan/work quay.io/jupyter/scipy-notebook:2025-01-20

echo ${PWD}

docker build -t heart-disease-api .

docker run -it --rm -p 8000:8000 -v "${PWD}":/home/jovyan/work heart-disease-api
docker run -it --rm -p 8000:8000 -v "${PWD}":/home/jovyan/work heart-disease-api /bin/bash

curl -X POST "http://127.0.0.1:8000/predict" \
 -H 'Content-Type: application/json' \
 -d '{"num_patients": 10}' > response.json
