from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///./music_box.db", future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
