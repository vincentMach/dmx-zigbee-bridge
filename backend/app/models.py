from sqlmodel import SQLModel, Field
from typing import Optional

class Scene(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    mappings: str  # JSON serialized mappings
