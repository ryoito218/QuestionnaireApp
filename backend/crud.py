from sqlalchemy.orm import Session
from . import models, schemas

def create_content(db: Session, content: schemas.ContentBase):
    db_content = models.Content(
        name=content.name,
        age=content.age,
        residence1=content.residence1,
        residence2=content.residence2,
        allergy=content.allergy,
        howtoeat=content.howtoeat,
        brand=content.brand,
        comment=content.comment,
        umamiA=content.umamiA,
        umamiB=content.umamiB,
        sweetA=content.sweetA,
        sweetB=content.sweetB,
        bitterA=content.bitterA,
        bitterB=content.bitterB,
        sourA=content.sourA,
        sourB=content.sourB,
        saltyA=content.saltyA,
        saltyB=content.saltyB,
        astringencyA=content.astringencyA,
        astringencyB=content.astringencyB,
        shakishakiA=content.shakishakiA,
        shakishakiB=content.shakishakiB,
        fuwafuwaA=content.fuwafuwaA,
        fuwafuwaB=content.fuwafuwaB,
        peelfirmnessA=content.peelfirmnessA,
        peelfirmnessB=content.peelfirmnessB,
        pulpfirmnessA=content.pulpfirmnessA,
        pulpfirmnessB=content.pulpfirmnessB,
    )
    db.add(db_content)
    db.commit()
    db.refresh(db_content)
    return db_content