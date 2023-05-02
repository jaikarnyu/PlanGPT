import streamlit as st
import logging
from utils import *
from template_utils import *

logging.basicConfig(level=logging.DEBUG)
st.set_option('deprecation.showfileUploaderEncoding', False)


logger = logging.getLogger(__name__)

st.set_page_config(layout="wide")

if 'webbot_id' not in st.session_state:
    st.session_state['webbot_id'] = 0

# Session State Instruction
if "instruction" not in st.session_state:
    # st.session_state["instruction"] = "Please click the get instruction button to get a instruction"
    st.session_state["instruction"] = ""

#Session State Submitted
if 'submitted' not in st.session_state:
    st.session_state['submitted'] = False


system_prompt_list = get_templates(template_type="system_message")
user_prompt_list = get_templates(template_type="user_message")
names = [prompt['name'] for prompt in system_prompt_list]
ids = [prompt['id'] for prompt in system_prompt_list]
st.session_state['system_prompt_dict'] = dict(zip(names,ids))

#instructionForm
with st.form("InstructionForm",clear_on_submit=True):
    # form_columns = st.columns(3,gap="large")
    # with form_columns[0]:
    #     st.session_state['submitted'] = st.form_submit_button("⚙️ Click to Generate Completion")
    # with form_columns[1]:
    #     st.form_submit_button("⏭️ Next")
    form_input = st.text_input("Enter Instruction", key="instruction_input", value = st.session_state['instruction'])
  
    
    system_template =  st.multiselect('Select System Prompts',names)
    user_template =  st.multiselect('Select User Prompts',user_prompt_list)
    form_columns = st.columns(3,gap="large")
    with form_columns[0]:
        st.session_state['submitted'] = st.form_submit_button("⚙️ Click to Generate Completion")

if (st.session_state['submitted'] and form_input != "" and system_template != []) :
    system_template_ids = [st.session_state['system_prompt_dict'][name] for name in system_template]
    completions, ground_truth_answer, retrievals = create_completions(form_input,system_template_ids)
    st.session_state['completion1'] = completions[0]
    st.session_state['completion2'] = completions[1]
    st.session_state['retrieval'] = retrievals
    st.session_state['groundtruth'] = ground_truth_answer
    st.success("Completion Generated")
    st.session_state['submitted'] = False




#Session State Completion1
if 'completion1' not in st.session_state:
    st.session_state['completion1']= {"assistant_message" : "Please generate a Completion above"}

elif (st.session_state['submitted'] and form_input == ""):
    st.error("Please describe your plan before clicking submit")

#Session State Completion2
if 'completion2' not in st.session_state:
    st.session_state['completion2']= {"assistant_message" : "Please generate a Completion above"}

elif (st.session_state['submitted'] and form_input == ""):
    st.error("Please describe your plan before clicking submit")

#Session State Retrieval
if 'retrieval' not in st.session_state:
    st.session_state['retrieval'] = "Please generate a Completion above"
elif (st.session_state['submitted'] and form_input == ""):
    st.error("Please describe your plan before clicking submit")

#Session State GroundTruth
if 'groundtruth' not in st.session_state:
    st.session_state['groundtruth'] = "Please generate a Completion above"
elif (st.session_state['submitted'] and form_input == ""):
    st.error("Please describe your plan before clicking submit")

# st.session_state['completion1'] = 'Completion1Demo'
# st.session_state['completion2'] = 'Completion2Demo'
# st.session_state['retrieval'] = 'retrievalDemo'
# st.session_state['retrieval'] = 'GroundtruthDemo'

#Showing Plan Part 
if st.session_state['completion1']:
    with st.form("Plans",clear_on_submit=True):

        # st.session_state['evaluated'] = st.form_submit_button("✅ Submit the Evaluation")
        
        generated_response, groundtruth_prompt = st.columns(2)
        with generated_response:
            completion1_rating = st.slider('Rate Completion1',min_value=1, max_value=10, step=1,value=st.session_state.get("completion_1_rating", 5), key="completion1_rating")
            generated_response = st.text_area("Completion1:", key="generated_response",value = st.session_state['completion1']['assistant_message'], height=200   )

            completion2_rating = st.slider('Rate Completion2',min_value=1, max_value=10, step=1,value=st.session_state.get("completion_2_rating", 5), key='completion2_rating')
            generated_response2 = st.text_area("Completion2:", key="generated_response2",value = st.session_state['completion2']['assistant_message'], height=200   )

        with groundtruth_prompt:
            
            groundtruth_prompt = st.text_area("Groundtruth:", key="groundtruth_prompt",value = st.session_state['groundtruth'], height=300   )
            retrieval_rating = st.slider('Rate Retrieval',min_value=1, max_value=10, step=1,value=st.session_state.get("context_retrieval_rating", 5), key='retrieval_rating')
            retrieval_prompt = st.text_area("Retrieval:", key="retrieval_prompt",value = st.session_state['retrieval'], height=200   )
        
        st.session_state['evaluated'] = st.form_submit_button("✅ Submit the Evaluation")

#Sanity Check
# completion1_rating,completion2_rating,retrieval_rating
# st.write('completion1_rating:', completion1_rating)
# st.write('completion2_rating:', completion2_rating)
# st.write('retrieval_rating:', retrieval_rating)
# st.write('groundtruth',groundtruth_prompt)
# st.write(st.session_state['groundtruth'])
# st.session_state['response'] = st.session_state['response'].replace("\n\n Plan is exectuted", "")
# st.write(st.session_state['response'])
st.sidebar.title("PlanGPT")

if st.session_state['evaluated'] :
    # st.write(st.session_state['completion1'])
    create_evaluation(st.session_state['completion1']['id'], completion1_rating,retrieval_rating)
    update_ground_truth(st.session_state['completion1']['id'], groundtruth_prompt)
    create_evaluation(st.session_state['completion2']['id'], completion2_rating,retrieval_rating)
    update_ground_truth(st.session_state['completion2']['id'], groundtruth_prompt)
    st.session_state['completion_1_rating'] = completion1_rating
    st.session_state['completion_2_rating'] = completion2_rating
    st.session_state['context_retrieval_rating'] = retrieval_rating
    st.success("Evaluation Submitted")
    st.session_state['evaluated'] = False


