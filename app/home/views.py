from . import home #导入蓝图对象

@home.route('/')
def index():
    return "<h1 style='color:green'>this is home</h1>"