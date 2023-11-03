# from flask import Flask, request
#
# app = Flask(__name__)
#
# @app.route('/', methods=['POST'])
# def handle_webhook():
#     if request.method == 'POST':
#         webhook_data = request.get_data().decode('utf-8')
#         print("Received webhook data:", webhook_data)
#         return "Webhook received successfully"
#
# if __name__ == '__main__':
#     app.run(port=80)



'''-----------------------'''
# import http.client
# from flask import Flask, request, Response
#
# conn = http.client.HTTPSConnection('eo5qh6612qgta49.m.pipedream.net')
# # JSON 형식의 데이터를 올바른 형태로 나타내기
# data = '''{
#   "test": "event"
# }'''
#
# # POST 요청 전송
# conn.request("POST", "/", data, {'Content-Type': 'application/json'})
#
# # 응답 받기
# res = conn.getresponse()
# print(res.read().decode())
'''---------------------------------'''
from flask import Flask, request, Response
import threading

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     print('Success!')
#     return 'Hello World!'

@app.route('/', methods=['GET', 'POST'])
def webhook():

    '''자동화 작업 함수'''
    def auto(content):
        print(content)

    if request.method == 'GET':
        content = request.args.to_dict()
    elif request.method == 'POST':
        if request.is_json is True:  # Content-Type: json
            content = request.get_json()
        else:  # Content-Type: x-www-form-urlencoded
            content = request.form.to_dict()

    '''스레드 실행'''
    thread = threading.Thread(target=auto, kwargs={'content': content})
    thread.start()

    return 'Hello World!'


if __name__ == '__main__':
    app.run(port=80, debug=True)
