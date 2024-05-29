knowledge_base = {
  "greetings": ["hi", "hello", "hey"],
  "farewells": ["bye", "goodbye", "see you later"],
  "thanks": ["thanks", "thank you"],
  "weather": {
    "questions": ["how's the weather", "what's the weather like"],
    "response": "I can't access real-time weather data yet, but I can tell you it's a beautiful day for a conversation!",
  },
  "movies": {
    "questions": ["recommend a movie", "what movie should I watch"],
    "genres": {
      "comedy": ["The Hangover", "21 Jump Street"],
      "action": ["Top Gun", "Mad Max: Fury Road"],
      "drama": ["Schindler's List", "The Shawshank Redemption"],
    },
  },
  "myself": {
    "questions": ["who are you", "what can you do"],
    "response": "I'm a simple Python chatbot. I can't answer everything yet, but I'm learning! I can recommend movies, answer basic questions, and have a friendly conversation.",
  },
}

def get_response(user_input):
  user_input = user_input.lower()
  # Check for greetings, farewells, and thanks
  if user_input in knowledge_base["greetings"]:
    return "Hi there! How can I help you today?"
  elif user_input in knowledge_base["farewells"]:
    return "See you later! Have a nice day!"
  elif user_input in knowledge_base["thanks"]:
    return "You're welcome!"

  # Check for specific topics
  for topic, details in knowledge_base.items():
    if topic != "greetings" and topic != "farewells" and topic != "thanks":
      if user_input in details.get("questions", []):
        if topic == "weather":
          return details["response"]
        elif topic == "movies":
          genre = get_movie_genre(user_input)
          if genre:
            return recommend_movie(genre)
          else:
            return "What kind of movie are you interested in (comedy, action, drama)?"
        else:
          return details["response"]

  # Default response (no match)
  return "I'm still learning! Can you rephrase that or try asking something different?"

def get_movie_genre(user_input):
  for genre, movies in knowledge_base["movies"]["genres"].items():
    if genre in user_input:
      return genre
  return None

def recommend_movie(genre):
  return f"How about a {genre} movie? You might enjoy {knowledge_base['movies']['genres'][genre][0]} or {knowledge_base['movies']['genres'][genre][1]}."

while True:
  user_input = input("You: ")
  response = get_response(user_input)
  print("Chatbot:", response)
  if response in knowledge_base["farewells"]:
    break

print("Chatbot: Conversation ended.")