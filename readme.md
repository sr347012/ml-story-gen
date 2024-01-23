### ML Story Generator

## Overview
ML Story generator is an AI story generator built using openai.

## Architecture
![overview](images/overview.png?raw=true "ML Prompt Generation process")

## Factors cntributed for story generation
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

## Conact
- In case of any queries, Please feel free to write to us.
