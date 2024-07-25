from langchain_openai import OpenAI
from sentence_transformers import SentenceTransformer, util
import torch

OPENAI_API_KEY = "API_KEY"

# Initialize the OpenAI model with LangChain
llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.6)

# Initialize the sentence transformer model for embeddings
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Simple cache for frequently asked questions
cache = {
    "What is the capital of France?": "The capital of France is Paris.",
    "Who wrote 'To Kill a Mockingbird'?": "Harper Lee wrote 'To Kill a Mockingbird'.",
    "What is the boiling point of water?": "The boiling point of water is 100 degrees Celsius.",
    "What is a Large Language Model (LLM)?": "A Large Language Model (LLM) is a type of artificial intelligence model that is trained on vast amounts of text data to understand and generate human-like language.",
    "How do LLMs work?": "LLMs work by using deep learning techniques to analyze and generate text based on patterns learned from large datasets. They use neural networks with many layers to understand context, syntax, and semantics.",
    "What are some applications of LLMs?": "Applications of LLMs include chatbots, text summarization, language translation, sentiment analysis, and more.",
    "How can I fine-tune an LLM?": "Fine-tuning an LLM involves training the model further on a specific dataset to make it more effective for a particular task or domain.",
    "What is LangChain?": "LangChain is a library that provides tools and frameworks to build applications powered by language models. It offers features for prompt management, workflow automation, and model integration.",
    "What are some common projects using LLMs?": "Common projects using LLMs include virtual assistants, automated customer support, content generation tools, and language translation services.",
}

# Precompute embeddings for cache questions
cache_embeddings = embedding_model.encode(list(cache.keys()), convert_to_tensor=True)

def get_most_similar_question(user_input):
    user_embedding = embedding_model.encode(user_input, convert_to_tensor=True)
    similarities = util.pytorch_cos_sim(user_embedding, cache_embeddings)
    best_match_index = torch.argmax(similarities).item()
    best_match_question = list(cache.keys())[best_match_index]
    best_match_score = similarities[0][best_match_index].item()
    return best_match_question, best_match_score

def chatbot(user_input):
    # Find the most similar question in the cache
    best_match_question, best_match_score = get_most_similar_question(user_input)

    if best_match_score > 0.5:  # You can adjust this threshold as needed
        response = cache[best_match_question]
    else:
        try:
            response = llm.invoke(user_input)
            # Cache the response if it's a common question
            if user_input not in cache:
                cache[user_input] = response
                global cache_embeddings
                cache_embeddings = torch.cat([cache_embeddings, embedding_model.encode([user_input], convert_to_tensor=True)], dim=0)
        except Exception as e:
            print(f"Error: {e}")
            response = "An error occurred."

    # print("AI:", response)
    return response

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Exiting chatbot...")
            break
        response = chatbot(user_input)
        print("AI:", response)
