
# 1: Base Python image
FROM python:3.10-slim

# 2: Create working directory inside the container
WORKDIR /app

# 3: Copy project files into the container
COPY . .

# 4: Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# 5: Expose the port for FastAPI (default is 8000)
EXPOSE 8000

# 6: Command to run the API with Uvicorn
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]