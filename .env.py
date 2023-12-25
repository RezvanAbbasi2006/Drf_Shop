# ARVAN CLOUD SETTING
from config.settings.base import env

DEFAULT_AUTO_FIELD = env('django.db.models.BigAutoField')
DEFAULT_FILE_STORAGE = env('storages.backends.s3.S3Storage')
ARVAN_ACCESS_KEY_ID = env('7035f69d-cee6-44a5-a8ad-d32a627d0ce6')
ARVAN_SECRET_ACCESS_KEY = env('ae2d5eaf26fb86cdc3ba6941594759efa9b7270f466187809207db094bef620b')
ARVAN_STORAGE_BUCKET_NAME = env('gapbucket22')
ARVAN_ENDPOINT_URL = env('s3.ir-thr-at1.arvanstorage.ir')
ARVAN_STORAGE_REGION_NAME = env('ir-tehran')
AWS_S3_REGION_NAME = env('me-south-1')
ARVAN_STORAGE_DEFAULT_ACL = 'public-read'

# EMAIL SETTING
EMAIL_HOST_USER = "your email"
EMAIL_HOST_PASSWORD = "your password"

SECRET_KEY = env('django-insecure-9c4%pa+gw@hfk1^5ke*u7etn^vu1mu2vganw9((pcek38d$45f')
