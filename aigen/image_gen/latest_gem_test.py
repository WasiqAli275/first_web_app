import google.generativeai as genai

# API Key set karen
genai.configure(api_key="new_api_key.env") # enter your own api key in double quotes "" of this line.

# Model initialize karen
model = genai.GenerativeModel('gemini-1.5-pro-latest')  # Latest version

# Chat start karen
chat = model.start_chat()

# Prompt bhejen aur response print karen
response = chat.send_message("Hello Gemini! Mujhe Python programming ke bare mein 2 sentences mein batao")
print(response.text)
