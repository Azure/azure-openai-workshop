#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_type = "azure"
openai.api_base = "https://cogsearchdemo.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
  engine="gpt-35-turbo",
  messages = [{"role":"system","content":"You are an AI assistant that helps people find information."},
              {"role":"user","content":"Can you summerize this page: https://learn.microsoft.com/en-us/azure/machine-learning/tutorial-create-secure-workspace"},{"role":"assistant","content":"The page is a tutorial on how to create a secure workspace in Microsoft Azure Machine Learning. It covers topics such as creating a workspace, configuring security settings, managing access, and using Azure Key Vault to securely store secrets. It also provides step-by-step instructions and code samples to help users follow along. The tutorial emphasizes the importance of security in machine learning workflows and highlights the features of Azure that can help ensure data and model security."},{"role":"user","content":"What are the difference between previous page and this page? https://learn.microsoft.com/en-us/azure/machine-learning/tutorial-create-secure-workspace-no-address"},{"role":"assistant","content":"I'm sorry, but I am not able to access the links you provided. The links seem to be broken or inaccessible. Could you please provide me with a different link or explain what you would like me to do?"}],
  temperature=0.7,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None)

print(response)