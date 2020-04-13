from flask import Flask, request, render_template
import yolo_getfiles

app = Flask(__name__, static_url_path="/static")

@app.route("/")
def my_form():
	return render_template("my-form.html")

@app.route("/", methods=['POST'])
def my_form_post():
    dirname = request.form['text']
    return yolo_getfiles.printfilelist(dirname)
    # return yolo_getfiles.printfilelist('/media/mynewdrive/data/Retail_AI/3DPeS/small_video_set_1')
    # processed_text = text.upper()
    # return processed_text

# @app.route("/printfilelist")
# def printfilelist():
#     return yolo_getfiles.printfilelist('/media/mynewdrive/data/Retail_AI/3DPeS/small_video_set_1')

if __name__ == '__main__':
    app.run(debug=True)