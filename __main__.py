import unittest

from flask import Flask

from routes.characters_routes import character_blueprint

app = Flask(__name__)
app.register_blueprint(character_blueprint)

if __name__ == "__main__":
     app.run(debug=True, port=8080)
     #unittest.main()