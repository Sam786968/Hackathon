from flask import Flask, render_template
from main import *
app =Flask(__name__)

@app.route('/')
def index():
    quote = print_random_quote()
    return render_template('index.html', quote=quote)

if __name__=='__main__':
    app.run()
    
    
def print_random_quote():
    with open('quotes.json') as f:
        data=json.load(f)
    quote=random.choice(data['quotes'])['text']
    print(quote)

    threading.Timer(10, print_random_quote).start()