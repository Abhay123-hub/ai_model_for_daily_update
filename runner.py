from workflow import workflow
## This is my input which i am going to provide to my AI model
input = {
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
    "Physics": {
        "physics_revision": {
            "topic": "Electrostatics",
            "type": "watched video",
            "solved_questions": 3,
            "questions_corrected": 1,
            "time_spent": "15 minutes",
            "confidence_level": 2,
            "doubts": "doubts",
            "doubt_part": "Coulomb’s Law",
            "helpful": "not helpful"
        }
    },
    "Organic_Chemistry": {
        "organic_chemistry_revision": {
            "topic": "Hydrocarbons",
            "type": "read theory",
            "solved_questions": 4,
            "questions_corrected": 1,
            "time_spent": "25 minutes",
            "confidence_level": 3,
            "doubts": "doubts",
            "doubt_part": "reaction mechanisms",
            "helpful": "not helpful"
        }
    },
    "Inorganic_Chemistry": {
        "inorganic_chemistry_revision": {
            "topic": "Periodic Trends",
            "type": "watched video",
            "solved_questions": 2,
            "questions_corrected": 0,
            "time_spent": "10 minutes",
            "confidence_level": 2,
            "doubts": "doubts",
            "doubt_part": "atomic radius trend",
            "helpful": "not helpful"
        }
    },
    "Physical_Chemistry": {
        "physical_chemistry_revision": {
            "topic": "Ionic Equilibrium",
            "type": "read theory",
            "solved_questions": 6,
            "questions_corrected": 2,
            "time_spent": "30 minutes",
            "confidence_level": 3,
            "doubts": "doubts",
            "doubt_part": "buffer solutions",
            "helpful": "not helpful"
        }
    }
}



work = workflow()
response =work.execute(input)
print(response.get("final_score"))
print(response.get("math_report_revision"))
