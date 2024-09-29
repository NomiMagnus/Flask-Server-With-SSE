from flask import Flask, Response

import time

app = Flask(__name__)

def generate_time():
    while True:
        current_time = time.strftime('%H:%M:%S')
        yield f"Current Time: {current_time}\n\n"
        time.sleep(1)

@app.route('/time')
def events():
    return Response(generate_time(), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)