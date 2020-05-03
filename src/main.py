from flask import Flask, request, jsonify
import numpy as np
import json
from deeplearning.ch08.dl import DL
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>mnist deeplearning backend</h1>"

@app.route('/__version__')
def version():
    import sys
    import flask,gunicorn,gevent
    return '<h1>Env</h1><p>numpy: %s</p><p>python: %s</p><p>flask: %s</p><p>gunicorn: %s</p><p>gevent: %s</p>' % (np.__version__, sys.version,flask.__version__,gunicorn.__version__,gevent.__version__)


@app.route('/v1/guess', methods=['POST'])
def guess():
    data = request.get_data()
    data_json = json.loads(data)
    filepath = os.path.split(os.path.realpath(__file__))[0]+'/deeplearning/ch08/deep_convnet_params.pkl'
    
    input = data_json['input']
    input_np = np.array(input)
    input_np = input_np.reshape((1,1,28,28)) # 转换类型
    
    dl = DL(filepath=filepath)
    y,softmax_result = dl.predict(input_np)
    # 组装数据
    c = [{"index": index, "value": format(value, '.5f')}
         for index,value in enumerate(softmax_result[0])]

    result = {
        "code": 1,
        "data": {
            "number": format(y[0],'0.1f'),  # 找出最大值所在的索引
            "softmax_result": c
        }
    }
    return jsonify(result)


# 启动服务器
if __name__ == '__main__':
    print("running...")
    app.run(debug=~True,host="0.0.0.0",port="5000")
