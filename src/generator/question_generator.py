from langchain.output_parsers import PydanticOutputParser
from src.models.question_schemas import FillBlankQuestion,MCQQuestion
from src.prompts.templates import mcq_prompt_template,fill_blank_prompt_template
from src.llm.groq_client import get_groq_llm
from src.config.settings import setting
from src.common.logger import get_logger
from src.common.common_exception import CustomException


class QuestionGenerator:
    def __init__(self):
        self.llm = get_groq_llm();
        self.logger = get_logger(self.__class__.__name__)     #we want to use logger with with class name question

    def _retry_and_parse(self,prompt,parser,topic,difficulty):
        for attempt in range(setting.MAX_RETRIES):
            try:
                self.logger.info(f"Generating question for topic {topic} with difficulty")
                response = self.llm.invoke(prompt.format(topic=topic,difficulty=difficulty))
                parsed = parser.parse(response.content)
                self.logger.info("Succcessfully parsed the question")
            except Exception as e:
                self.logger.error(f"Failed to generate question for topic {topic} with difficulty {difficulty}.")
                if attempt==setting.MAX_RETRIES-1:
                    raise CustomException(f"Failed to generate question for topic {topic} with difficulty {difficulty}.")   
                

    def generate_mcq(self,topic:str,difficulty:str='medium')->MCQQuestion:
        try:
            parser = PydanticOutputParser(pydantic_object=MCQQuestion)
            question = self._retry_and_parse(mcq_prompt_template,parser=parser,topic=topic,difficulty=difficulty)

            if len(question.options)!=4 or question.correct_answer not in question.options:
                raise CustomException("Generated question does not have 4 options or correct answer is not in options")
            self.logger.info("Generated a Valid MCQ Question")
            return question
        except Exception as e:
            self.logger.error(f"failed to generate mcq question for topic {topic} with difficulty {difficulty}")
            
                
    def generate_fill_blank(self,topic:str,difficulty:str='medium')->FillBlankQuestion:
        try:
            parser = PydanticOutputParser(pydantic_object=FillBlankQuestion)
            question = self._retry_and_parse(fill_blank_prompt_template,parser=parser,topic=topic,difficulty=difficulty)

            if "____" not in question.question:
                raise CustomException("Generated question does not have a '___' in the ")
            self.logger.info("Generated a Valid Fill in BlankQuestion")
            return question
        except Exception as e:
            self.logger.error(f"failed to generate Fill in Blank question for topic {topic} with difficulty {difficulty}")                              

