from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.adorama.com%2Falc%2Fwp-content%2Fuploads%2F2021%2F05%2Fbird-wings-flying-feature.gif&tbnid=Kz4be22T3oSCUM&vet=12ahUKEwiO9OOT-dv-AhVe23MBHQ7rCswQMygMegUIARChAg..i&imgrefurl=https%3A%2F%2Fwww.adorama.com%2Falc%2Fhow-to-make-an-animated-gif-in-photoshop%2F&docid=jc7mj51zTpC5oM&w=825&h=465&q=gifs%20images&ved=2ahUKEwiO9OOT-dv-AhVe23MBHQ7rCswQMygMegUIARChAg"
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
