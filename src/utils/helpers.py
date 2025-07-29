import os
from datetime import datetime
import streamlit as st
import pandas as pd
from src.generator.question_generator import QuestionGenerator



def rerun():
    st.session_state['rerun_trigger'] = not st.session_state.get('rerun_trigger',False)
class QuizzManager:
    def __init__(self):
        self.questions = []
        self.user_answer = []
        self.results = []
    def generate_question(self,generator:QuestionGenerator,topic:str,question_type:str,difficulty:str,num_question:int):
        self.questions = []
        self.user_answer = []
        self.results = []

        try:
            for i in range(num_question):
                if question_type == "Multiple Choice":
                    question = generator.generate_mcq(topic,difficulty.lower())

                    self.questions.append(
                        {
                            "type":"MCQ",
                            "question":question.question,
                            "options":question.options,
                            "correct_answer":question.correct_answer
                        }
                    )
                elif question_type == "Fill in the Blanks":
                    question = generator.generate_fill_blank(topic, difficulty.lower())
                    self.questions.append(
                        {
                            "type": "Fill in the Blanks",
                            "question": question.question,
                            "correct_answer": question.correct_answer
                        }
                    )
                else:
                    question = generator.generate_true_false(topic, difficulty.lower())
                    self.questions.append(
                        {
                            "type": "True or False",
                            "question": question.statement,
                            "correct_answer": question.answer
                        }
                    )
        except Exception as e:
            st.error(f"Error generating question {e}")
            return False
        return True
    

    def attempt_quiz(self):
        for i,q in enumerate(self.questions):
            st.markdown(f"**Question {i+1} : {q['question']}**")

            if q['type']=='MCQ':
                user_answer = st.radio(
                    f"Select and answer for Question {i+1}",
                    q['options'],
                    key = f"mcq_{i}"
                )
                self.user_answer.append(user_answer)
            elif q['type'] == 'Fill in the Blanks':
                user_answer = st.text_input(
                    f"Fill in the blanks for Question {i+1}",
                    key = f"fill_blank{i}"
                )
                self.user_answer.append(user_answer)
            else:
                user_answer = st.radio(
                f"True or False - Question {i+1}",
                ["True", "False"],
                key=f"true_false_{i}"
            )
            self.user_answer.append(user_answer)

    def evaluate_quiz(self):
        self.results=[]
        for i,(q,user_ans) in enumerate(zip(self.questions,self.user_answer)):
            result_dict = {
                'question_number':i+1,
                'question':q['question'],
                'question_type':q['type'],
                'user_answer':user_ans,
                'correct_answer':q['correct_answer'],
                "is_correct":False
            }
            if q['type']=='MCQ':
                result_dict['options'] = q['options']
                result_dict["is_correct"]=user_ans==q["correct_answer"]            
            elif q['type'] == 'Fill in the Blanks':
                result_dict['options'] = []
                result_dict["is_correct"]=user_ans.strip().lower()==q["correct_answer"].strip().lower()
            else:
                result_dict['options'] = ["True", "False"]
                result_dict["is_correct"] = user_ans.strip().lower() == q["correct_answer"].strip().lower()
            self.results.append(result_dict)
    def generate_result_dataframe(self):
        if not self.results:
            return pd.DataFrame()
        return pd.DataFrame(self.results)
    def save_to_csv(self,filename_prefix="quiz_results"):
        if not self.results:
            st.warning("No results to save!..")
            return None
        df = self.generate_result_dataframe()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        unique_filename = f"{filename_prefix}_{timestamp}.csv"
        os.makedirs('results',exist_ok=True)
        full_path = os.path.join('results',unique_filename)
        try:
            df.to_csv(full_path,index=False)
            st.success("Results saved successfully..!")
            return full_path
        except:
            st.warning("Failed to save results to csv!..")
            return None

        
