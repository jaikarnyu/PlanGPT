import json 
import requests
from datetime import datetime
import streamlit as st
import os 


CONVERSATION_BASE_URL = os.getenv("CONVERSATION_BASE_URL", 'random url')

base_url = CONVERSATION_BASE_URL

def send_to_api(data):
    # api_url = base_url + '/api'
    # response = post(api_url, data)
    # return response
    return True

def get_from_api():
    response = "Dummy Text"
    return response

def update_from_api():
    response = "Updated Text"
    return response 

def exectute_plan():
    return "Plan is exectuted"

def post(api_url, data):
    response = requests.post(api_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    status_code = response.status_code
    if str(status_code).startswith('2'):
        print("Data sent successfully to the API! %s ", api_url)
        # print("Response: %s ", response.content)
        try:
            return json.loads(response.content)
        except:
            return response.content

    else:
        print('Error sending data to the API \n %s : \n %s ', api_url,response.content)
        return None

def get(api_url):
    response = requests.get(api_url)
    response_content = response.content
    status_code = response.status_code
    if str(status_code).startswith('2'):
        # print('Received data:', response_content)
        try:
            return json.loads(response_content)
        except:
            return response_content
    else:
        print('Error receiving data from the API:', response.status_code)
        return None
    
def update_state():
    st.session_state['submitted'] = True
    return st.session_state['submitted']

def get_prompts():
    response = "test prompt"
    return response