from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
import os

app = Flask(__name__)

# Файл для хранения данных
DATA_FILE = 'tag_data.json'

# Инициализация данных, если файла нет
def init_data():
    if not os.path.exists(DATA_FILE):
        default_data = {
            "tags": [
                {"name": "Link1", "url": "https://Link1.com", "clicks": 10},
                {"name": "Link2", "url": "https://Link2.com", "clicks": 8},
                {"name": "Link3", "url": "https://Link3.com", "clicks": 15},
                {"name": "Link4", "url": "https://Link4.com", "clicks": 5},
                {"name": "Link5", "url": "https://Link5.com", "clicks": 12},
                {"name": "Link6", "url": "https://Link1.com", "clicks": 7}
            ]
        }
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(default_data, f, ensure_ascii=False, indent=2)

# Загрузка данных
def load_data():
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

# Сохранение данных
def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# Обновление счётчика кликов
def update_click(tag_name):
    data = load_data()
    for tag in data['tags']:
        if tag['name'] == tag_name:
            tag['clicks'] += 1
            break
    save_data(data)
    return tag['url']  # Возвращаем URL для перенаправления

@app.route('/')
def index():
    init_data()
    data = load_data()
    return render_template('index.html', tags=data['tags'])

@app.route('/click/<tag_name>')
def handle_click(tag_name):
    url = update_click(tag_name)
    return redirect(url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011, debug=True)
