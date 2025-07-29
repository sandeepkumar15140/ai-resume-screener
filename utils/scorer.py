from sentence_transformers import SentenceTransformer, util

model = None

def analyze_resume(resume_text, job_desc):
    global model
    if model is None:
        model = SentenceTransformer("paraphrase-MiniLM-L3-v2")
    
    resume_emb = model.encode(resume_text, convert_to_tensor=True)
    jd_emb = model.encode(job_desc, convert_to_tensor=True)
    similarity = util.cos_sim(resume_emb, jd_emb).item()
    
    score = round(similarity * 100, 2)
    return {
        "ats_score": score,
        "match_level": "High" if score > 70 else "Medium" if score > 40 else "Low",
        "suggestions": "Add more relevant keywords from the job description."
    }
