from pydantic import BaseModel


class EmailStrucure(BaseModel):
    to: str
    subject: str
    message_text: str
