from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from music_box.database.base import Base


class Track(Base):
    __tablename__ = "tracks"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
