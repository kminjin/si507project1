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

@app.route('/bank/<bankname>/<currency>/<value>')
def finalbank(bankname, currency, value):
    final=Bank(bankname,Currency)
    return '<h1>Welcome to the {} bank! {} <h1>'.format(final.name, final.__str__)



if __name__ == '__main__':
    app.run()
