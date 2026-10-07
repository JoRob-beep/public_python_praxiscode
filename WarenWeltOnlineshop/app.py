from flask import Flask, render_template, request, redirect, url_for, session
from waitress import serve

app = Flask(__name__)
app.secret_key = 'dein_geheimer_schlüssel'  # Für Sessions

# Beispiel-Benutzerdaten
USERNAME = 'admin'
PASSWORD = 'geheim'

@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/home")
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login'), logout_text="Logout")


@app.route("/buecher")
def buecher():
    return render_template("buecher.html", logout_text="Logout")

@app.route("/elektronik")
def elektronik():
    return render_template("elektronik.html", logout_text="Logout")

@app.route("/kleidung")
def kleidung():
    return render_template("kleidung.html", logout_text="Logout")

@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            session['username'] = request.form['username']
            return redirect(url_for('home'))
        else:
            error = 'Falscher Benutzername oder Passwort'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('username', None)
    text = "Logout"
    return redirect(url_for('login'))

@app.route("/registrierung")
def registrierung():
    return render_template("registrierung.html", logout_text="Logout")

@app.route("/warenkorb")
def warenkorb():
    return render_template("warenkorb.html", logout_text="Logout")

@app.route("/after_reg")
def after_reg():
    return render_template("after_reg.html", logout_text="Logout")



if __name__ == "__main__":
    app.run(debug=True)

