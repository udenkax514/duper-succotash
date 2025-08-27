import json
from difflib import get_close_matches

KNOWLEDGE_FILE = "knowledge_base.json"

# Load/save JSON
def load_knowledge_base():
    with open(KNOWLEDGE_FILE, "r") as file:
        return json.load(file)

def save_knowledge_base(data):
    with open(KNOWLEDGE_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Fuzzy search
def find_similar_questions(user_question, knowledge_base, cutoff=0.6):
    all_questions = [q["question"] for q in knowledge_base.get("questions", [])]
    return get_close_matches(user_question, all_questions, n=1, cutoff=cutoff)

# Answer lookup
def get_answer(user_question):
    knowledge_base = load_knowledge_base()
    similar = find_similar_questions(user_question, knowledge_base)
    if similar:
        for q in knowledge_base["questions"]:
            if q["question"].lower() == similar[0].lower():
                return q["answer"]
    return None

# Add new knowledge
def add_knowledge(question, answer):
    knowledge_base = load_knowledge_base()
    knowledge_base["questions"].append({"question": question, "answer": answer})
    save_knowledge_base(knowledge_base)
