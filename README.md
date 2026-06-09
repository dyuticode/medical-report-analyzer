# 🩺 MediInsight AI Pro

<div align="center">

### Intelligent Medical Report Analysis Powered by AI

Transform laboratory PDFs into actionable health insights using OCR, Medical NLP, Risk Prediction, Voice Queries, and Google Gemini AI.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red)
![Gemini](https://img.shields.io/badge/Google-Gemini_2.5_Flash-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

</div>

---

# 📌 Overview

**MediInsight AI Pro** is an advanced AI-powered healthcare analytics platform designed to automatically extract, interpret, and explain laboratory reports from PDF files.

Traditional lab reports contain large amounts of medical data that may be difficult for patients to understand. MediInsight AI Pro converts these reports into an interactive dashboard that highlights abnormalities, explains medical terminology, predicts potential health risks, and provides personalized lifestyle recommendations.

The application combines:

* Medical parameter extraction
* Clinical range validation
* AI-powered report interpretation
* Disease risk assessment
* Voice-enabled interaction
* Multi-language translation
* Professional PDF report generation

---

# 🚀 Key Features

## 📄 Smart PDF Report Analysis

Upload laboratory reports in PDF format and automatically extract:

* Complete Blood Count (CBC)
* Blood Sugar Profile
* Lipid Profile
* Liver Function Test (LFT)
* Kidney Function Test (KFT)
* Thyroid Profile
* Heart Health Indicators
* Urine Analysis

Supports analysis of **58+ medical parameters**.

---

## 🔍 Intelligent Parameter Extraction

The regex-based parsing engine automatically detects:

| Category        | Parameters                                  |
| --------------- | ------------------------------------------- |
| CBC             | Hemoglobin, WBC, RBC, Platelets, Hematocrit |
| Diabetes        | FBS, PPBS, HbA1c                            |
| Lipid Profile   | Cholesterol, HDL, LDL, Triglycerides        |
| Liver Function  | ALT, AST, Bilirubin, Albumin                |
| Kidney Function | Creatinine, Urea, eGFR                      |
| Thyroid         | T3, T4, TSH                                 |
| Cardiac Health  | CRP, Homocysteine                           |
| Urine Analysis  | Protein, Glucose, Ketones                   |

---

## 🎨 Dynamic Health Status Classification

Every parameter is categorized into one of three levels:

### 🟢 Normal

Value lies within the medically accepted reference range.

### 🟡 Slightly Abnormal

Value deviates slightly from standard limits.

### 🔴 Critical

Value exceeds a dynamic threshold of ±25% from the normal range and requires immediate attention.

---

## 🧬 AI Disease Risk Prediction

Using Google Gemini AI, the application evaluates combined biomarker patterns and predicts possible risks associated with:

* Type 2 Diabetes
* Prediabetes
* Hypertension
* Cardiovascular Disease
* Hyperlipidemia
* Kidney Dysfunction
* Liver Disorders
* Anemia
* Inflammatory Conditions

The generated report includes:

* Risk Level
* Contributing Parameters
* Clinical Interpretation
* Preventive Measures

---

## 💬 AI Health Assistant

Built-in chatbot allows users to ask questions such as:

* Why is my hemoglobin low?
* What causes high cholesterol?
* What does elevated creatinine indicate?
* Is my HbA1c dangerous?
* How can I improve liver function?

The chatbot uses Gemini AI to generate medically understandable explanations.

---

## 🎙️ Voice Assistant Support

Hands-free interaction using microphone input.

Users can:

* Ask questions verbally
* Receive AI-generated explanations
* Navigate reports more easily

---

## 🌐 Multi-Language Translation

Translate:

* Report Analysis
* Risk Assessment
* AI Explanations
* Recommendations

Supported Languages:

* English
* Hindi
* Spanish
* French
* German
* Arabic

---

## 📥 PDF Report Export

Generate professional downloadable reports containing:

* Patient Summary
* Extracted Parameters
* Status Indicators
* Disease Risk Assessment
* Lifestyle Recommendations
* AI Insights

---

# 🏗️ System Architecture

```text
medical report/
│
├── app.py
├── .env
├── README.md
│
└── utils/
    │
    ├── __init__.py
    ├── ocr.py
    ├── parser.py
    ├── analyzer.py
    ├── ai_engine.py
    └── pdf_generator.py
```

---

# 📂 Module Breakdown

## app.py

Main Streamlit application.

Responsibilities:

* User Interface
* File Upload
* Dashboard Rendering
* Chat Interface
* Voice Assistant Integration
* PDF Download

---

## utils/ocr.py

Responsible for:

* Reading uploaded PDFs
* Extracting raw text
* Cleaning OCR output

Libraries:

```python
pdfplumber
```

---

## utils/parser.py

Regex-powered parameter extraction engine.

Responsibilities:

* Detect parameter names
* Extract values
* Normalize formats
* Support multiple report layouts

Example:

```python
Hemoglobin: 12.4 g/dL
WBC Count: 8500 /µL
```

---

## utils/analyzer.py

Medical validation engine.

Responsibilities:

* Compare extracted values against reference ranges
* Determine Normal / Abnormal / Critical status

Example:

```python
normal_ranges = {
    "Hemoglobin": (12,16),
    "WBC": (4000,11000)
}
```

---

## utils/ai_engine.py

Google Gemini integration.

Functions:

* Risk Prediction
* Medical Explanation Generation
* Translation Services
* Health Recommendations

Model Used:

```python
gemini-2.5-flash
```

---

## utils/pdf_generator.py

Creates structured downloadable reports.

Libraries:

```python
reportlab
```

---

# 🛠️ Installation

## Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/medical-report-analyzer.git

cd medical-report-analyzer
```

---

## Step 2: Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Step 3: Install Dependencies

```bash
pip install streamlit
pip install pandas
pip install pdfplumber
pip install google-genai
pip install reportlab
pip install gtts
pip install python-dotenv
pip install streamlit-mic-recorder
```

Or:

```bash
pip install -r requirements.txt
```

---

## Step 4: Configure Environment Variables

Create:

```text
.env
```

Add:

```env
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

Generate your API key from:

https://aistudio.google.com/

---

# ▶️ Running the Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

# 🧪 Sample Report for Testing

```text
METROPOLITAN DIAGNOSTIC LABORATORY

Patient Name: John Doe
Age: 45

Complete Blood Count (CBC)

Hemoglobin: 11.2 g/dL
WBC Count: 14500 /µL
Platelets: 380000 /µL

Blood Sugar Profile

Fasting Blood Sugar: 156 mg/dL
HbA1c: 7.4 %

Kidney Function Test

Creatinine: 1.8 mg/dL

Urine Analysis

Urine Protein: Positive
Urine Glucose: Positive
```

---

# 🔄 Workflow

```text
PDF Upload
    ↓
OCR Extraction
    ↓
Regex Parsing
    ↓
Parameter Identification
    ↓
Medical Range Validation
    ↓
Risk Prediction (Gemini AI)
    ↓
Chatbot Explanation
    ↓
Translation
    ↓
PDF Export
```

---

# 📊 Supported Medical Parameters

The system currently supports over 58 biomarkers including:

### CBC

* Hemoglobin
* RBC
* WBC
* Platelets
* Hematocrit
* MCV
* MCH
* MCHC

### Blood Sugar

* FBS
* PPBS
* HbA1c

### Lipid Profile

* Total Cholesterol
* HDL
* LDL
* VLDL
* Triglycerides

### Kidney Function

* Creatinine
* Urea
* BUN
* Uric Acid

### Liver Function

* ALT
* AST
* Bilirubin
* Albumin
* Total Protein

### Thyroid

* T3
* T4
* TSH

### Urine Analysis

* Protein
* Glucose
* Ketones
* pH
* Specific Gravity

And many more.

---

# 🔮 Future Enhancements

### Phase 2

* Medical Report Image Upload
* OCR using EasyOCR/Tesseract
* Interactive Trend Graphs
* Health Score Generation
* Historical Report Comparison
* Medication Recommendations
* Doctor Consultation Suggestions
* Personalized Diet Plans
* Health Risk Timeline

### Phase 3

* Multi-user Authentication
* Cloud Database Storage
* Report History Tracking
* Hospital Integration
* Mobile Application
* RAG-based Medical Knowledge Base
* Fine-Tuned Medical LLM

---

# 🛡️ Disclaimer

MediInsight AI Pro is intended solely for educational and informational purposes.

The system:

* Does not diagnose diseases.
* Does not replace professional medical consultation.
* Does not prescribe treatments.
* Should not be used as a substitute for licensed healthcare advice.

Always consult a qualified healthcare professional regarding medical concerns.

---

# 👨‍💻 Author

Developed by:

**Dyuti Asok B**

B.Tech Artificial Intelligence & Data Science

Amrita Vishwa Vidyapeetham

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the project

🛠️ Contribute improvements

📢 Share with others

---

### "Turning complex medical reports into understandable health insights using AI."
