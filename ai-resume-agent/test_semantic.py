from app.services.semantic_matcher import semantic_match_score

resume = """
Python developer.
Built REST APIs using FastAPI.
Worked with MongoDB.
"""

jd = """
Looking for backend developer.
FastAPI experience required.
Knowledge of APIs and databases.
"""

print(
    semantic_match_score(
        resume,
        jd
    )
)