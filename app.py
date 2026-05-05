from flask import Flask, jsonify

app = Flask(__name__)

todos = []

@app.route('/')
def home():
    return jsonify({"message": "Todo App is running!", "todos": todos})

@app.route('/add/<item>')
def add_todo(item):
    todos.append(item)
    return jsonify({"message": f"Added: {item}", "todos": todos})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)