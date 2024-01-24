import openai
import os
# ==========================================================
# This model is a specific model which generates stories
# stories based on specific backgrounds. We experimented 
# the base model with different prompts (basic structure remains same) 
# to create the variety in the story. 
# ==========================================================

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OPENAI_KEY')

# ==========================================================
#               M   O   D   E   L
# ==========================================================
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    # response = openai.ChatCompletion.create(
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.8, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]
# ==========================================================
#           P   A   R   A   M   E   T   E   R   S
# ==========================================================
background = ['sports', 'army','corporate'] #sample prompts

sports_story_prompt= f"""
you are an AI assitant for a script writer. your job is to \ 
generate an array of three stories in a json format. \

Each story should meet the following conditions: \
- Assume that the audience are of age between 12 to 20. \
- The opening line of the story should be between 250 chars to 750 chars. \
- The story should provide the user an array of a minimum of three twists\
to chose from. Twists and subtwists should be stated clearly. \
- Each twist should have a title and body. \
- Each twist should have an id of twist1, twist2 and so on. \
- Each twist should have a minimum of three subtwists. \
- Each subtwists should have an id, a title and a body attribute. \

- Each story should be in a {background} background filled with emotion \
and drama.
- The titles or subtitles cannot be repetitive.\

Write the response into array of jsons in the following format:\
- title : "title of the story"\
- body : "opening line of the story"\
- twists: "An array of twists in the story and their subtwists"\
 
 
"""
prompt = f"""
you are an AI assitant for a script writer. your job is to \ 
generate an array of three stories in a json format. \

Each story should meet the following conditions: \
- Assume that the audience are of age between 12 to 20. \
- The opening line of the story should be between 250 chars to 750 chars. \
- The story should provide the user an array of a minimum of three twists\
to chose from. Twists and subtwists should be stated clearly. \
- Each twist should have a title and body. \
- Each twist should have an id of twist1, twist2 and so on. \
- Each twist should have a minimum of two subtwists. \
- Each subtwists should have an id, a title and a body attribute. \

- Each story should have sufficient emotion, romance, comedy , \
spirituality and enough drama to make audience engaged. Please feel free to vary them\

-  A story with emotional_quotient of 1 \
should be able to make the user cry and read with a heavy heart.\
- A story with 0 reality_quotient \
means the environment of the story takes place in a well built realistic city \
and 1 being the story taking place in a remote fictitious village.\
- A story with a location_quotient of 0  means \
the location of story happening in Northern part of India \
and 1 means the story happepning in Southern part of India .\
- The titles or subtitles cannot be repetitive.\

Write the response into array of jsons in the following format:\
- title : "title of the story"\
- body : "opening line of the story"\
- twists: "An array of twists in the story and their subtwists"\
 
 
"""
response = get_completion(prompt)
print(response)