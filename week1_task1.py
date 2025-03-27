from flask import Flask, request, redirect, render_template
import random
import string

app = Flask(__name__)

# In-memory key-value store
url_mapping = {}

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
        while short_code in url_mapping:
            short_code = generate_short_code()

        url_mapping[short_code] = long_url
        short_url = f"http://127.0.0.1:5000/{short_code}"

    return render_template("index.html", short_url=short_url)

@app.route('/<short_code>', methods=['GET'])
def redirect_to_long(short_code):
    long_url = url_mapping.get(short_code)

    if not long_url:
        return render_template("index.html", error="Short URL not found.")

    return redirect(long_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

