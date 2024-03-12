"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai
# from config import apikey
genai.configure(api_key="AIzaSyBJYyIFD2d94BS3V4WjqWwyC0DTRWw-eXE")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["Write me a song"]
  },
  {
    "role": "model",
    "parts": ["(Verse 1)\nIn the tapestry of life, where dreams unfurl their wings,\nA melody arose, a song my heart now sings.\nThrough the canvas of emotions, it dances free,\nA symphony of whispers, only you and I can see.\n\n(Chorus)\nOh, let our voices entwine,\nIn this sacred song of mine.\nWith each note, a story unfolds,\nA tale of love, a heart that holds.\n\n(Verse 2)\nLike a gentle breeze, your presence fills the air,\nYour laughter paints the sky, a vibrant hue so rare.\nThrough the storms and trials, we stand side by side,\nOur bond unbreakable, our love our guiding tide.\n\n(Chorus)\nOh, let our voices entwine,\nIn this sacred song of mine.\nWith each note, a story unfolds,\nA tale of love, a heart that holds.\n\n(Bridge)\nIn the twilight's embrace, as stars twinkle bright,\nWe share our dreams and hopes, in the soft moonlight.\nThrough the tapestry of time, our love will never cease,\nA melody that echoes, bringing us eternal peace.\n\n(Chorus)\nOh, let our voices entwine,\nIn this sacred song of mine.\nWith each note, a story unfolds,\nA tale of love, a heart that holds.\n\n(Outro)\nSo let the music flow, let our voices rise,\nIn this eternal symphony, where our love never dies.\nFor in this song, our hearts forever intertwine,\nA timeless masterpiece, a love that's truly divine."]
  },
])

# convo.send_message("Write me your name")
# print(convo.last.text)

response = model.generate_content("Write ma a song on sunrise")
print(response)