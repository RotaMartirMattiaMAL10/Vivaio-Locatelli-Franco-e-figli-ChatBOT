from pydantic import BaseModel

class ClienteContext(BaseModel):
    name: str
    email: str
    phone: str
    address: str
    subscription_date: str
