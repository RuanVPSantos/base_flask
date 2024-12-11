import requests
from flask import current_app

def fetch_external_data(endpoint: str, params: dict = None):
    """
    Realiza uma requisição GET para a API externa.

    Args:
        endpoint (str): O endpoint da API externa.
        params (dict): Parâmetros opcionais para a requisição.

    Returns:
        dict: Resposta da API externa.
    """
    base_url = current_app.config.get("EXTERNAL_API_BASE_URL")

    headers = {
        "Content-Type": "application/json",
    }

    response = requests.get(f"{base_url}/{endpoint}", headers=headers, params=params)
    
    if response.status_code != 200:
        response.raise_for_status()

    return response.json()