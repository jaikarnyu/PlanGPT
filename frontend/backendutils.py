import json 
import requests
from datetime import datetime
import streamlit as st
import os 
from utils import *
from Home import * 
from config import *


base_url = KNOWLEDGE_BASE_URL

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
    


def upload_file_to_api(file, webbot_id):
    api_url = base_url + "/files/upload/" + str(webbot_id)
    print("Uploading file to the API...")
    files_list = {'files[]': file}
    response = requests.post(api_url, files=files_list)
    print(response.json())
    file_id = response.json()['results'][0]['file_id']
    text_file_id = response.json()['results'][0]['text_file_id']
    print("File uploaded successfully!")
    table_ids = response.json()['results'][0]['tables']
    # response = process_file(file_id)
    # if text_file_id:
    #     response = process_file(text_file_id)
    return {"file_id": file_id, "table_ids": table_ids, "text_file_id": text_file_id} 

def process_file(file_id):
    base_url = EMBEDDING_BASE_URL
    api_url = base_url + "/context/process_file/{file_id}?embedding_model=text-embedding-ada-002&chunk_size=200&summary_chunk_size=6000".format(file_id=file_id)
    response = requests.get(api_url)
    if response.status_code == 201:
        print("File processed successfully!")
    else:
        print('Error processing file:', response.status_code)
        print(response.content)
    return response

def generate_questions(webbot_id,file_id):
    """ Generates questions for a file """
    api_url = "{0}/questions/generate".format(base_url)
    data = {"webbot_id": webbot_id, "file_id": file_id}
    response = post(api_url, data)
    return None

