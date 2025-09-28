from pydantic import BaseModel,Field,computed_field,Field
from typing import Optional,Annotated,Literal
class UserInput(BaseModel):
    age: Annotated[int , Field(...,gt=0 ,description='Age of the user')]
    weight: Annotated[float,Field(...,gt=0,description='Weight of the user')]
    height: Annotated[float,Field(...,gt=0,description='Height of the user')]
    income_lpa:Annotated[float,Field(...,gt=0,description='Income of the user in lakh per annum')]
    smoker:Annotated[bool,Field(...,description='Whether the user is a smoker or not')]
    city: Annotated[str,Field(...,description='City of the user')]
    occupation: Annotated [Literal[ 'retired', '1','business_owner', 'student', 'government_job','unemployed', 'private_job'], Field(...,description='Occupation of the user')]

    @computed_field
    @property
    def bmi(self)->float:
        bmi=self.weight/(self.height**2)
        return round(bmi,2) 
    @computed_field
    @property
    def city_tier(self)->int:
        tier_1_cities=['Delhi','Mumbai','Chennai','Kolkata','Hyderabad']
        tier_2_cities=['Bengaluru','Pune','Ahmedabad','Surat','Jaipur']
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3
    @computed_field
    @property
    def age_group(self)-> str:
        if self.age <25:
            return 'young'
        elif self.age <45:
            return 'adult'
        elif self.age <60:
            return 'middle_aged'
        else:
            return 'senior'
    @computed_field
    @property
    def lifestyle_risk(self)->str:
        if self.smoker and self.bmi >30:
            return 'high'
        elif self.smoker and self.bmi >27:
            return 'medium'
        else:
            return 'low'