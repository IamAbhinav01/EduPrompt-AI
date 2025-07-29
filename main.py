import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from src.utils.helpers import *
from src.generator.question_generator import *

def main():
    st.set_page_config("🎓 EduPrompt AI",page_icon="🎓")
    
    if 'quiz_manager' not in st.session_state:
        st.session_state.quiz_manager = QuizzManager()

    if 'quiz_generated' not in st.session_state:
        st.session_state.quiz_generated = False

    if 'quiz_submitted' not in st.session_state:
        st.session_state.quiz_submitted = False
    
    if 'quiz_score' not in st.session_state:
        st.session_state.quiz_score = 0
    
    if 'rerun_trigger' not in st.session_state:
        st.session_state.rerun_trigger = False

    st.title("🎓 EduPrompt AI")

    st.sidebar.header("PROMPT SETTINGS")

    question_type = st.sidebar.selectbox(
        "Select question type",
        ["Multiple Choice", "Fill in the Blanks","True or False"],
        index=0
    )
    topic = st.sidebar.text_input("Enter the Topic",placeholder="DSA,OS,WEB DEVELOPMENT")
    difficulty = st.sidebar.selectbox(
        "Select difficulty level",
        ["Easy", "Medium", "Hard"],
        index = 1
    )
    num_questions = st.sidebar.number_input("Number of questions",min_value=1,max_value=40)

    if st.sidebar.button("Generate Quiz"):
        st.session_state.quiz_submitted = False
        generator = QuestionGenerator()
        success = st.session_state.quiz_manager.generate_question(
            generator,
            question_type=question_type,
            topic=topic,
            difficulty=difficulty,
            num_question=num_questions
        )
        st.session_state.quiz_generated = success
        rerun()
    if st.session_state.quiz_generated and st.session_state.quiz_manager.questions:
        st.write("Questions")
        st.session_state.quiz_manager.attempt_quiz()
        if st.button("Submit Answers"):
            st.session_state.quiz_manager.evaluate_quiz()
            st.session_state.quiz_submitted = True
            rerun()
    if st.session_state.quiz_submitted:
        st.write("Quiz Results")
        results_df = st.session_state.quiz_manager.generate_result_dataframe()
        if not results_df.empty:
            correct_count = results_df["is_correct"].sum()
            total_questions = len(results_df)
            score_percentage = (correct_count/total_questions)*100
            st.write(f"Quiz Score: {score_percentage:.2f}%")
            for i,j in results_df.iterrows():
                question_num = j['question_number']
                if j["is_correct"]:
                    st.success(f"👨‍🎓👨‍🎓 Question {question_num}:{j['question']}")
                else:
                    st.error(f"🤦‍♂️ Question {question_num}:{j['question']}")
                    st.write(f"Your answer : {j['user_answer']}")
                    st.write(f"Correct Answer : {j['correct_answer']}")

                st.markdown("🔚🔚🔚🔚🔚🔚🔚🔚🔚🔚🔚🔚🔚🔚🔚")

            if st.button("Save Results"):
                saved_file = st.session_state.quiz_manager.save_to_csv()
                if saved_file:
                    with open(saved_file,'rb') as f:
                        st.download_button(
                            label="Download Results CSV",
                            data=f.read(),
                            file_name=os.path.basename(saved_file),
                            mime='text/csv'
                        )
                else:
                    st.warning("No Results available")
if __name__=="__main__":
    main()