from . import home #导入蓝图对象
from flask import render_template

@home.route('/')
def index():
    return render_template('home/index.html')