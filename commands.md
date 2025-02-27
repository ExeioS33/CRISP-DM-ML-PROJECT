# Launch jupyter environment for the ML part

```bash
# launch it in one shell and access the url on localhost in the logs
docker run -it --rm -p 8888:8888 -v "${PWD}":/home/jovyan/work quay.io/jupyter/scipy-notebook:2025-01-20
```

# build custom image with the REST service that exposes the model prediction

docker build -t heart-disease-api .

# run container for the prediction

```bash
docker run -it --rm -p 8000:8000 -v "${PWD}":/home/jovyan/work heart-disease-api
## DEBUG : enter the container
# docker run -it --rm -p 8000:8000 -v "${PWD}":/home/jovyan/work heart-disease-api /bin/bash
```

# Make random false prediction

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
 -H 'Content-Type: application/json' \
 -d '{"num_patients": 10}' > response.json
```
