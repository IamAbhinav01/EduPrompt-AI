# 🎓 EduPrompt AI

> **Revolutionizing Education with AI-Powered Question Generation**

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/LangChain-0.3.27+-green.svg)](https://langchain.com/)
[![Groq](https://img.shields.io/badge/Groq-LLM-orange.svg)](https://groq.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.47.1+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🚀 What is EduPrompt AI?

EduPrompt AI is an intelligent educational platform that leverages cutting-edge AI technology to automatically generate high-quality educational questions. Whether you're a teacher looking to create engaging assessments or a student wanting to practice with diverse question types, EduPrompt AI has got you covered!

### ✨ Key Features

- 🤖 **AI-Powered Generation**: Uses Groq LLM for intelligent question creation
- 📝 **Multiple Question Types**: Generate MCQs and Fill-in-the-Blank questions
- 🎯 **Difficulty Control**: Customize question difficulty (easy, medium, hard)
- 🔄 **Smart Retry Logic**: Robust error handling with automatic retries
- 📊 **Structured Output**: Pydantic models ensure consistent, validated responses
- 🎨 **Modern UI**: Beautiful Streamlit interface for seamless interaction

## 🛠️ Technology Stack

- **Backend**: Python 3.10+
- **AI Framework**: LangChain + Groq LLM
- **Data Validation**: Pydantic
- **Web Interface**: Streamlit
- **Environment Management**: uv (modern Python package manager)
- **Logging**: Custom logging system with structured output

## 📦 Installation

### Prerequisites

- Python 3.10 or higher
- Groq API key (get one at [groq.com](https://groq.com/))

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/IamAbhinav01/EduPrompt-AI.git
   cd EduPrompt-AI
   ```

2. **Install dependencies using uv**
   ```bash
   uv sync
   ```

3. **Set up environment variables**
   ```bash
   # Create a .env file
   echo "GROQ_API_KEY=your_groq_api_key_here" > .env
   ```

4. **Run the application**
   ```bash
   uv run streamlit run main.py
   ```

## 🎯 Usage

### Generating Questions

```python
from src.generator.question_generator import QuestionGenerator

# Initialize the generator
generator = QuestionGenerator()

# Generate an MCQ question
mcq = generator.generate_mcq(
    topic="Python Programming", 
    difficulty="medium"
)
print(f"Question: {mcq.question}")
print(f"Options: {mcq.options}")
print(f"Correct Answer: {mcq.correct_answer}")

# Generate a Fill-in-the-Blank question
fill_blank = generator.generate_fill_blank(
    topic="Machine Learning", 
    difficulty="hard"
)
print(f"Question: {fill_blank.question}")
print(f"Answer: {fill_blank.correct_answer}")
```

### Question Types

#### Multiple Choice Questions (MCQ)
- 4 carefully crafted options
- One correct answer
- Difficulty-based complexity
- Topic-specific content

#### Fill-in-the-Blank Questions
- Contextual sentence completion
- Single-word or phrase answers
- Adaptive difficulty levels
- Educational focus

## 🏗️ Project Structure

```
EduPrompt-AI/
├── src/
│   ├── common/           # Common utilities and exceptions
│   ├── config/           # Configuration management
│   ├── generator/        # Question generation logic
│   ├── llm/             # Groq LLM integration
│   ├── models/          # Pydantic data models
│   ├── prompts/         # AI prompt templates
│   └── utils/           # Helper functions
├── main.py              # Application entry point
├── pyproject.toml       # Project configuration
├── requirements.txt     # Dependencies
└── README.md           # This file
```

## 🔧 Configuration

The application uses a settings system that can be configured through environment variables:

- `GROQ_API_KEY`: Your Groq API key
- `MAX_RETRIES`: Maximum retry attempts for question generation (default: 3)
- `LOG_LEVEL`: Logging level (default: INFO)

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Setup

```bash
# Install development dependencies
uv sync --dev

# Run tests (when implemented)
uv run pytest

# Format code
uv run black src/
uv run isort src/
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Groq** for providing fast and reliable LLM inference
- **LangChain** for the excellent AI framework
- **Streamlit** for the beautiful web interface
- **Pydantic** for robust data validation

## 📞 Support

- 🐛 **Bug Reports**: [Create an issue](https://github.com/IamAbhinav01/EduPrompt-AI/issues)
- 💡 **Feature Requests**: [Suggest a feature](https://github.com/IamAbhinav01/EduPrompt-AI/issues)
- 📧 **Contact**: Reach out through GitHub

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=IamAbhinav01/EduPrompt-AI&type=Date)](https://star-history.com/#IamAbhinav01/EduPrompt-AI&Date)

---

<div align="center">

**Made with ❤️ for the education community**

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/IamAbhinav01)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/your-profile)

</div>
