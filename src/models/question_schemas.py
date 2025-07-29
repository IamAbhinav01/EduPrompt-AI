from typing import List
from pydantic import BaseModel, Field, field_validator

class MCQQuestion(BaseModel):
    """A class used to represent a Multiple Choice Question."""
    question: str = Field(description="The question text")
    options: List[str] = Field(description="List of options for the question")
    correct_answer: str = Field(description="The correct answer from the options")

    @field_validator('question', mode='before')
    def clean_question(cls, v):
        if isinstance(v, dict):
            return v.get('description', str(v))
        return str(v)


class FillBlankQuestion(BaseModel):
    """A class used to represent a Fill in the blanks Question."""
    question: str = Field(description="The question text with '____'")
    correct_answer: str = Field(description="The correct answer for the blank")

    @field_validator('question', mode='before')
    def clean_question(cls, v):
        if isinstance(v, dict):
            return v.get('description', str(v))
        return str(v)

class TrueFalseQuestions(BaseModel):
    """A class used to represent a True or False Question."""
    statement: str = Field(description="A factual statement to be judged true or false")
    answer: str = Field(description="Either 'True' or 'False' as the correct answer")

    @field_validator('statement', mode='before')
    def clean_statement(cls, v):
        if isinstance(v, dict):
            return v.get('description', str(v))
        return str(v)

    @field_validator('answer')
    def validate_answer(cls, v):
        if v not in ("True", "False"):
            raise ValueError("Answer must be either 'True' or 'False'")
        return v