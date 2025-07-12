from sqlmodel import SQLModel, create_engine

engine = create_engine("sqlite:///./dmx_zigbee.db")

def init_db():
    from app.models import Scene
    SQLModel.metadata.create_all(engine)
