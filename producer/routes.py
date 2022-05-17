from typing import List
from fastapi import APIRouter, BackgroundTasks

from producer.db import SessionLocal
from producer.schema import EmailSchema
from producer.models import Emails
from producer.producers import send_mail_to_broker

router = APIRouter()

db = SessionLocal()


@router.get('/')
def get_all_emails() -> List[Emails]:
    return db.query(Emails).all()


@router.post('/send')
def send(item: EmailSchema, bgtask: BackgroundTasks) -> EmailSchema:
    new_mail = Emails(email=item.email, message=item.message)
    bgtask.add_task(send_mail_to_broker, item.email, item.message)
    db.add(new_mail)
    db.commit()
    db.refresh(new_mail)

    return new_mail
