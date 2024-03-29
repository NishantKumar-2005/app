# SecureXpert Backend

SecureXpert Backend is a Flask application designed to conduct device scans for identifying open ports and assessing vulnerabilities. It utilizes various functionalities to provide users with detailed reports on the status of their devices' security.

## 📚 Table of Contents

1. [SecureXpert Backend](#securexpert-backend)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Getting Started](#getting-started)
5. [Usage](#usage)
6. [Deployment](#deployment)


🚀 **Features**

- **Scan**: Conduct scans on specified IP addresses to identify open ports.
- **Service Version Detection**: Utilize socket connections to determine service versions running on open ports.
- **Vulnerability Assessment**: Use searchsploit tool to search for known vulnerabilities associated with detected service versions.
- **API Endpoint**: Expose a `/scan` endpoint to receive scan requests and provide scan results.

🛠️ **Tech Stack**

- **Flask**: Framework for building web applications in Python.
- **Flask-CORS**: Extension for handling Cross-Origin Resource Sharing (CORS) in Flask applications.
- **Socket**: Library for socket programming to establish connections for service version detection.
- **Subprocess**: Module for spawning new processes, used here for executing searchsploit commands.

## Getting Started

To get started with SecureXpert Backend:

1. Clone the repository to your local machine.
2. Navigate to the project directory:

    ```bash
    cd securexpert-backend
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Start the Flask server:

    ```bash
    python app.py
    ```

## Usage

Make POST requests to the `/scan` endpoint with JSON data containing the IP address and optionally the number of ports to scan. Receive JSON responses containing scan results including open ports, detected services, and associated vulnerabilities.

## Deployment

SecureXpert Backend can be easily deployed using Render.

1. Sign up for a Render account and create a new web service.
2. Configure the web service to use the appropriate deployment settings, ensuring it points to the correct repository and specifies the necessary environment variables.
3. Deploy the application to Render, and the service will automatically start running.

Here's a sample configuration for deploying with Render:

```yaml
# render.yaml
services:
  - name: securexpert-backend
    env: python
    buildCommand: python app.py
    routes:
      - type: http
        primary: true
```

