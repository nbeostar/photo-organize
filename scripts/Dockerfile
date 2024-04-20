FROM python:3.13.0a6-slim

WORKDIR /usr/src/app
COPY src/* .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Create a group and user
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

# Switch to the non-root user
USER appuser

# Run app.py when the container launches
CMD ["python", "photo-organize.py","/src","/dest"]
