import os
from werkzeug.utils import secure_filename
from project import app
from project.models.calculate_Similarity import calculate_Similarity, SIFT_detector
from flask import render_template, request, redirect, url_for


# filename Initialize
global filename
filename = "images/9.bmp"
tempImages = []
tempPercent = []
tests= []


# Index
@app.route('/', methods=['GET'])
def start():

    return render_template('index.html',
                           filename=filename, tempImages = tempImages)


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
    global tempImages
    global tempPercent
    #global tests
    if request.method == 'POST':
        print( request.files)
        if 'upfile' not in request.files:
            print( 'No file part')
            return redirect( request.url)
        file = request.files['upfile']
        if file.filename == '':
            print('No Selected file')
            return redirect(request.url)
        print(file.filename)

        if file and allowed_file(file.filename):
            tempImages = []
            tempPercent = []

            print('File allowed')
            filename = "images/" + secure_filename(file.filename)
            img = os.path.join(app.config['UPLOAD_FOLDER']  , filename)
            file.save(img)

            # models.calculate_Similarity
            for root, dirs, files in os.walk('project/static/images/'):
                for fname in files:
                    try:
                        full_fname = os.path.join(root, fname)
                        #full_fname = "project/static/images/" + fname
                        fileType = full_fname.split('.')[1]
                        if (fileType == "bmp"):
                            SIFT_detector(img, full_fname, fname)
                            diff = calculate_Similarity(img, full_fname)
                            #tempPercent.append( diff)
                            #tempImages.append(  "diff_images/diff_" + fname)
                            tempImages.append( {'diff':diff, 'path': "diff_images/diff_" + fname} )

                    except:
                        print("")

            tempImages= sorted( tempImages, key = lambda k : k['diff'])
            # if 처음 등장 "new"
            # 이미 등장했던 사람 "already"

            return "new"

        print("error")
        return render_template('error.html')