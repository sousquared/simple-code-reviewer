# Import the Secret Manager client library.
from google.cloud import secretmanager
from google.cloud.secretmanager_v1.types.resources import Secret
import json
import os

from exception.errors import SecretManagerApiError


def get_secret(project_id: str, secret_id: str) -> Secret:
    """
    Get information about the given secret. This only returns metadata about
    the secret container, not any secret material.
    """

    client = secretmanager.SecretManagerServiceClient()

    try:
        path = client.secret_version_path(project_id, secret_id, "latest")
        response = client.access_secret_version(name=path)
    except Exception as e:
        raise SecretManagerApiError(f"Failed to get secret: {e}")

    secret_str = response.payload.data.decode("UTF-8")
    secret_value = json.loads(secret_str)["api_key"]
    return secret_value


def get_secret_from_env(key: str) -> Secret:
    secret = os.environ.get(key)
    if secret:
        return json.loads(secret)["api_key"]
    else:
        raise SecretManagerApiError(f"Failed to get secret, key: {key}")
