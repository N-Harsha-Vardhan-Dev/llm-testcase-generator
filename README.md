# 🧪 LLM-Based Test Case Generation System

An AI-powered QA automation tool that converts functional requirements into structured test cases with edge case extraction, classification, coverage scoring, and export support.

This project demonstrates how Large Language Models (LLMs) can enhance **shift-left testing**, improve test coverage, and automate requirement-to-test workflows.

---

## 🚀 Features

### ✅ Core Capabilities
- Convert functional requirements → structured test cases
- JSON schema–validated outputs
- Classification: type, priority, severity
- Edge case generation (security, concurrency, performance, accessibility)
- Coverage scoring to evaluate test completeness

### 📤 Export Options
- JSON download
- CSV export for QA tools (Excel, TestRail, Jira)

### 🖥 Interfaces
- FastAPI backend
- Streamlit interactive UI

---

## 🧠 Why This Project?

Manual test case design is:
- time-consuming
- inconsistent
- prone to missing edge cases

This system automates requirement-to-test translation and ensures coverage across critical testing dimensions.

---

## 🏗 Architecture
```

Requirement  
↓  
Prompt Engineering  
↓  
LLM (Gemini / extensible to Ollama)  
↓  
JSON Extraction & Validation  
↓  
Coverage Scoring  
↓  
Export (JSON / CSV)  
↓  
FastAPI & Streamlit UI

```
---

## 📂 Project Structure
```

llm-testcase-generator/  
│  
├── app/  
│ ├── main.py # FastAPI backend  
│ ├── streamlit\_app.py # Streamlit UI  
│ ├── llm\_client.py # LLM provider integration  
│ ├── llm\_service.py # Retry & orchestration  
│ ├── prompt.py # Prompt template  
│ ├── schema.py # Pydantic schema  
│ ├── validator.py # JSON extraction & validation  
│ ├── coverage.py # Coverage scoring  
│ └── exporter.py # JSON & CSV export  
│  
├── examples/ # Demo dataset  
├── exports/ # Generated files (ignored)  
├── .env.example  
├── requirements.txt  
└── README.md

```
---

## ▶️ Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/llm-testcase-generator.git
cd llm-testcase-generator
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set API key

Copy `.env.example` → `.env`

```ini
GOOGLE_API_KEY=your_api_key_here
```

---

## 🚀 Run FastAPI

```bash
uvicorn app.main:app --reload
```

Open:  
👉 http://127.0.0.1:8000/docs

---

## 🖥 Run Streamlit UI

```bash
streamlit run streamlit_app.py
```

---

## 🧪 Example Input

```arduino
User can upload profile image with maximum size 2MB.
Supported formats: JPG and PNG.
```

---

## 📊 Example Output

The system generates:

-   Positive tests
    
-   Boundary conditions (2MB limit)
    
-   Security scenarios (XSS, path traversal)
    
-   Concurrency tests
    
-   Accessibility considerations
    
-   Coverage summary with missing categories
    

---

## 📈 Coverage Scoring

The system evaluates test completeness across:

-   Positive scenarios
    
-   Negative scenarios
    
-   Boundary conditions
    
-   Security tests
    
-   Performance tests
    
-   Concurrency tests
    
-   Accessibility
    

---

## 🔮 Future Enhancements

-   Multi-requirement parsing
    
-   Automation script generation (Selenium/Postman)
    
-   Ollama local model support
    
-   Prompt auto-improvement based on coverage gaps
    
-   Deployment on Streamlit Cloud
    

---

## 👨‍💻 Author

**Harsha Vardhan Nandineni**

Final-year Computer Science student specializing in:

-   Generative AI
    
-   LLM integration
    
-   QA automation systems
    
-   FastAPI backend development
    
![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![LLM](https://img.shields.io/badge/LLM-Gemini-purple)

---