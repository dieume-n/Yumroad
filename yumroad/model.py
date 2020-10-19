from datetime import datetime

from yumroad.extensions import db


class BaseModel(db.Model):
    __abstract__ = True

    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __save_to_db(self):
        db.session.add(self)
        db.session.commit()