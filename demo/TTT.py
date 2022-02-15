import base64
from flask import request
from flask import Flask
import os

app = Flask(__name__)


# 定义路由
@app.route("/photo", methods=['POST'])
def get_frame():
    # 接收图片
    scan_num = request.form.get('scan_num')
    upload_file = request.files['front']
    upload_file1 = request.files['back']


    # 获取图片名
    file_name = upload_file.filename
    file_name1 = upload_file1.filename
    # 文件保存目录（桌面）
    file_path = r'./imgs'
    if upload_file and upload_file1:
        # 地址拼接
        file_paths = os.path.join(file_path, file_name)
        file_paths1 = os.path.join(file_path, file_name1)
        # 保存接收的图片到桌面
        upload_file.save(file_paths)
        upload_file1.save(file_paths1)
        return '1234124124'
        # 随便打开一张其他图片作为结果返回，
        # with open(r'C:/Users/Administrator/Desktop/1001.jpg', 'rb') as f:
        #     res = base64.b64encode(f.read())
        #     return res


if __name__ == "__main__":
    app.run(debug=True,host='192.168.0.115',port=5000)