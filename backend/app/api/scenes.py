from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models import Scene
from app.database import engine
from typing import List

router = APIRouter()

def get_session():
    with Session(engine) as session:
        yield session

@router.get("", response_model=List[Scene])
async def read_scenes(session: Session = Depends(get_session)):
    return session.exec(select(Scene)).all()

@router.post("", response_model=Scene)
async def create_scene(scene: Scene, session: Session = Depends(get_session)):
    session.add(scene)
    session.commit()
    session.refresh(scene)
    return scene

@router.put("/{scene_id}", response_model=Scene)
async def update_scene(scene_id: int, scene: Scene, session: Session = Depends(get_session)):
    db_scene = session.get(Scene, scene_id)
    if not db_scene:
        raise HTTPException(status_code=404, detail="Scene not found")
    db_scene.name = scene.name
    db_scene.mappings = scene.mappings
    session.add(db_scene)
    session.commit()
    session.refresh(db_scene)
    return db_scene

@router.delete("/{scene_id}")
async def delete_scene(scene_id: int, session: Session = Depends(get_session)):
    db_scene = session.get(Scene, scene_id)
    if not db_scene:
        raise HTTPException(status_code=404, detail="Scene not found")
    session.delete(db_scene)
    session.commit()
    return {"detail": "Deleted"}
