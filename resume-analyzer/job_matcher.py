job_roles = {

"Data Scientist":[
"python","machine learning","pandas","numpy","statistics","sql"
],

"Data Analyst":[
"python","sql","excel","power bi","tableau","data analysis"
],

"Web Developer":[
"html","css","javascript","react","nodejs"
],

"ML Engineer":[
"python","machine learning","tensorflow","pytorch","deep learning"
]

}

def match_job_role(resume_skills):

    best_role = None
    best_score = 0
    matched_skills = []
    missing_skills = []

    for role, skills in job_roles.items():

        match = list(set(resume_skills) & set(skills))
        score = len(match) / len(skills) * 100

        if score > best_score:

            best_score = score
            best_role = role
            matched_skills = match
            missing_skills = list(set(skills) - set(resume_skills))

    return best_role, best_score, matched_skills, missing_skills