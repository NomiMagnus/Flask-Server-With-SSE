# Server-Sent Events (SSE) Time Display

This project demonstrates how to create a simple web application using Python with Flask to send Server-Sent Events (SSE) to a browser displaying the current time every second.

## Installation

1. Install Flask and Flask-SSE using pip:
   ```
   pip install Flask Flask-SSE
   ```

## Usage

1. Run the `sse_server.py` Python script:
   ```
   python sse_server.py
   ```

2. Access the SSE Time page in your web browser:
   Open a web browser and go to `http://127.0.0.1:5000/` to see the current time updating every second.

## How It Works

- The Python script uses Flask to create a web server and Flask-SSE to handle Server-Sent Events.
- The script generates the current time every second and sends it to the client using SSE.
- The HTML page subscribes to these events and updates the displayed time in real-time.

## Files

- `sse_server.py`: Python script containing the server-side code.
- `README.md`: This file providing instructions and information about the project.

## Dependencies

- Flask
- Flask-SSE

## References

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask-SSE Documentation](https://flask-sse.readthedocs.io/)
