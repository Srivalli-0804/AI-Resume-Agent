from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def semantic_match_score(
    resume_text,
    job_description
):

    resume_embedding = model.encode(
        resume_text,
        convert_to_tensor=True
    )

    jd_embedding = model.encode(
        job_description,
        convert_to_tensor=True
    )

    similarity = cos_sim(
        resume_embedding,
        jd_embedding
    )

    score = float(
        similarity.item()
    )

    return round(
        score * 100,
        2
    )