import os

OAUTH_REDIRECT_URI = os.getenv("OAUTH_REDIRECT_URI", 'http://localhost:8501')
CONVERSATION_BASE_URL = os.getenv("CONVERSATION_BASE_URL", 'https://r5mpc7pa7d.us-east-1.awsapprunner.com/api')
KNOWLEDGE_BASE_URL = os.getenv("KNOWLEDGE_BASE_URL", 'https://jgpyxxfqz3.us-east-1.awsapprunner.com/api')
EMBEDDING_BASE_URL = os.getenv("EMBEDDING_BASE_URL", 'https://55vpqqfcy6.us-east-1.awsapprunner.com/api')
WEEBOT_BASE_URL = os.getenv("WEEBOT_BASE_URL", 'https://mtvwupdvb3.us-east-1.awsapprunner.com/api')
# BASE_URL = os.getenv("BASE_URL", 'https://j3vvivg3pn.us-east-1.awsapprunner.com/api/')
WEBBOT_ID = os.getenv("WEBBOT_ID", 1)
CONVERSATION_ID = os.getenv("CONVERSATION_ID", 0)
BASE_URL = os.getenv("BASE_URL", 'http://localhost:8000/api/')
