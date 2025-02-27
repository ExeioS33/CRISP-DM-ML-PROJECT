# Dockerfile

# 1) Use the Jupyter SciPy Notebook base image
FROM quay.io/jupyter/scipy-notebook:2025-01-20

# 2) Set the working directory inside the container
WORKDIR /home/jovyan/work

# 3) Install the required libraries for API + joblib if needed
RUN pip install --no-cache-dir fastapi uvicorn 

# 4) Copy model and source code
COPY models/RandomForest_20250129_154514.pkl ./
COPY app/src/ src/

# 5) Expose the FastAPI port
EXPOSE 8000

# 6) Define the command to run FastAPI
CMD ["uvicorn", "app.src.main:app", "--host", "0.0.0.0", "--port", "8000"]
