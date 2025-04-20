import json
from sentence_transformers import SentenceTransformer, util
import torch

# Load model for sentence embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load intents
with open('intents.json', 'r') as f:
    data = f.read()
    print(data)  # This will print the content of the file to verify it's being read correctly
    intents = json.loads(data)

# Prepare intent questions and embeddings
intent_texts = [item['question'] for item in intents['intents']]
intent_embeddings = model.encode(intent_texts, convert_to_tensor=True)

def get_bot_response(user_input):
    user_embedding = model.encode(user_input, convert_to_tensor=True)
    
    # Calculate similarity
    cos_scores = util.pytorch_cos_sim(user_embedding, intent_embeddings)[0]
    best_idx = torch.argmax(cos_scores).item()
    best_intent = intents['intents'][best_idx]

    response = best_intent['response']
    intent_name = best_intent['tag']
    return response, intent_name
