from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Заглушка для функции анализа глагола
def analyze_verb(verb_form):
    # Здесь будет твоя реальная логика
    # Пока возвращаем тестовые данные
    return {
        'root': 'فعل',
        'features': {
            'время': 'dsf',
            'лицо': 'третье',
            'число': 'единственное',
            'род': 'мужской'
        }
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    verb_form = request.form['verb']
    result = analyze_verb(verb_form)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)