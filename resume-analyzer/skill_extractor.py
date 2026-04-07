import pandas as pd

skills_db = pd.read_csv("dataset/skills.csv")

skills_list = [skill.lower() for skill in skills_db['skill'].tolist()]

def extract_skills(resume_text):

    found_skills = []

    for skill in skills_list:

        if skill in resume_text:
            found_skills.append(skill)

    return list(set(found_skills))