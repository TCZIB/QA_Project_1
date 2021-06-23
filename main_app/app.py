from sub_programs import app
from flask_sqlalchemy import SQLAlchemy
import os

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')