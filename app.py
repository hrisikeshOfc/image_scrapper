from flask import Flask, jsonify, render_template, request, send_file
from scrapper import ImageScraper
from utils import SendZipOutput
import os
from logger import logging as lg

app = Flask(__name__)

@app.route("/")
def home():
    lg.info("home page is accessed.")
    return render_template("index.html")
    
@app.route('/scrape', methods=['POST'])
def scrape():
    try:
        search_input = str(request.form['search_input'])
        num_images = int(request.form['num_images'])
        lg.info("got user inputs")
        
        scrapper = ImageScraper(search_input= search_input)
        scrapper.scrape_images(num_images= num_images)
        lg.info("downloded photos")

        #let's zip the downloaded images folder
        zip = SendZipOutput(search_input)
        zip.makezip() 

        zip_file = f"{search_input}.zip"
        return send_file(zip_file)
    
    except Exception as e:
        lg.error(e)
        return jsonify(e)


@app.route("/log")
def return_log():
    return send_file(os.path.join("logs","app.log"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)