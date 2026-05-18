from music_box.database.base import Base
from music_box.database.session import engine

Base.metadata.create_all(bind=engine)
print("DB migrated")
