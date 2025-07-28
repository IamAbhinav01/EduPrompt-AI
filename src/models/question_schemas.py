from typing import List
from pydantic import BaseModel,Field,model_validator

class MCQQuestion(BaseModel):
    """A class used to represent a Multiple Choice Question."""
    question:str = Field(description="The question text")
    options: List[str] = Field(description="List of options for the question")
    correct_answer:str=Field(description="The correct answer from the option")

    @model_validator('question',pre=True)
    def clean_question(cls,v):
        if isinstance(v,dict):
            return v.get('description',str(v))
        return str(v)
    

class FillBlankQuestion(BaseModel):
    """A class used to represent a Fill in the blanks Question."""
    question:str = Field(description="The question text with '____")
    correct_answer:str=Field(description="The correct answer for the blank")

    @model_validator('question',pre=True)
    def clean_question(cls,v):
        if isinstance(v,dict):
            return v.get('description',str(v))
        return str(v)