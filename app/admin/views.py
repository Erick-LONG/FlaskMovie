from . import admin  # 导入蓝图对象

@admin.route('/')
def index():
    return "<h1 style='color:red'>this is admin</h1>"
