from flask import Flask, jsonify, request


app = Flask(__name__)


mock_data = [

    {'question_id': 1, 'question_str': '会社のエレベーターが広くなったので、荷物の（ ）が便利になった。', 'question_choices': {1: '運搬', 2: '輸送', 3: '運送', 4: '運輸'}, 'question_answer': 1},
    {'question_id': 2, 'question_str': 'ケネディ殺害の容疑者は __ に謎を残したままマフィアに撃たれて死亡した。', 'question_choices': {1: '動機', 2: '本音', 3: '動力', 4: '下心'}, 'question_answer': 1},
    {'question_id': 3, 'question_str': 'いつ見つけても __ の早いがんでは予後が悪く、遅いがんは予後がいい。早くても遅くても意味はないのです。', 'question_choices': {1: '先進', 2: '増進', 3: '進出', 4: '進行'}, 'question_answer': 4}

]

@app.route('/', methods=['GET'])
def get_question():

    return jsonify(mock_data)


if __name__ == '__main__':
    app.run(port=5000)