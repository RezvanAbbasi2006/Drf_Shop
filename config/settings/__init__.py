# import os
from split_settings.tools import include

include("aws.py")

# print("LOGGG   :", os.environ.get("ENV_NAME"))
# if os.environ.get("ENV_NAME") == 'env':
#     from .aws import *
# else:
#     from .local import *
