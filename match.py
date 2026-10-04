import spacy
import re
from extract import extract_pdf, extract_docx 
nlp=spacy.load("en_core_web_sm")
def eng(path):
    with open(path) as f:
        text=f.read()
    doc=nlp(text)
    return doc

def find_skills(text):
    text=text.lower()
    found=set()
    for skill in SKILLS:
        pattern = r"(?<![a-z0-9])" + re.escape(skill) + r"s?(?![a-z0-9])"
        if re.search(pattern, text):
            found.add(skill)
    return found

SKILLS = [
    "python", "java", "javascript", "c++", "sql", "mysql", "postgresql",
    "sqlite", "mongodb", "flask", "django", "fastapi", "react", "node.js",
    "html", "css", "git", "github", "docker", "kubernetes", "aws", "azure",
    "linux", "rest api", "json", "pytest", "unit testing", "ci/cd", "agile",
    "data structures", "algorithm", "object-oriented programming",
    "pandas", "numpy", "scikit-learn", "tensorflow", "machine learning",
    "nlp", "power bi", "spring boot",
]

if __name__=="__main__":
    with open("samples/job_description.txt") as f:
        jd_text=f.read()

    
    resume_text = extract_docx("samples/resume_data_science.docx")
    jd_skills = find_skills(jd_text)
    resume_skills=find_skills(resume_text)
    matched=jd_skills & resume_skills
    missing= jd_skills - resume_skills
    score= len(matched)/len(jd_skills)*100

    print("Matched:", sorted(matched))
    print("Missing:", sorted(missing))
    print("Score:", round(score), "%")


