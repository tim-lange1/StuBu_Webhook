from flask import Blueprint, jsonify, request

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    return jsonify(
        {
            'status': 200,
            'message': 'Webhook is working.'
        }
    )
