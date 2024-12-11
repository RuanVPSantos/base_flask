from flask import Blueprint, jsonify
from app.services.product_service import get_product_details

product_bp = Blueprint('v1_product', __name__)

@product_bp.route('/<product_id>', methods=['GET'])
def product_details(product_id):
    """
    Rota para obter detalhes de um produto.

    Args:
        product_id (str): ID do produto.

    Returns:
        dict: Detalhes do produto.
    """
    try:
        product = get_product_details(product_id)
        return jsonify(product)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
