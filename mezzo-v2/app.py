from flask import Flask, render_template, redirect, url_for
import json
import os
import stat

app = Flask(__name__)

DATA_FILE = 'tag_data.json'
FILE_PERMISSIONS = stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH

def init_data():
    if not os.path.exists(DATA_FILE):
        default_data = {
            "tags": [
                {"name": "Google", "url": "https://www.google.com/", "clicks": 10},
                {"name": "Сумма прописью 2 JS", "url": "https://leorodx.github.io/Amount-words-Mz_On-frontend/", "clicks": 8},
                {"name": "Playbook 2 WP", "url": "https://терре.рф/playbook/", "clicks": 15}
            ]
        }
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(default_data, f, ensure_ascii=False, indent=2)
        os.chmod(DATA_FILE, FILE_PERMISSIONS)

def load_data():
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.chmod(DATA_FILE, FILE_PERMISSIONS)

@app.route('/')
def index():
    init_data()
    data = load_data()
    return render_template('index.html', tags=data['tags'])

@app.route('/click/<tag_name>')
def handle_click(tag_name):
    data = load_data()
    for tag in data['tags']:
        if tag['name'] == tag_name:
            tag['clicks'] += 1
            save_data(data)
            # Открываем URL в новом окне после сохранения
            return f"""
            <script>
                window.open('{tag['url']}', '_blank');
                window.location.href = '/';
            </script>
            """
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5034, debug=True)
