# Import flask and classes
from flask import Flask
from lab3_code import Currency, Dollar, Yuan, Pound, Bank

# Set up application
app = Flask(__name__)

# Routes
@app.route('/')
def basic():
    return 'Welcome to the banking system!'

@app.route('/bank/<name>')
def show_bank_name(name):
    b_inst = Bank(name, Dollar)
    return "Welcome to {}!".format(b_inst.name)

@app.route('/dollar/<amt>')
def show_dollar(amt):
    d_inst = Dollar(int(amt))
    return d_inst.__str__()

@app.route('/yuan/<amt>')
def show_yuan(amt):
    y_inst = Yuan(int(amt))
    return y_inst.__str__()

@app.route('/pound/<amt>')
def show_pounds(amt):
    p_inst = Pound(int(amt))
    return p_inst.__str__()

@app.route('/bank/<name>/<currency>/<value>')
def show_message(name, currency, value):

    if currency == "Dollar":
        c_inst = Dollar
    elif currency == "Yuan":
        c_inst = Yuan
    elif currency == "Pound":
        c_inst = Pound
    else:
        return "Invalid URL inputs for bank"

    b_inst = Bank(name, c_inst, int(value))
    return b_inst.__str__()

if __name__ == "__main__":
    app.run()
