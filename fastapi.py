from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

streamlit_app_url = "https://your-streamlit-app-url.com"  # Replace with your Streamlit app URL

@app.get("/redirect_to_streamlit")
def redirect_to_streamlit():
    return RedirectResponse(url=streamlit_app_url)



#!/bin/bash

# Start Streamlit app in the background
streamlit run /app/streamlit_app.py &

# Start FastAPI app
uvicorn fastapi_app:app --host 0.0.0.0 --port 8000


# Use a base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Install necessary dependencies
RUN pip install streamlit fastapi uvicorn

# Copy your Streamlit and FastAPI files into the container
COPY streamlit_app.py /app/streamlit_app.py
COPY fastapi_app.py /app/fastapi_app.py

# Copy the bash script
COPY start_services.sh /app/start_services.sh

# Expose ports
EXPOSE 8501 8000

# Give execute permissions to the script
RUN chmod +x /app/start_services.sh

# Start services using the script
CMD ["/bin/bash", "/app/start_services.sh"]


