from flask import Flask
from src.routes import main_bp

app = Flask(__name__)

app.register_blueprint(main_bp)

if __name__ == '__main__':
    print("FlavorGraph Flask app - starting on http://0.0.0.0:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)
