from flask import Flask, request, redirect, render_template
import random
import string
import redis
import os

# Get Redis host and port from environment variables
REDIS_HOST = os.getenv("REDIS_HOST", "redis")  # Use "redis" for Docker networking
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

app = Flask(__name__)

# Try connecting to Redis with error handling
try:
    redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    redis_client.ping()  # Check if Redis is reachable
except redis.ConnectionError:
    print("Error: Unable to connect to Redis. Make sure Redis is running.")

# Function to generate a random short URL identifier
def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/', methods=['GET', 'POST'])
def home():
    short_url = None

    if request.method == 'POST':
        long_url = request.form.get('long_url')

        if not long_url:
            return render_template("index.html", error="Please enter a valid URL.")

        # Generate a unique short code
        short_code = generate_short_code()

        # Ensure uniqueness
        while redis_client.exists(short_code):
            short_code = generate_short_code()

        redis_client.set(short_code, long_url)
        short_url = f"http://127.0.0.1:5000/{short_code}"

    return render_template("index.html", short_url=short_url)

@app.route('/<short_code>', methods=['GET'])
def redirect_to_long(short_code):
    long_url = redis_client.get(short_code)

    if not long_url:
        return render_template("index.html", error="Short URL not found.")

    return redirect(long_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

