from langchain.prompts import PromptTemplate

mcq_prompt_template = PromptTemplate(
    template=(
        "Generate a {difficulty} multiple-choice question about {topic}.\n\n"
        "Return ONLY a JSON object with these exact fields:\n"
        "- 'question': A clear, specific question\n"
        "- 'options': An array of exactly 4 possible answers\n"
        "- 'correct_answer': One of the options that is the correct answer\n\n"
        "Example format:\n"
        '{{\n'
        '    "question": "What is the capital of France?",\n'
        '    "options": ["London", "Berlin", "Paris", "Madrid"],\n'
        '    "correct_answer": "Paris"\n'
        '}}\n\n'
        "Your response:"
    ),
    input_variables=["topic", "difficulty"]
)

fill_blank_prompt_template = PromptTemplate(
    template=(
        "You are an expert question generator.\n"
        "Generate a {difficulty} fill-in-the-blank question on the topic: {topic}.\n\n"
        "⚠️ Strict format instructions:\n"
        "- Return ONLY a JSON object with these exact fields:\n"
        "  • 'question': A grammatically correct sentence that contains exactly one blank using '_____'\n"
        "  • 'answer': The correct word or phrase that fills the blank\n"
        "- Do NOT add any explanation or commentary.\n\n"
        "✅ Example format:\n"
        '{{\n'
        '  "question": "The capital of France is _____.",\n'
        '  "answer": "Paris"\n'
        '}}\n\n'
        "Your response:"
    ),
    input_variables=["topic", "difficulty"]
)
true_false_prompt_template = PromptTemplate(
    template=(
        "Generate a {difficulty} true or false question about {topic}.\n\n"
        "Return ONLY a JSON object with these exact fields:\n"
        "- 'statement': A concise factual statement\n"
        "- 'answer': Either 'True' or 'False' (as a string)\n\n"
        "Example format:\n"
        '{{\n'
        '    "statement": "The capital of France is Paris.",\n'
        '    "answer": "True"\n'
        '}}\n\n'
        "Your response:"
    ),
    input_variables=["topic", "difficulty"]
)
