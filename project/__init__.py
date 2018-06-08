# -*- coding: utf-8 -*-

__version__ = '0.1'

import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename



UPLOAD_FOLDER = os.path.join('project', 'static')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','bmp'])

app = Flask('project')
app.config['SECRET_KEY'] ='random'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS
import project.models
import project.controller
