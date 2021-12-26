from flask import Flask,render_template,request,send_from_directory
from PIL import Image, ImageOps
import numpy as np
import keras

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './images/uploads/'
my_model = keras.models.load_model("./model_save.hdf5")
li = ['Apple', 'Carambola', 'Plum', 'Tomatoes']

@app.route("/", methods=["GET"])
def index():
    # return render_template('index.html')
    return render_template('index.html')

@app.route("/", methods=["POST"])
def predict():
    imageFile = request.files['imageFile']
    image_path = "./images/uploads/" + imageFile.filename
    imageFile.save(image_path)

    size= (150,150)
    image = Image.open(image_path)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image = np.asarray(image)
    image = np.expand_dims(image,axis=0)
    image = image/255
    prediction = my_model.predict(image)
    prediction = np.argmax(prediction)
    className = li[prediction]
    # className = "Apple"
    return render_template('index.html', uploaded_image=imageFile.filename , prediction=className)

@app.route('/display/<filename>')
def send_uploaded_image(filename=''):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == "__main__":
    app.run()