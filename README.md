<h1 align="center">🎯 AI-Based Personalized IIT-JEE Study Report Generator</h1>

<p align="center">
  <strong>Empowering every IIT-JEE student with personalized guidance using AI.</strong><br>
  <em>Built with LangGraph · LangChain · FastAPI · Uvicorn</em>
</p>

---

## ✨ Overview

🎓 Traditional coaching often offers **generic guidance**, but every student has a unique pace, strengths, and weaknesses.

This project is an **AI-powered system** that generates **daily personalized study reports** for IIT-JEE aspirants based on their activity, doubts, confidence levels, and time spent.

> 💡 *Inspired by my own struggles during JEE prep, I built this system to offer what I wish I had — tailored feedback every single day.*

---

## 🚀 Features

- ✅ **Personalized Daily Reports** for every subject
- 📊 Analyzes:
  - Topics covered
  - Time spent
  - Number of questions solved
  - Confidence level
  - Doubts and understanding
- 📚 Subject-wise breakdown:
  - Mathematics
  - Physics
  - Organic Chemistry
  - Inorganic Chemistry
  - Physical Chemistry
- 🧠 Uses LLMs to generate encouraging and constructive feedback
- 🌐 API access with FastAPI + Uvicorn

---

## 🧱 Tech Stack

| Layer         | Tool       |
|---------------|------------|
| AI Workflow   | 🔁 LangGraph  |
| LLM Orchestration | 🦜 LangChain |
| Backend       | ⚡ FastAPI |
| Server        | 🚀 Uvicorn |
| Language      | 🐍 Python |

---

## 📥 Input Format Example

```json
{
  "Math": {
    "math_revision": {
      "topic": "Vectors",
      "type": "read theory",
      "solved_questions": 5,
      "questions_corrected": 2,
      "time_spent": "20 minutes",
      "confidence_level": 3,
      "doubts": "doubts",
      "doubt_part": "direction cosine",
      "helpful": "not helpful"
    }
  },
  ...
}


## output report example

{
  "math_report_revision": "You revised the topic of Vectors today by reading theory, solving 5 questions...",
  "physics_report_revision": "Today's revision focused on Electrostatics...",
  "final_report": "Today, you dedicated time to revise various subjects for your IIT-JEE preparation...",
  "final_score": 5
}
