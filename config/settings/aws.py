from pathlib import Path

from config.env import env

BASE_DIR = Path(__file__).resolve().parent.parent.parent

if env("USE_ARVAN_BUCKET", cast=bool, default=False):
    """Config Arvan Cloud Storage"""

    DEFAULT_FILE_STORAGE = env("DEFAULT_FILE_STORAGE", cast=str)
    AWS_ACCESS_KEY_ID = env("ARVAN_ACCESS_KEY_ID", cast=str)
    AWS_SECRET_ACCESS_KEY = env("ARVAN_SECRET_ACCESS_KEY", cast=str)

    AWS_STORAGE_BUCKET_NAME = env("ARVAN_STORAGE_BUCKET_NAME", cast=str)
    AWS_S3_REGION_NAME = env("ARVAN_STORAGE_REGION_NAME", cast=str)

    AWS_S3_ENDPOINT_URL = env("ARVAN_ENDPOINT_URL", cast=str)

    AWS_STORAGE_DEFAULT_ACL = env("ARVAN_STORAGE_DEFAULT_ACL", cast=str)
    AWS_DEFAULT_ACL = env("ARVAN_STORAGE_DEFAULT_ACL", cast=str)


