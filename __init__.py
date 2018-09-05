from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object('test_labeling_app.config')
bootsrap = Bootstrap(app)

import test_labeling_app.views
