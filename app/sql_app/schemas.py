from pydantic import BaseModel


class InfoBase(BaseModel):
    """
    Base model for user other infos
    """
    school: str | None = None
    company: str | None = None


class InfoCreate(InfoBase):
    """
    Create model for user other infos
    """
    pass


class Info(InfoBase):
    """
    info model
    """
    id: int
    owner_id: int

    class Config:  # provide configuration for the model
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    infos: list[Info] = []

    class Config:
        orm_mode = True