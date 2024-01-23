import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OPENAI_KEY')


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    # response = openai.ChatCompletion.create(
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.8, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


emotional_quotient= 0.5
location_quotient= 0.3
drama_quotient = 0.7  
reality_quotient= 0.5
spiritual_quotient = 0.7


prompt = f"""
you are an AI assitant for a script writer. your job is to \ 
generate a story with \
emotional_quotient as {emotional_quotient}, \
location_quotient as {location_quotient}, \
spiritual_quotient as {spiritual_quotient}, \
drama_quotient as {drama_quotient} and \
reality_quotient as {reality_quotient}

The story should meet the following conditions:
- Assume that the audience are of age between 10 to 20.
- Make sure to add some romance or comedy while generating.
- The opening line should be between 250 chars to 750 chars.
- The story should provide the user an array of a minimum of three twists\
to chose from. Twists and Options should be stated clearly.
- Each twist should have a title and body.The body \
cannot exceed 1200 chars.
- Each twist should have an id of twist1, twist2 and so on. 
- Each subtwists should have an id, title and body attributes.
- Each twist should have a minimum of two subtwists.

- The story should have an emotional_quotient \
ranging from 0 to 1, 0 being \
lowest and 1 being highest. A story with emotional_quotient of 1 \
should be able to make the user cry and read with a heavy heart.
- The story should have a reality_quotient \
0 being the environment of the story take place in a well built realistic city \
and 1 being the story taking place in a remote fictitious village.
- The story should have a drama_quotient of 0 to 1, 1 being more dramatic.
- The story should have a location_quotient of 0 to 1, where 0 being 
the location of story happening in the state of Jammu & Kashmir(North India) / 
and 1 being the story happepning in the state of Tamil Nadu(South India) .
- The story should have a spiritual_quotient of 0 to 1, 1 being more spiritual.

Write the response into json in the following format:
- title : "title of the story"
- body : "opening line of the story"
- twists: "An array of twists in the story and their subtwists"
- climax: "Climax of the story"
- metadata: "An array of emotional quotient, drama quotient \
and location quotient for the generated story".

"""
response = get_completion(prompt)
print(response);
# with open('result.txt', 'a') as fp:
#     fp.write(response)