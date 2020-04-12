from flask import Flask
import yolo_getfiles # this will be your file name; minus the `.py`

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello World"

@app.route("/printfilelist")
def printfilelist():
    return yolo_getfiles.printfilelist('/media/mynewdrive/data/Retail_AI/3DPeS/Video_Set_1')

if __name__ == '__main__':
    app.run(debug=True)