import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ==========================================
# DOWNLOAD NLTK RESOURCES
# ==========================================

def download_nltk_resources():

    resources = [
        ("corpora/stopwords", "stopwords"),
        ("corpora/wordnet", "wordnet"),
        ("corpora/omw-1.4", "omw-1.4")
    ]

    for path, package in resources:

        try:
            nltk.data.find(path)

        except LookupError:
            nltk.download(package, quiet=True)


download_nltk_resources()


# ==========================================
# NLP OBJECTS
# ==========================================

stop_words = set(
    stopwords.words("english")
)

lemmatizer = WordNetLemmatizer()


# ==========================================
# GENERIC WORDS TO IGNORE
# ==========================================

GENERIC_WORDS = {
    "resume",
    "curriculum",
    "vitae",
    "candidate",
    "applicant",
    "experience",
    "experienced",
    "education",
    "qualification",
    "qualifications",
    "skills",
    "skill",
    "responsibility",
    "responsibilities",
    "requirement",
    "requirements",
    "required",
    "preferred",
    "knowledge",
    "ability",
    "abilities",
    "working",
    "work",
    "team",
    "teams",
    "company",
    "organization",
    "role",
    "position",
    "job",
    "profile",
    "professional",
    "including",
    "using",
    "used",
    "strong",
    "good",
    "excellent",
    "looking",
    "seeking",
    "provide",
    "provided",
    "develop",
    "developed",
    "development",
    "data",
    "analysis",
    "analyst",
    "description",
    "driven",
    "communication",
    "problem",
    "problems",
    "solution",
    "solutions",
    "information",
    "details",
    "support",
    "management",
    "manager",
    "services",
    "service",
    "business",
    "project",
    "projects",
    "process",
    "processes",
    "level",
    "based",
    "related",
    "various",
    "ability",
    "abilities",
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december",
    "certification",
    "certifications",
    "descriptive"
}


# ==========================================
# TEXT PREPROCESSING
# ==========================================

def preprocess_text(text):

    # Convert to lowercase
    text = text.lower()

    # Remove email addresses
    text = re.sub(
        r"\S+@\S+",
        " ",
        text
    )

    # Remove URLs
    text = re.sub(
        r"http\S+|www\S+",
        " ",
        text
    )

    # Remove years such as 2023, 2024
    text = re.sub(
        r"\b(19|20)\d{2}\b",
        " ",
        text
    )

    # Remove numbers
    text = re.sub(
        r"\b\d+\b",
        " ",
        text
    )

    # Keep only letters and spaces
    text = re.sub(
        r"[^a-zA-Z\s]",
        " ",
        text
    )

    # Tokenization
    tokens = text.split()

    # Remove stopwords
    tokens = [
        word
        for word in tokens
        if word not in stop_words
    ]

    # Remove generic resume words
    tokens = [
        word
        for word in tokens
        if word not in GENERIC_WORDS
    ]

    # Remove very short words
    tokens = [
        word
        for word in tokens
        if len(word) >= 3
    ]

    # Lemmatization
    tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
    ]

    return " ".join(tokens)


# ==========================================
# TF-IDF SIMILARITY
# ==========================================

def calculate_similarity(
    resume_text,
    jd_text
):

    resume_processed = preprocess_text(
        resume_text
    )

    jd_processed = preprocess_text(
        jd_text
    )

    documents = [
        resume_processed,
        jd_processed
    ]

    # Prevent empty-document error
    if not resume_processed.strip() or not jd_processed.strip():
        return 0

    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2)
    )

    tfidf_matrix = vectorizer.fit_transform(
        documents
    )

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )[0][0]

    return similarity * 100

# ==========================================
# IMPORTANT TECHNICAL TERMS
# ==========================================

IMPORTANT_TERMS = {
    "python",
    "java",
    "sql",
    "mysql",
    "excel",
    "power bi",
    "tableau",
    "machine learning",
    "deep learning",
    "natural language processing",
    "nlp",
    "data science",
    "data analysis",
    "statistics",
    "pandas",
    "numpy",
    "scikit learn",
    "tensorflow",
    "pytorch",
    "streamlit",
    "artificial intelligence",
    "aws",
    "docker",
    "git",
    "mongodb",
    "database",
    "data visualization",
}


# ==========================================
# EXTRACT IMPORTANT KEYWORDS
# ==========================================

def extract_keywords(
    text,
    top_n=8
):

    processed_text = preprocess_text(text)

    # Prevent empty-text error
    if not processed_text.strip():
        return []

    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2),
        max_features=150,
        sublinear_tf=True
    )

    matrix = vectorizer.fit_transform(
        [processed_text]
    )

    feature_names = (
        vectorizer.get_feature_names_out()
    )

    scores = matrix.toarray()[0]

    keyword_scores = []

    for keyword, score in zip(
        feature_names,
        scores
    ):

        words = keyword.split()

        # Ignore generic single words
        if (
            len(words) == 1
            and words[0] in GENERIC_WORDS
        ):
            continue

        # Ignore very short words
        if any(
            len(word) < 3
            for word in words
        ):
            continue

        keyword_lower = keyword.lower()

        # ----------------------------------
        # Boost important technical terms
        # ----------------------------------

        if keyword_lower in IMPORTANT_TERMS:
            score = score * 2.5

        # ----------------------------------
        # Give preference to meaningful
        # two-word phrases
        # ----------------------------------

        elif len(words) == 2:
            score = score * 1.2

        keyword_scores.append(
            (keyword, score)
        )

    # Sort by final score
    keyword_scores.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return keyword_scores[:top_n]

    # --------------------------------------
    # Remove weak / meaningless keywords
    # --------------------------------------

    cleaned_keywords = []

    for keyword, score in keyword_scores:

        words = keyword.split()

        # Ignore keywords containing generic words
        if len(words) == 1 and words[0] in GENERIC_WORDS:
            continue

        # Ignore keywords shorter than 3 chars
        if any(
            len(word) < 3
            for word in words
        ):
            continue

        cleaned_keywords.append(
            (keyword, score)
        )

    # Sort by TF-IDF score
    cleaned_keywords.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return cleaned_keywords[:top_n]


# ==========================================
# COMPARE KEYWORDS
# ==========================================

def compare_keywords(
    resume_text,
    jd_text
):

    resume_keywords = extract_keywords(
        resume_text,
        top_n=8
    )

    jd_keywords = extract_keywords(
        jd_text,
        top_n=8
    )

    resume_words = {
        keyword.lower()
        for keyword, score
        in resume_keywords
    }

    jd_words = {
        keyword.lower()
        for keyword, score
        in jd_keywords
    }

    # --------------------------------------
    # Common keywords
    # --------------------------------------

    common_keywords = sorted(
        resume_words & jd_words
    )

    # --------------------------------------
    # Missing keywords
    # --------------------------------------

    missing_keywords = sorted(
        jd_words - resume_words
    )

    # --------------------------------------
    # Keyword coverage
    # --------------------------------------

    if jd_words:

        coverage = (
            len(common_keywords)
            / len(jd_words)
        ) * 100

    else:

        coverage = 0

    return {

        "resume_keywords":
            resume_keywords,

        "jd_keywords":
            jd_keywords,

        "common_keywords":
            common_keywords,

        "missing_keywords":
            missing_keywords,

        "keyword_coverage":
            coverage
    }


# ==========================================
# NLP SUMMARY
# ==========================================

def get_nlp_summary(
    resume_text,
    jd_text
):

    similarity = calculate_similarity(
        resume_text,
        jd_text
    )

    keyword_analysis = compare_keywords(
        resume_text,
        jd_text
    )

    return {

        "similarity_score":
            similarity,

        "resume_keywords":
            keyword_analysis[
                "resume_keywords"
            ],

        "jd_keywords":
            keyword_analysis[
                "jd_keywords"
            ],

        "common_keywords":
            keyword_analysis[
                "common_keywords"
            ],

        "missing_keywords":
            keyword_analysis[
                "missing_keywords"
            ],

        "keyword_coverage":
            keyword_analysis[
                "keyword_coverage"
            ]
    }