#!/usr/bin/env/python3

from flask import Flask, render_template, request, send_file, redirect, url_for, Response, redirect

app = Flask(__name__)

import sys
import os


@app.route('/', methods=['GET', 'POST'])
def menu():
    if request.form:
        print()
    monstres=[]
    return render_template("index.html", monstres=monstres)
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8001)

