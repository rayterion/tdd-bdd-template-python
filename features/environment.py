import threading
from wsgiref.simple_server import make_server
from selenium import webdriver
from src.core.website import app

def before_all(context):
    # Spin up the Flask app in a background daemon thread
    threading.Thread(
        target=lambda: make_server('127.0.0.1', 5000, app).serve_forever(), 
        daemon=True
    ).start()

    # Setup headless Chrome and base URL
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    context.browser = webdriver.Chrome(options=options)
    context.base_url = "http://127.0.0.1:5000"

def after_all(context):
    context.browser.quit()