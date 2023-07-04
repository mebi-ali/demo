import os

import requests  # type: ignore
from base_logger import logger
from dotenv import load_dotenv

load_dotenv()


def get_api_data(url: str) -> dict:
<<<<<<< HEAD
=======
    """
    Retrieve data from the specified API endpoint.

    Parameters:
    - url (str): The URL of the API endpoint.

    Returns:
    - dict: The JSON response data from the API.
    """
>>>>>>> f1cddabe60ee508a6e5c931f110b118b29f0ebdb
    response = requests.get(url)
    try:
        response.raise_for_status()
    except requests.HTTPError:
        err_msg = f"Error {response.status_code} occurred while accessing {url}"
        logger.error(err_msg)
        raise
    return response.json()


urls = {
    "appointment": f"{os.getenv('BASE_URL')}/appointment",
    "councillor": f"{os.getenv('BASE_URL')}/councillor",
    "patient_councillor": f"{os.getenv('BASE_URL')}/patient_councillor",
    "rating": f"{os.getenv('BASE_URL')}/rating",
}


if __name__ == "__main__":
    data = {key: get_api_data(val) for key, val in urls.items()}
