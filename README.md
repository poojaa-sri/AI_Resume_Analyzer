# 📄 AI Resume Analyzer

An AI-powered web application that analyzes a resume against a given job description and provides a **resume match score, skill analysis, and actionable suggestions**.

The project uses **Natural Language Processing (NLP), TF-IDF, Cosine Similarity, and skill matching** to help job seekers understand how well their resume matches a target job role.

---

## 🚀 Project Overview

Applying for jobs often requires tailoring a resume according to the job description. Manually comparing a resume with a job description can be time-consuming.

**AI Resume Analyzer** simplifies this process by automatically analyzing the uploaded resume and comparing it with the provided job description.

It helps:

* 👩‍💼 **Recruiters** quickly evaluate and shortlist candidates.
* 👨‍🎓 **Job seekers** identify missing skills and improve their resumes.
* 📊 **Candidates** understand how closely their resume matches a specific job role.

---

## ✨ Key Features

### 📄 Resume Upload

* Upload resumes in **PDF or DOCX format**.
* Automatically extracts text from the uploaded resume.

### 📝 Job Description Analysis

* Accepts a job description as input.
* Identifies important skills and keywords from the job description.

### 🧠 NLP-Based Analysis

The application uses Natural Language Processing techniques to process and analyze resume content.

### 🔍 Skill Matching

* Compares skills mentioned in the resume with the skills required by the job description.
* Identifies matching and missing skills.

### 📊 Resume Match Score

Calculates a similarity score between the resume and job description using:

* **TF-IDF (Term Frequency-Inverse Document Frequency)**
* **Cosine Similarity**

### 💡 Improvement Suggestions

Provides suggestions based on missing skills and keywords to help improve the resume.

### ⭐ Resume Rating

Generates an overall resume rating based on the analysis.

---

## 🛠️ Technologies Used

| Technology      | Purpose                        |
| --------------- | ------------------------------ |
| 🐍 Python       | Core programming language      |
| 🎈 Streamlit    | Web application interface      |
| 🧠 NLP          | Text processing and analysis   |
| 📊 Scikit-learn | TF-IDF and Cosine Similarity   |
| 📄 PDFPlumber   | Extract text from PDF resumes  |
| 📝 Python-DOCX  | Extract text from DOCX resumes |
| 🔤 NLTK         | Text preprocessing             |
| 📦 Pandas       | Data processing                |

---

## 🔄 Project Workflow

```text
                ┌───────────────────┐
                │  Upload Resume    │
                │    PDF / DOCX     │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Extract Resume    │
                │      Text         │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Enter Job         │
                │ Description       │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ NLP Preprocessing │
                │ & Tokenization    │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ TF-IDF Vectorizer │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Cosine Similarity │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Skill Matching    │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Match Score &     │
                │ Suggestions       │
                └───────────────────┘
```

---

## 📁 Project Structure

```text
AI_Resume_Analyzer/
│
├── app.py
├── resume_parser.py
├── nlp_processor.py
├── analyzer.py
├── requirements.txt
├── README.md
│
└── .venv/
```

### File Description

**`app.py`**

Main Streamlit application that handles the user interface and connects all the project components.

**`resume_parser.py`**

Extracts text from uploaded PDF and DOCX resumes.

**`nlp_processor.py`**

Performs NLP preprocessing and generates NLP-based analysis using techniques such as TF-IDF and cosine similarity.

**`analyzer.py`**

Handles resume comparison, skill matching, resume rating, and improvement suggestions.

**`requirements.txt`**

Contains the Python libraries required to run the project.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI_Resume_Analyzer.git
```

### 2. Navigate to the Project Folder

```bash
cd AI_Resume_Analyzer
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

### 5. Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your browser.

Usually, it will be available at:

```text
http://localhost:8501
```

---

## 🖥️ How to Use

### Step 1 — Upload Resume

Upload your resume in either:

* PDF
* DOCX

### Step 2 — Enter Job Description

Paste the job description for the position you are applying for.

### Step 3 — Analyze

Click the **Analyze Resume** button.

### Step 4 — View Results

The application provides:

* 📊 Resume Match Score
* ✅ Matching Skills
* ❌ Missing Skills
* 💡 Improvement Suggestions
* ⭐ Resume Rating

---

## 🧠 NLP Techniques Used

### TF-IDF

**Term Frequency-Inverse Document Frequency (TF-IDF)** is used to convert text into numerical vectors based on the importance of words within the resume and job description.

### Cosine Similarity

Cosine similarity measures how similar the resume is to the job description based on their TF-IDF vectors.

A higher similarity value indicates greater textual similarity between the resume and job description.

### Skill Matching

The application maintains a list of relevant technical and professional skills and checks whether those skills appear in the resume and job description.

---

## 📊 Example Output

The analyzer can provide results such as:

```text
Resume Match Score: 78%

Matching Skills:
✓ Python
✓ SQL
✓ Power BI
✓ Excel

Missing Skills:
✗ Machine Learning
✗ Tableau

Suggestions:
• Add relevant Machine Learning projects.
• Highlight your SQL and Power BI experience.
• Include job-specific keywords where applicable.
```

> **Note:** The actual score and suggestions depend on the uploaded resume and job description.

---

## 🎯 Use Cases

### 👨‍🎓 Students & Freshers

* Check whether their resume matches a job description.
* Identify missing skills.
* Improve resume content before applying.

### 💼 Job Seekers

* Tailor resumes for specific job roles.
* Identify important keywords.
* Improve ATS-oriented resume content.

### 👩‍💼 Recruiters

* Quickly compare resumes with job requirements.
* Identify relevant candidate skills.
* Support initial resume screening.

---

## 🔮 Future Enhancements

Some possible improvements for future versions include:

* 🤖 Integration with Large Language Models (LLMs)
* 📌 Advanced ATS score calculation
* 🧠 Semantic similarity using transformer models
* 📑 Automatic resume improvement
* 🎯 Job recommendation based on resume skills
* 📈 Resume analytics dashboard
* 🌐 Deployment as a public web application
* 🔗 Integration with job portals

---

## 📚 Learning Outcomes

Through this project, I gained practical experience in:

* Python programming
* Natural Language Processing
* Text preprocessing
* TF-IDF
* Cosine Similarity
* Skill extraction and matching
* Streamlit application development
* Resume parsing
* Building an AI-based application
* Git and GitHub project management

---

## 👩‍💻 Author

**Pooja Sri**

B.Sc. Artificial Intelligence and Machine Learning

Interested in **AI, Machine Learning, Data Analytics, and Generative AI**.

---

## ⭐ If You Like This Project

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub!
