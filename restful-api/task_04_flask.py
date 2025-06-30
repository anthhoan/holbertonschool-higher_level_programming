from flask import Flask
from flask import request
from flask import jsonify
from flask import abort
import requests
import threading
import time


app = Flask(__name__)
users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"name": "John", "age": 30, "city": "New York"}
}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def data():
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    return jsonify({"status": "OK"})

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        abort(404)

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    if not data or 'username' not in data or 'name' not in data:
        abort(400, description="Invalid input: 'username' and 'name' are required")

    username = data['username']
    if username in users:
        abort(400, description="User already exists")

    users[username] = {
        "name": data['name'],
        "age": data.get('age', 0),
        "city": data.get('city', "Unknown")
    }

    return jsonify({"message": "User added succesfully!", "user": users[username]}), 201

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "404 Not Found", "message": "Endpoint not found."}), 404

def run_server():
    app.run(host="localhost", port=5000)

def run_tests():
    time.sleep(1)
    test_home()
    test_data()
    test_status()
    test_add_user()
    test_get_user()
    print("All tests completed.")

def test_home():
    response = requests.get("http://localhost:5000/")
    assert response.status_code == 200
    assert response.text == "Welcome to the Flask API!"

def test_data():
    response = requests.get("http://localhost:5000/data")
    assert response.status_code == 200
    assert response.json() == ["jane", "john"]

def test_status():
    response = requests.get("http://localhost:5000/status")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}

def test_add_user():
    user_data = {"username": "bob", "name": "Bob", "age": 32, "city": "Seattle"}
    response = requests.post("http://localhost:5000/add_user", json=user_data)

    if response.status_code == 201:
        assert response.json()["user"]["name"] == "Bob"
    elif response.status_code == 400:
        print("User already exists or invalid input.")
    else:
        print(f"Unexpected status code: {response.status_code}")

def test_get_user():
    response = requests.get("http://localhost:5000/users/bob")
    assert response.status_code == 200
    assert response.json() == {"name": "Bob", "age": 32, "city": "Seattle"}

if __name__ == "__main__":
    server_thread = threading.Thread(target=run_server)
    server_thread.start()
    try:
        run_tests()
    finally:
        pass
    server_thread.join()