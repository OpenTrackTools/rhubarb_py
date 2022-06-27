from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_babel import Babel
from flask_caching import Cache
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt
from sqlalchemy import MetaData

curr_date = datetime.today().strftime('%Y%m%d')
metadata = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s_" + curr_date,
        "uq": "uq_%(table_name)s_%(column_0_name)s_" + curr_date,
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s_" + curr_date,
        "pk": "pk_%(table_name)s_" + curr_date,
    }
)

db = SQLAlchemy(metadata=metadata, session_options={"future": True})
babel = Babel()
mail = Mail()
cache = Cache()
csrf = CSRFProtect()
bcrypt = Bcrypt()
migrate = Migrate()
