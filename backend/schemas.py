from pydantic import BaseModel, Field
import datetime

class ContentBase(BaseModel):
    name: str = Field(max_length=20)
    age: int
    residence1: str
    residence2: str
    allergy: str
    howtoeat: str
    brand: str
    comment: str

    umamiA: int
    umamiB: int
    sweetA: int
    sweetB: int
    bitterA: int
    bitterB: int
    sourA: int
    sourB: int
    saltyA: int
    saltyB: int
    astringencyA: int
    astringencyB: int

    shakishakiA: int
    shakishakiB: int
    fuwafuwaA: int
    fuwafuwaB: int
    peelfirmnessA: int
    peelfirmnessB: int
    pulpfirmnessA: int
    pulpfirmnessB: int

class Content(ContentBase):
    content_id: int
    create_at: datetime.datetime

    class Config:
        orm_mode = True