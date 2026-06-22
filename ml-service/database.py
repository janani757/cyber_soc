import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):

    # =========================
    # GET DATABASE URL
    # =========================
    db_url = os.getenv("DATABASE_URL")

    # =========================
    # FALLBACK (LOCAL RUN SAFE)
    # =========================
    if not db_url:
        db_url = "sqlite:///soc.db"

    # =========================
    # FIX FOR RENDER POSTGRES
    # =========================
    if db_url.startswith("postgres://"):
        db_url = db_url.replace("postgres://", "postgresql://")

    # =========================
    # APPLY CONFIG
    # =========================
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()