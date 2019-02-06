from lab3_code import*
from flask import Flask

#Set up application
app=Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to the banking application!</h>'
#Routes
@app.route('/bank/<bankname>')
def weclome_bank(bankname):
    bank=Bank(bankname,Currency)
    return '<h1>Welcome to {}!<h1>'.format(bank.name)

@app.route('/dollar/<amt>')
def showdollar(amt):
    dollar=Dollar(int(amt))
    return "{}".format(dollar)

@app.route('/yuan/<amt>')
def showyuan(amt):
    yuan=Yuan(int(amt))
    return '{}'.format(yuan)

@app.route('/pound/<amt>')
def showpound(amt):
    pound=Pound(int(amt))
    return "{}".format(pound)

@app.route('/bank/<bankname>/<currency>/<amt>')
def finalbank(bankname, currency, amt):
    if currency=="dollar":
        currency= Dollar
    elif currency=="pound":
        currency=Pound
    elif currency == "yuan":
        currency=Yuan
    else:
        return "invalid input for bank"
    final=Bank(bankname, currency, int(amt))
    return "Welcome to the {} bank! {}".format(final.name, final)


if __name__ == '__main__':
    app.run()
