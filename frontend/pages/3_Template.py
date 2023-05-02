import streamlit as st
import logging
from utils import *
from template_utils import *

if 'type_option' not in st.session_state:
    st.session_state['type_option'] = " "
if 'template_name' not in st.session_state:
    st.session_state['template_name'] = " "
if 'template_description' not in st.session_state:
    st.session_state['template_description'] = " "
if 'template_submitted' not in st.session_state:
    st.session_state['template_submitted'] = None
if 'template_content' not in st.session_state:
    st.session_state['template_content'] = " "

st.subheader("Template")

with st.form("TemplateContentForm", clear_on_submit=True):
    # template_submitted = st.form_submit_button("💡Save and Generate this Template ", on_click=update_state_template_submission,)
    st.session_state['type_option'] = st.selectbox('Type of the template?',('system_message', 'user_message'))
    st.session_state['template_name'] =  st.text_input("Enter the name of your template", key = 'template_name_input')
    st.session_state['template_description'] = st.text_input("Enter the description of your template", key = 'template_description_input')
    st.session_state['template_content'] = st.text_area("Enter the content of your template", key="template_content_input", height=300   )
    template_submitted = st.form_submit_button("💡Save and Generate this Template ", on_click=update_state_template_submission,)
    if ((template_submitted) and ((st.session_state['template_name'] or st.session_state['template_description'] or st.session_state['template_content'])!= " ")):
        create_template(st.session_state['template_name'], st.session_state['template_description'], st.session_state['template_content'], st.session_state['type_option'])
        st.success("Template Saved")
    elif ((template_submitted) and ((st.session_state['template_name'] or st.session_state['template_description'] or st.session_state['template_content']) == " ")):
        st.error("Fill in everything")
