### ML Story Generator

## Overview
ML Story generator is an AI story generator built using openai.

### Architecture
![overview](images/overview.png?raw=true "ML Prompt Generation process")
The prompt engineering follows the below steps in generating a ML model :
- Idea generation
- Prepare the prompt
- Execute the model
- Error analysis /  Fine tuning

There are two types of chatbot models:
- <strong>Single turn</strong> :- We describe the task to be done by the assistant in a single prompt. Conversation will be one-way and chatbot has no access to previous conversations.
- <strong>Multi turn</strong> :- We continue the conversations with the chatbot. It can remember the past conversation with us, when we feed the same in the context of the prompt.

### Factors contributed for story generation
- When we generated the story, we considered the below quotients in preparing the prompt:
- Emotional Quotient
- Reality Quotient
- Locality Quotient
- Drama quotient

1. <strong>Emotional quotient</strong> varies from 0 to 1. 1 being more emotional story and 0 being least emotional
2. <strong>Reality quotient</strong> varies from 0 to 1. 1 being the story happening more in the real world whereas 0 being the story happening in a virtual world like wonderland.
3. <strong>Locality quotient</strong> varies from 0 to 1. 1 being the story happening in Northern part of India whereas 0 being the story happening in southern part.
4. <strong>Drama quotient</strong> varies from 0 to 1. 1 being the story more dramatic.

Sample values given for generating the model:
```
emotional_quotient= 0.5
location_quotient= 0.3
drama_quotient = 0.7  
reality_quotient= 0.5
```
![Factors for story generation](images/story.png?raw=true "Story generation attributes")

## Specifications:
Below are the specifications based on which the model is created:
- Platform  : openai
- Model : gpt-3.5-turbo
- Library: 0.27
- Type : single-turn 

## Environment setup for running ML model
- Run the below instructions step-by-step
```pip install openai```
```pip install python-dtenv```
- Create an openai account and follow the instructions here.
- Mention OPENAI_API_KEY as the key generated from yur openai account.
- Run the model to generate the story in json format.

## Expected output format of ML response
- The below file is a sample input format for the javascript
```
{
    title : "title01",
    body : "A simple story Line ",
    twists: [
        {
            id: "twist1',
            title: "A mini twist".
            body: "Body of the mini twist",
            subtwists = [
                {
                    title: "A micro twist",
                    body: "A micro body twist"
                }
            ]            
        },
        {
            id: "twist2',
            title: "Another mini twist".
            body: "Body of the mini twist",
            subtwists = [
                {
                    title: "Another micro twist",
                    body: "A micro body twist"
                }
            ]            
        }

    ]
}
```
## Environment setup for running the javascript code
- Run the below instructions for running the code
1. ```npm install```
2. Copy the story to an input file (story.json)
3. Update the file name in the index.js.
4. Verify the json file for any errors, manually.
5. Create a story3 account and generate an API_KEY.
6. Add the API_KEY in the STORY3_KEY variable of .env file in the root folder.
5. Run the command ```npm run start```

## Contact
- In case of any queries, Please feel free to write to us.
