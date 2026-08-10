import re

from skills import SKILLS


# -----------------------------
# EXTRACT SKILLS
# -----------------------------

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):

            found_skills.append(skill)

    return sorted(set(found_skills))


# -----------------------------
# COMPARE RESUME AND JOB
# -----------------------------

def compare_skills(
    resume_text,
    job_description
):

    resume_skills = extract_skills(
        resume_text
    )

    job_skills = extract_skills(
        job_description
    )

    matched = sorted(
        set(resume_skills)
        & set(job_skills)
    )

    missing = sorted(
        set(job_skills)
        - set(resume_skills)
    )

    if job_skills:

        skill_score = (
            len(matched)
            / len(job_skills)
        ) * 100

    else:

        skill_score = 0

    return {
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "matched": matched,
        "missing": missing,
        "skill_score": skill_score
    }


# -----------------------------
# RESUME SUGGESTIONS
# -----------------------------

def generate_suggestions(
    missing_skills,
    score
):

    suggestions = []

    if missing_skills:

        suggestions.append(
            "Consider adding or highlighting "
            "these skills if you genuinely have "
            "experience with them: "
            + ", ".join(missing_skills)
        )

    if score >= 80:

        suggestions.append(
            "Your resume is strongly aligned "
            "with the job description."
        )

        suggestions.append(
            "Highlight measurable achievements "
            "in your projects and experience."
        )

    elif score >= 60:

        suggestions.append(
            "Your resume has a reasonable match "
            "with the job description."
        )

        suggestions.append(
            "Improve keyword alignment and "
            "highlight relevant projects."
        )

    else:

        suggestions.append(
            "Your resume has a low skill match."
        )

        suggestions.append(
            "Tailor your resume to the specific "
            "requirements of the job description."
        )

    return suggestions


# -----------------------------
# RESUME RATING
# -----------------------------

def resume_rating(score):

    if score >= 90:

        return "★★★★★ Excellent Resume"

    elif score >= 75:

        return "★★★★☆ Very Good Resume"

    elif score >= 60:

        return "★★★☆☆ Good Resume"

    elif score >= 40:

        return "★★☆☆☆ Average Resume"

    else:

        return "★☆☆☆☆ Needs Significant Improvement"