FROM python:3.9-slim
WORKDIR /app

COPY . /app

# Install Chrome and Chromedriver dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Download and install Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update && apt-get install -y google-chrome-stable

RUN pip install -r requirements.txt

# Install additional dependencies for running Chrome headless
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libfontconfig1


# Copy the rest of the code to the container
COPY . /app/

# Set environment variables for Chromedriver and Chrome options
ENV CHROME_BINARY_PATH=/usr/bin/google-chrome
ENV CHROME_OPTIONS="--no-sandbox --disable-dev-shm-usage"

# Run your Python script or application
CMD ["python", "app.py"]
