import uuid
from typing import List

from pydantic import BaseModel

from app.api.v1.endpoints.topping.schemas import ToppingBaseSchema


class PizzaTypeBaseSchema(BaseModel):
    name: str
    price: float
    description: str

    class Config:
        orm_mode = True


class PizzaTypeCreateSchema(PizzaTypeBaseSchema):
    dough_id: uuid.UUID
    sauce_ids: List[uuid.UUID]


class PizzaTypeSchema(PizzaTypeBaseSchema):
    id: uuid.UUID


class PizzaTypeToppingQuantityBaseSchema(BaseModel):
    quantity: int

    class Config:
        orm_mode = True


class PizzaTypeToppingQuantityCreateSchema(PizzaTypeToppingQuantityBaseSchema):
    topping_id: uuid.UUID


class PizzaTypeSauceSchema(BaseModel):
    sauce_id: uuid.UUID

    class Config:
        orm_mode = True


class JoinedPizzaTypeQuantitySchema(PizzaTypeBaseSchema, ToppingBaseSchema):
    pass
