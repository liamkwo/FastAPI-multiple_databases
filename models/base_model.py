import arrow
from sqlalchemy import Column, Integer, DateTime


def kst_now():
    return arrow.utcnow().to("+09:00")


class ModelBase:
    id = Column(Integer, primary_key=True, autoincrement=True)
    updated_at = Column(DateTime(True))
    created_at = Column(DateTime(timezone=True), nullable=False, default=kst_now)

    def to_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
