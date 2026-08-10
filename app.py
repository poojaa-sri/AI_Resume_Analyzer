import streamlit as st
import pandas as pd

from resume_parser import extract_text
from nlp_processor import get_nlp_summary
from analyzer import (
    compare_skills,
    generate_suggestions,
    resume_rating
)


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# ==========================================
# TITLE
# ==========================================

st.title("📄 AI Resume Analyzer")

st.write(
    "Analyze your resume using NLP, skill matching, "
    "TF-IDF and cosine similarity."
)

st.divider()


# ==========================================
# INPUT SECTION
# ==========================================

col1, col2 = st.columns(2)


with col1:

    st.subheader("📤 Upload Resume")

    resume = st.file_uploader(
        "Upload your resume",
        type=["pdf", "docx"]
    )


with col2:

    st.subheader("💼 Job Description")

    jd = st.text_area(
        "Paste the job description here",
        height=200
    )


# ==========================================
# ANALYZE BUTTON
# ==========================================

analyze_button = st.button(
    "🔍 Analyze Resume",
    type="primary",
    use_container_width=True
)


# ==========================================
# MAIN ANALYSIS
# ==========================================

if analyze_button:

    # --------------------------------------
    # VALIDATION
    # --------------------------------------

    if resume is None:

        st.warning(
            "⚠️ Please upload a PDF or DOCX resume."
        )

        st.stop()


    if not jd.strip():

        st.warning(
            "⚠️ Please paste a job description."
        )

        st.stop()


    # --------------------------------------
    # EXTRACT RESUME TEXT
    # --------------------------------------

    try:

        resume_text = extract_text(resume)

    except Exception as e:

        st.error(
            f"Error while reading resume: {e}"
        )

        st.stop()


    if not resume_text.strip():

        st.error(
            "Could not extract text from the resume."
        )

        st.stop()


    # ======================================
    # RESUME STATISTICS
    # ======================================

    st.divider()

    st.header("📊 Resume Statistics")


    words = len(
        resume_text.split()
    )

    characters = len(
        resume_text
    )

    lines = len(
        [
            line
            for line in resume_text.splitlines()
            if line.strip()
        ]
    )


    stat1, stat2, stat3 = st.columns(3)


    with stat1:

        st.metric(
            "Words",
            words
        )


    with stat2:

        st.metric(
            "Characters",
            characters
        )


    with stat3:

        st.metric(
            "Text Lines",
            lines
        )


    # ======================================
    # SKILL ANALYSIS
    # ======================================

    st.divider()

    st.header("🧠 Skill Analysis")


    try:

        analysis = compare_skills(
            resume_text,
            jd
        )

    except Exception as e:

        st.error(
            f"Skill analysis error: {e}"
        )

        st.stop()


    # --------------------------------------
    # GET SKILL RESULTS
    # --------------------------------------

    matched = analysis.get(
        "matched",
        []
    )

    missing = analysis.get(
        "missing",
        []
    )

    resume_skills = analysis.get(
        "resume_skills",
        []
    )

    job_skills = analysis.get(
        "job_skills",
        []
    )

    skill_score = analysis.get(
        "skill_score",
        0
    )


    # ======================================
    # NLP ANALYSIS
    # ======================================

    st.divider()

    st.header("🤖 NLP Analysis")


    try:

        nlp_result = get_nlp_summary(
            resume_text,
            jd
        )


        similarity_score = nlp_result.get(
            "similarity_score",
            0
        )


        resume_keywords = nlp_result.get(
            "resume_keywords",
            []
        )


        jd_keywords = nlp_result.get(
            "jd_keywords",
            []
        )


        common_keywords = nlp_result.get(
            "common_keywords",
            []
        )


        missing_keywords = nlp_result.get(
            "missing_keywords",
            []
        )


        keyword_coverage = nlp_result.get(
            "keyword_coverage",
            0
        )


    except Exception as e:

        st.error(
            f"NLP analysis error: {e}"
        )

        similarity_score = 0

        resume_keywords = []

        jd_keywords = []

        common_keywords = []

        missing_keywords = []

        keyword_coverage = 0


    # ======================================
    # FINAL ATS SCORE
    # ======================================

    # Skill Match       = 60%
    # NLP Similarity    = 25%
    # Keyword Coverage  = 15%

    ats_score = (

        (skill_score * 0.60)

        + (similarity_score * 0.25)

        + (keyword_coverage * 0.15)

    )


    # Keep score between 0 and 100

    ats_score = max(
        0,
        min(100, ats_score)
    )


    # ======================================
    # RESUME MATCH SCORE
    # ======================================

    st.divider()

    st.subheader(
        "🎯 Resume Match Score"
    )


    st.progress(
        ats_score / 100
    )


    score_col1, score_col2, score_col3, score_col4 = (
        st.columns(4)
    )


    with score_col1:

        st.metric(
            "ATS Score",
            f"{ats_score:.1f}%"
        )


    with score_col2:

        st.metric(
            "Skill Match",
            f"{skill_score:.1f}%"
        )


    with score_col3:

        st.metric(
            "NLP Similarity",
            f"{similarity_score:.1f}%"
        )


    with score_col4:

        st.metric(
            "Keyword Coverage",
            f"{keyword_coverage:.1f}%"
        )


    # ======================================
    # ATS SCORE MESSAGE
    # ======================================

    if ats_score >= 80:

        st.success(
            f"🟢 Excellent Match — ATS Score: "
            f"{ats_score:.1f}%"
        )

    elif ats_score >= 65:

        st.info(
            f"🔵 Good Match — ATS Score: "
            f"{ats_score:.1f}%"
        )

    elif ats_score >= 50:

        st.warning(
            f"🟡 Moderate Match — ATS Score: "
            f"{ats_score:.1f}%"
        )

    else:

        st.error(
            f"🔴 Low Match — ATS Score: "
            f"{ats_score:.1f}%"
        )


    # ======================================
    # NLP KEYWORD ANALYSIS
    # ======================================

    st.divider()

    st.subheader(
        "🔑 NLP Keyword Analysis"
    )


    nlp_col1, nlp_col2 = st.columns(2)


    with nlp_col1:

        st.metric(
            "NLP Similarity",
            f"{similarity_score:.1f}%"
        )


    with nlp_col2:

        st.metric(
            "Keyword Coverage",
            f"{keyword_coverage:.1f}%"
        )


    st.progress(
        min(
            keyword_coverage / 100,
            1.0
        )
    )


    # ======================================
    # TOP KEYWORDS
    # ======================================

    keyword_col1, keyword_col2 = (
        st.columns(2)
    )


    # --------------------------------------
    # TOP RESUME KEYWORDS
    # --------------------------------------

    with keyword_col1:

        st.subheader(
            "📄 Top Resume Keywords"
        )


        if resume_keywords:

            for keyword, score in resume_keywords:

                st.write(
                    f"**{keyword}** — "
                    f"{score:.3f}"
                )

        else:

            st.write(
                "No important keywords found."
            )


    # --------------------------------------
    # TOP JOB KEYWORDS
    # --------------------------------------

    with keyword_col2:

        st.subheader(
            "💼 Top Job Keywords"
        )


        if jd_keywords:

            for keyword, score in jd_keywords:

                st.write(
                    f"**{keyword}** — "
                    f"{score:.3f}"
                )

        else:

            st.write(
                "No important keywords found."
            )


    # ======================================
    # COMMON KEYWORDS
    # ======================================

    st.divider()

    st.subheader(
        "✅ Common Keywords"
    )


    if common_keywords:

        st.success(
            ", ".join(
                common_keywords
            )
        )

    else:

        st.info(
            "No common keywords detected."
        )


    # ======================================
    # MISSING KEYWORDS
    # ======================================

    st.subheader(
        "⚠️ Missing Keywords"
    )


    if missing_keywords:

        for keyword in missing_keywords:

            st.warning(
                keyword
            )

    else:

        st.success(
            "No important keywords are missing."
        )


    # ======================================
    # MATCHED AND MISSING SKILLS
    # ======================================

    st.divider()

    skill_col1, skill_col2 = (
        st.columns(2)
    )


    # --------------------------------------
    # MATCHED SKILLS
    # --------------------------------------

    with skill_col1:

        st.subheader(
            "✅ Matched Skills"
        )


        if matched:

            for skill in matched:

                st.success(
                    f"✓ {skill}"
                )

        else:

            st.write(
                "No matching skills found."
            )


    # --------------------------------------
    # MISSING SKILLS
    # --------------------------------------

    with skill_col2:

        st.subheader(
            "❌ Missing Skills"
        )


        if missing:

            for skill in missing:

                st.error(
                    f"✗ {skill}"
                )

        else:

            st.success(
                "No missing skills detected!"
            )


    # ======================================
    # ALL RESUME SKILLS
    # ======================================

    st.divider()

    st.subheader(
        "🛠️ Skills Detected in Resume"
    )


    if resume_skills:

        st.write(
            ", ".join(
                resume_skills
            )
        )

    else:

        st.write(
            "No predefined skills detected."
        )


    # ======================================
    # JOB SKILLS
    # ======================================

    st.subheader(
        "💼 Skills Required by Job"
    )


    if job_skills:

        st.write(
            ", ".join(
                job_skills
            )
        )

    else:

        st.write(
            "No predefined skills detected "
            "in the job description."
        )


    # ======================================
    # RESUME RATING
    # ======================================

    st.divider()

    st.header(
        "🏆 Resume Rating"
    )


    rating = resume_rating(
        ats_score
    )


    st.subheader(
        rating
    )


    # ======================================
    # IMPROVEMENT SUGGESTIONS
    # ======================================

    st.divider()

    st.header(
        "💡 Resume Improvement Suggestions"
    )


    suggestions = generate_suggestions(
        missing,
        ats_score
    )


    if suggestions:

        for suggestion in suggestions:

            st.write(
                f"• {suggestion}"
            )

    else:

        st.write(
            "No major improvements required."
        )


    # ======================================
    # SKILL SUMMARY CHART
    # ======================================

    st.divider()

    st.header(
        "📈 Skills Summary"
    )


    chart_data = pd.DataFrame(
        {
            "Skills": [
                "Matched",
                "Missing"
            ],

            "Count": [
                len(matched),
                len(missing)
            ]
        }
    )


    st.bar_chart(
        chart_data.set_index(
            "Skills"
        )
    )


    # ======================================
    # NLP ANALYSIS DETAILS
    # ======================================

    st.divider()

    st.header(
        "🔬 NLP Analysis Details"
    )


    st.write(
        """
        The system uses Natural Language Processing
        (NLP) to compare the resume with the job
        description.
        """
    )


    st.write(
        "The NLP pipeline includes:"
    )


    st.write(
        """
        1. Text Cleaning
        2. Lowercasing
        3. Tokenization
        4. Stopword Removal
        5. Lemmatization
        6. TF-IDF Vectorization
        7. Cosine Similarity
        8. Keyword Extraction
        9. Keyword Coverage
        """
    )


    # ======================================
    # REPORT GENERATION
    # ======================================

    st.divider()

    st.header(
        "📥 Download Reports"
    )


    report = f"""
AI RESUME ANALYZER REPORT
=========================

ATS Score:
{ats_score:.1f}%

Skill Match Score:
{skill_score:.1f}%

NLP Similarity Score:
{similarity_score:.1f}%

Keyword Coverage:
{keyword_coverage:.1f}%

Resume Rating:
{rating}


MATCHED SKILLS
==============

{", ".join(matched) if matched else "None"}


MISSING SKILLS
==============

{", ".join(missing) if missing else "None"}


COMMON KEYWORDS
===============

{", ".join(common_keywords) if common_keywords else "None"}


MISSING KEYWORDS
================

{", ".join(missing_keywords) if missing_keywords else "None"}


SUGGESTIONS
===========

"""


    for suggestion in suggestions:

        report += (
            f"- {suggestion}\n"
        )


    # --------------------------------------
    # TXT DOWNLOAD
    # --------------------------------------

    st.download_button(
        label="📄 Download TXT Report",
        data=report,
        file_name="resume_analysis.txt",
        mime="text/plain"
    )


    # ======================================
    # CSV REPORT
    # ======================================

    csv_df = pd.DataFrame(
        {
            "Matched Skills": matched
        }
    )


    csv_data = csv_df.to_csv(
        index=False
    )


    st.download_button(
        label="📊 Download Matched Skills CSV",
        data=csv_data,
        file_name="matched_skills.csv",
        mime="text/csv"
    )


    # ======================================
    # RESUME PREVIEW
    # ======================================

    st.divider()

    st.header(
        "📄 Resume Preview"
    )


    with st.expander(
        "Click here to view extracted resume text"
    ):

        st.text(
            resume_text
        )