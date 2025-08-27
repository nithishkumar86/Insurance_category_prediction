from pydantic import BaseModel,Field,computed_field
from typing_extensions import TypedDict,Annotated,Literal


class InputBody(BaseModel):
    age:Annotated[int,Field(...,gt=0,le=120,description="the user age")]
    weight:Annotated[int,Field(...,gt=0,description="user weight")]
    height:Annotated[float,Field(...,gt=0,le=2.5,description="user height")]
    income_lpa:Annotated[float,Field(...,gt=0,description="user annual_income_lpa")]
    smoker:Annotated[bool,Field(...,description="whether the user is smoker or not")]
    occupation:Annotated[Literal['freelances', 'retired', 'private_job', 'student',
       'buisness_owner', 'government_job', 'unemployed'],Field(...,description="the user occupation")]
    
    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight/(self.height**2)
    
    @computed_field
    @property
    def age_group(self)->str:
        if self.age < 25:
            return "youth"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        else:
            return "senior"
        
    @computed_field
    @property
    def lifestyle_risk(self)->str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"
        
