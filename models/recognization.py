from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class face_recognization(db.Model):
    person_id = db.Column(db.String(30), unique=False, nullable=False, primary_key=True)
    cam_id = db.Column(db.String(30), unique=False, nullable=False)
    photo = db.Column(db.String(30), unique=False, nullable=False)
    timestamp = db.Column(db.Integer)

    def to_dict(self, base_url):
        return {
            "personID": self.person_id if self.person_id else "",
            "camID": self.cam_id if self.cam_id else "",
            "photoUrl": base_url + 'static/' + self.photo if self.photo else "",
            "timeStamp": self.timestamp if self.timestamp else None
        }