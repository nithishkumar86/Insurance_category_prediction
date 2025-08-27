from pydantic import BaseModel,Field
from typing_extensions import Annotated,TypedDict

class ResponseBody(BaseModel):
    predicted_category:str=Field(...,description="predicted category",examples=['High'])

    confidence:float=Field(...,description="confidence score range (0 to 1)",examples=[0.34])

    class_probabilities:dict[str,float]=Field(...,description="probability distribution accross all possible categories",examples=[{'high':0.45,"medium":3.45,"low":3.23}])

