
from flask import Flask, request, render_template
import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
import read_files_start_yolo
import plot_from_txt

PEOPLE_FOLDER = os.path.join('static','people_photo')

app = Flask(__name__, static_url_path="/static")
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER


@app.route("/")
def my_form():
    return render_template("my-form.html")


@app.route("/", methods=['POST'])
def my_form_post():
    dir_name = request.form['text']
    # dir_name = '/media/mynewdrive/data/Retail_AI/3DPeS/small_video_set_1'
    file_name = read_files_start_yolo.trigger_yolo(dir_name)
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
    return render_template('index.html', user_image=full_filename)


# def return_dataframe():
    # dir_name = "project_files/small_video_set_1"
    # df = getfiles.print_file_list(dir_name)
    # return render_template('view.html', tables=[df.to_html(classes='data')], titles=df.columns.values)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
