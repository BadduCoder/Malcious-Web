from flask import Flask, request, render_template
from test import main
from train import train_me
import urllib

app = Flask(__name__ , template_folder="Extension")

@app.route("/")
def home():
    return render_template("popup.html")

@app.route("/check/", methods=['POST'])
def check_url():
    url = request.form.get("url")
    print(url)
    try:
        urllib.urlretrieve(url, "markup.txt")
    except:
        return "PHISHING"
    print("In Here")
    prediction =  main(url)

    return render_template('predict.html',predict=prediction)
    
@app.route("/train/", methods=['GET'])
def train_model():
    return train_me()
    
if __name__ == "__main__":
    app.run(debug=True)