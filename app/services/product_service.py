from app.utils.external_api import fetch_external_data

def get_product_details(product_id):
    """
    Obtém detalhes de um produto a partir de uma API externa.

    Args:
        product_id (str): ID do produto.

    Returns:
        dict: Detalhes do produto.
    """
    endpoint = f"products/{product_id}"
    return fetch_external_data(endpoint)
