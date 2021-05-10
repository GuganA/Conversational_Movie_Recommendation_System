# ```Conversational Movie Recommendation System```
Movie Recommendation in Conversational 


Steps To Run projects

## Step 1: Create Slack Bot user

## Step 2: Create a IBM Watson account and Upload the bot.json workspace
     skill-sam.json file in nlp 
     
## Step 3: Install required packages

```sh
pip install pandas
pip install numpy
pip install sklearn
pip install nltk
python -m nltk.downloader stopwords
python -m nltk.downloader punkt]
pip install slackclient
pip install ibm-watson
```

## Step 4: Update the config files with the Slack and Watson API details

Please make sure that you modified the API details both for Slack and Watson in the config.py file

## Step 5: Download data from source and perform Data Preparation

The data for this example is downloaded from the location below,

https://www.kaggle.com/rounakbanik/movie-recommender-systems/data

Name of the dataset - movies_metadata.csv

## Step 6: Create "onetime.txt" file

Navigate to the folder where the main.py file resides and execute the code below.

```sh
python nlp/nlp_solutions/onetime_run_file.py
```
This will create the "onetime.txt" file automatically. If you need to rename this file, update the name in "config.py" file.

## Step 7: Initiate Bot

Navigate to the folder where the main python script exists and run the code below.

```sh
python main.py
```

# ```Working of the Bot```

### Step 1 (User asks question):
Users can interact with Sam via Slack. Once the user post a question via the interface, the question is passed to the backend system for analysis

### Step 2 (NLP processing):
All the natural language processing happens in step 2.  

### Step 3 (Return the NLP results):
After the NLP processing is completed, we have three outputs from it
1) Intents - What the user is trying to ask or query?
2) Entities - What is the exact field or column they are looking for?
3) Dialog/Interaction - Provide the appropriate request/response for the user question.

### Step 4 and 5(Query the data):

Currently, the data resides in a excel file. However, you can add multiple databases/excel files if needed, to access different sources. Based on the results from step 3, the appropriate database/excel file is queried and the results are returned.

### Step 6 (Post the result to user):

The results obtained from the backend is posted to user via Slack

### Step 7 (Log maintenance):

The interactions between the users are logged and stored in a flatfile format in a log file. Also, if the bot is not able to identify the user questions it will add those questions to a followup file.


