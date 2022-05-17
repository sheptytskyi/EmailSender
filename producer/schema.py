from pydantic import BaseModel, EmailStr


class EmailSchema(BaseModel):
    """ Email Schema.
    fields: email: EmailStr,
            message: str"""
    email: EmailStr
    message: str
