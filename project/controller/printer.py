import os
from werkzeug.utils import secure_filename
from project import app
from project.models.calculate_Similarity import calculate_Similarity
from flask import render_template, request, redirect, url_for




# filename Initialize
global filename
filename = "images/cctv.jpeg"

# Index
@app.route('/', methods=['GET'])
def start():
    global img

    return render_template('index.html',
                           filename=filename)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/test', methods=['POST'])
def test():
    global img
    if request.method == 'POST':
        print(request.data)
        name = request.data.decode('utf-8')



    return render_template('error.html',
                           oing=name)





# File upload
@app.route('/uploadFile', methods= [ 'POST'])
def upload_file():
    global filename
    if request.method == 'POST':
        print( request.files)
        if 'test' not in request.files:
            print( 'No file part')
            return redirect( request.url)
        file = request.files['test']
        print(file)
        if file.filename == '':
            print('No Selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            print('File allowed')
            filename = "images/" + secure_filename(file.filename)
            img = os.path.join(app.config['UPLOAD_FOLDER']  , filename)
            file.save(img)


            # models.calculate_Similarity
            print(calculate_Similarity( img))


            # if 처음 등장 "new"
            # 이미 등장했던 사람 "already"

            return "new"

        return render_template('error.html')