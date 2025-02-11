# Use Image Python
FROM python:3.10

# containar
WORKDIR /app

# Copy arch
COPY . /app

# install dependecies
RUN pip install --no-cache-dir -r requirements.txt

# port of FastAPI
EXPOSE 8000

# Execute App
CMD ["uvicorn", "controllers:app", "--host", "0.0.0.0", "--port", "8000"]
