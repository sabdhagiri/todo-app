from flask import Flask, request, session, g, redirect, url_for, render_template, abort, flash, jsonify
import sqlite3

# Configuration

DATABASE='flaskr.db'
DEBUG = True
SECRET_KEY = 'secret'
USERNAME = 'admin'
PASSWORD = 'password'


app = Flask(__name__)
app.config.from_object(__name__)

if __name__ == '__main__':
    app.run()
