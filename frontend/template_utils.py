from utils import get, post, requests, json
import config as config
import random

def create_template(name, description, template, template_type, webbot_id=config.WEBBOT_ID):

    """ 
     creates a template for a webbot
    """

    url = config.BASE_URL + "template"
    
    data = {
        'webbot_id': webbot_id,
        'name': name,
        'description': description,
        'template': template,
        'template_type': template_type
    }
    response = post(url, data=data)
    return True


def get_templates(webbot_id=config.WEBBOT_ID, template_type="system_message"):
    """ 
     gets all templates for a webbot
    """
    url = config.BASE_URL + "template?webbot_id={webbot_id}&template_type={template_type}".format(webbot_id=webbot_id, template_type=template_type)
    response = get(url)
    return response


def get_completion(completion_id):
    """ 
     gets all templates for a webbot
    """
    url = config.BASE_URL + "completion/{completion_id}".format(completion_id=completion_id)
    response = get(url)
    return response


def create_completions(instruction,system_message_template_ids, webbot_id=config.WEBBOT_ID, conversation_id=config.CONVERSATION_ID):
    """ 
     creates a template for a webbot
    """

    if len(system_message_template_ids) == 2:
        random_1 = 0
        random_2 = 1
    else:
        random_1 = random.randint(0, len(system_message_template_ids)-1)
        random_2 = random.randint(0, len(system_message_template_ids)-1)

    template_ids = [system_message_template_ids[random_1], system_message_template_ids[random_2]]
    completions = []


    for template_id in template_ids:
    
        payload = {
                    "webbot_id": webbot_id,
                    "conversation_id": 0,
                    "system_message_template_id": template_id,
                    "user_message": instruction,
                    }
        
        print(payload)
        
        url = config.BASE_URL + "completion"
        response = post(url, data=payload)
        completions.append(response)

    ground_truth = response['ground_truth_answer']
    retrievals = response['retrievals']

    return completions, ground_truth, retrievals


def update_ground_truth(completion_id, ground_truth_answer):
    

    payload = {
                "ground_truth_answer": ground_truth_answer
            }
    
    url = config.BASE_URL + "completion/" + str(completion_id)
    response = requests.put(url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
    status_code = response.status_code
    if str(status_code).startswith('2'):
        print("Data sent successfully to the API! %s ", url)
        # print("Response: %s ", response.content)
        try:
            return json.loads(response.content)
        except:
            print("Error parsing response from the update ground truth api")
            print(response.content)
            return response.content

    else:
        print('Error sending data to the API \n %s : \n %s ', url,response.content)
        return None


def create_evaluation(completion_id, completion_score, retrieval_score, webbot_id = config.WEBBOT_ID):
    """ 
     creates a template for a webbot
    """

    payload = {
                "webbot_id": webbot_id,
                "completion_id": completion_id,
                "completion_score": completion_score,
                "retrieval_score": retrieval_score,
                "evaluation_model" : "human"
            }
    
    url = config.BASE_URL + "evaluation"
    response = post(url, data=payload)
    return response


def create_webpage_knowledge(url, webbot_id=config.WEBBOT_ID):
    """ 
     creates a template for a webbot
    """

    payload = {
                "webbot_id": webbot_id,
                "source_url": url,
                "name" : url.split("/")[-1],
                "file_type": "webpage"
            }
    
    url = config.BASE_URL + "files"
    file_meta = post(url, data=payload)
    return file_meta


def create_context_for_file(file_meta):
    payload = file_meta
    url = config.BASE_URL + "context/create"
    response = post(url, data=payload)
    print(response)
    return response


