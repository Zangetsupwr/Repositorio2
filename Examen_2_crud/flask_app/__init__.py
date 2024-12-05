from flask import Flask, render_template, request, redirect, session
from dotenv import load_dotenv 
import os  

load_dotenv()

app = Flask(__name__) 
app.secret_key = os.getenv('APP_SECRET_KEY')
