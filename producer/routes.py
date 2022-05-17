from typing import List
from fastapi import APIRouter, BackgroundTasks

from producer.db import SessionLocal
from producer.schema import EmailSchema
from producer.models import Emails

router = APIRouter()

db = SessionLocal()


@router.get('/')
def get_all_emails() -> List[Emails]:
    return db.query(Emails).all()
