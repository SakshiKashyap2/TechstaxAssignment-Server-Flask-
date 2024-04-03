from flask import Blueprint, json, request, jsonify

webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')




@webhook.route('/test', methods=["GET"])
def home():
    return "Server Active!"


@webhook.route('/receiver', methods=["POST"])
def receiver():

    data=request.get_json()
    return jsonify(data),201
