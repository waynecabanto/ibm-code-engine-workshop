FROM python:3.10-slim

# Create app directory & set default dir so that next commands executes in /usr/app dir, liked cd-ing into /usr/app to execute npm install
WORKDIR /usr/app

# Copy app files from src directory
COPY main.py .

# Install app dependencies
RUN pip install fastapi uvicorn

# Start the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
