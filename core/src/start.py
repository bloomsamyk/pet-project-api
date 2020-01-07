from flask import Flask
from controller import Controller

app = Flask(__name__)


@app.route('/')
def get_data():
    controller = Controller()
    return controller.get_data()


if __name__ == '__main__':
    app.run()

