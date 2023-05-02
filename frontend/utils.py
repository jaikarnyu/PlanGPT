import json 
import requests
from datetime import datetime
import streamlit as st
import os 
from config import *



base_url = KNOWLEDGE_BASE_URL



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
    
def update_text_prompts():
    st.session_state['completion1']= {"assistant_message" : "Please generate an Instruction above"}
    st.session_state['completion2']= {"assistant_message" : "Please generate an Instruction above"}
    st.session_state['retrieval'] = "Please generate an Instruction above"
    st.session_state['groundTruth'] = "Please generate an Instruction above"

    return True


def get_prompts():
    response = "test prompt"
    return response

def get_source_link():
    return "nyu.edu"

def get_link_depth():
    return "3"

# def update_state_template_submitted():
#     if ((st.session_state['template_name'] or st.session_state['template_description'] or st.session_state['template_content']) 
#     == ""):
#         st.error("Please Fill in all the fields")
#         st.session_state['template_submitted'] = False
#     else:
#         st.session_state['template_submitted'] = True
#     return st.session_state['template_submitted']

def send_template_to_api(name, description, content, option_type):
    st.write("in func")
    st.write(name)
    st.write(description)
    st.write(content)
    st.write(option_type)

    return True

def update_state_template_submission():
    print("Show up in the func")
    st.session_state['template_submitted'] = True
    return st.session_state['template_submitted']

def upload_file(files):

    # upload_file_to_api(file=files,webbot_id=st.session_state['webbot_id'])
    count = 1
    responses = []
    table_ids = []
    for file in files:
        st.progress(99, "Uploading File " + str(count) +   "  Please wait...")
        response = upload_file_to_api(webbot_id=st.session_state['webbot_id'],file=file)
        st.success("File uploaded successfully")
        # file_id = response['file_id']
        # text_file_id = response['text_file_id']
        # st.progress(99, "Processing file")
        # response = process_file(file_id)
        # if text_file_id:
        #     response = process_file(text_file_id)
        # st.success("File processed successfully")
        # st.progress(99,"Generating questions")
        # generate_questions(webbot_id=st.session_state['webbot_id'], file_id=file_id)
        # st.success("Questions generated successfully")
        count += 1
        responses.append(response)
    return responses

def get_file_meta(file_id):
    api_url = BASE_URL + "files/" + str(file_id)
    response = get(api_url)
    return response

def upload_file_to_api(file, webbot_id=WEBBOT_ID):
    api_url = BASE_URL + "files/upload/" + str(webbot_id)
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


def show_style():
    hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """
    st.markdown(hide_menu_style, unsafe_allow_html=True)
    
    st.markdown(
    f'''
        <style>
            .sidebar .sidebar-content {{
                width: 10px;
            }}
        </style>
    ''',
    unsafe_allow_html=True
    )