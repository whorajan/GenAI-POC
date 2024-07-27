from pydantic import BaseModel

class testcaseRequestContext(BaseModel):
    requestKey : str
    requestBody : str