from flask import Flask, render_template
import json
import random
import time
import threading

app= Flask(__name__)
@app.route('/')
def index():
    print("I got clicked!")

    return "Click."

if __name__ == '__main__':
    app.run(debug=True)