import streamlit as st
import logging
from utils import *
from template_utils import *

#Session State Link
if 'link' not in st.session_state:
    st.session_state['link'] = ""

#Session State Knowledge:
if 'knowledge_type' not in st.session_state:
    st.session_state['knowledge_type'] = ""

st.subheader("Knowledge")

with st.form("LinkForm",clear_on_submit=True):
    
    # st.write(st.session_state['knowledge_type'])
    st.session_state['link'] = st.text_input("Please enter the URL for the Knowledge", key="link_input", value = st.session_state['link'])
    files = st.file_uploader("Upload your data", type=["csv", "txt", "json", "xlsx", "png", "jpg", "pdf"], accept_multiple_files=True)
    upload_file(files)
    # form_columns = st.columns(3,gap="large")
    # with form_columns[0]:
    st.session_state['submitted'] = st.form_submit_button("🧠 Click to Upload Knowledge")
    # responses = upload_file()


if (st.session_state['submitted'] and st.session_state['link'] != ""):
    file_meta = create_webpage_knowledge(st.session_state['link'])
    st.success("Knowledge Uploaded")
    response = create_context_for_file(file_meta)
    st.success("Context Created")
    st.session_state['submitted'] = False
    st.session_state['link'] = ""

if (st.session_state['submitted'] and files != []):
    responses = upload_file(files)
    st.success("Knowledge Uploaded")

    for each in responses:
        file_id = each['file_id']
        file_meta = get_file_meta(file_id)
        response = create_context_for_file(file_meta)
        st.success("Context Created for file %s " % file_meta['name'])
    response = create_context_for_file(file_meta)
    st.session_state['submitted'] = False


