# abcd.com/webhookreq에 요청 들어온 그대로 콘솔에 출력
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/post_published', methods=['POST'])
def post_published():
    if request.method == 'POST':
        data = request.get_data(as_text=True)
        print(data)
        return f"Received message: {data}"
    return "Invalid method."

@app.route('/post_updated', methods=['POST'])
def post_updated():
    if request.method == 'POST':
        try:
            data = request.get_json()  # JSON 데이터를 딕셔너리로 변환
            post_url = data["post"]["current"]["url"]  # 받은 JSON 데이터를 딕셔너리로 출력
            print(post_url)
            # 텔레그램, 디스코드 전송 os.system(f'sendtele.exe "포스트 업데이트 {post_url}"')
            return ""
        except Exception as e:
            return jsonify({"error": "Invalid JSON data", "details": str(e)}), 400
    return ""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)