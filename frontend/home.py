import streamlit as st
import logging
from utils import *

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

st.set_page_config(layout="wide")


if 'prompt' not in st.session_state:
    st.session_state['prompt'] = "Please click the get prompt button to get a prompt"

options = st.multiselect(
    'Configurations',
    ['GPT-3', 'GPT-3.5', 'GPT-4', 'knowledge with prompt', '50', '100', '200'])

text = "you selected " + ":red" + str(options) + ""
st.caption(text)

form = st.form("PlanForm",clear_on_submit=True)

if 'submitted' not in st.session_state:
    st.session_state['submitted'] = False

st.session_state['submitted'] = form.form_submit_button("⚙️ Click to Generate Plan")
form_input = form.text_input("Enter your Description of Plan", key="plan_input", value = st.session_state['prompt'])


if 'response' not in st.session_state:
    st.session_state['response'] = "Please generate a Plan above"

if (st.session_state['submitted'] and form_input != "") :
    send_to_api({"plan":form_input})
    st.session_state['response'] = get_from_api()
elif (st.session_state['submitted'] and form_input == ""):
    st.error("Please describe your plan before clicking submit")

#Showing Plan Part 
if st.session_state['response']:
    with st.form("Plans",clear_on_submit=False):
        # col_1,col_2 = st.columns(2,gap="large")
        # with col_1:
        #     executed = st.form_submit_button("🔥 Click to Execute", on_click=update_state,)
        # if (executed and ((st.session_state['response'] != "Please generate a Plan above") and 
        #                   (st.session_state['response'] != "Please generate a Plan above test"))):
        #     exectute_plan()
        #     st.session_state['response'] += "\n\n Plan is exectuted"
        # elif executed:
        #     st.session_state['response'] = "Please generate a Plan above test"
        # with col_2:
        #     changed = st.form_submit_button("👎 Change a new Plan")
        # if (changed and ((st.session_state['response'] != "Please generate a Plan above") and 
        #                   (st.session_state['response'] != "Please generate a Plan above test"))):
        #     st.session_state['response'] = update_from_api()
        st.session_state['response'] = 'Log in to Brightspace using your credentials. \n From the Brightspace homepage, click on the "Course Admin\" button located in the top right corner of the page.Click on the \"Course Offering Information\" option from the list of options.Locate the course you wish to activate, and click on the \"Edit Course\" link next to the course name.On the Edit Course page, scroll down to the \"Course Offering Information\" section.In the \"Status\" drop-down menu, select \"Active\".Click on the \"Save and Close\" button at the bottom of the page.'
        text_col1, text_col2 = st.columns(2)
        with text_col1:
            # text_col1 = st.text_area("Here is your plan:", key="code_input1",value = st.session_state['response'], height=300   )
            columns = st.columns(5,gap="large")
            with columns[0]:
                executed = st.form_submit_button("🔥 ", on_click=update_state,)
            if (executed and ((st.session_state['response'] != "Please generate a Plan above") and 
                            (st.session_state['response'] != "Please generate a Plan above test"))):
                exectute_plan()
                st.session_state['response'] += "\n\n Plan is exectuted"
            elif executed:
                st.session_state['response'] = "Please generate a Plan above test"
            with columns[4]:
                changed = st.form_submit_button("👎 ")
            if (changed and ((st.session_state['response'] != "Please generate a Plan above") and 
                            (st.session_state['response'] != "Please generate a Plan above test"))):
                st.session_state['response'] = update_from_api()
                
            text_col1 = st.text_area("Here is your plan:", key="code_input1",value = st.session_state['response'], height=300   )

        # text_col2 = st.text_area("Here is your plan:", key="code_input2",value = st.session_state['response'], height=50   )
        # text_col3 = st.text_area("Here is your plan:", key="code_input3",value = st.session_state['response'], height=50   )
        # text_col4 = st.text_area("Here is your plan:", key="code_input4",value = st.session_state['response'], height=50   )
        with text_col2:
            col_1,col_2 = st.columns(2,gap="large")
            with col_1:
                st.write("")
                st.write("")
                st.write("")
                # st.write("")
                st.write("")
            text_col2 = st.text_area("Here groundtruth:", key="code_input2",value = st.session_state['response'], height=300   )

st.session_state['response'] = st.session_state['response'].replace("\n\n Plan is exectuted", "")
st.write(st.session_state['response'])
st.sidebar.title("PlanGPT")
