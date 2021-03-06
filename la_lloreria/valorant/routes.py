from la_lloreria.valorant.utils import get_account_data, get_data_points_mmr, get_elo, get_data_points_matches
from flask import Blueprint

valorant = Blueprint('valorant', __name__)

@valorant.route('/mmr/<user>/<id>', methods=["GET"])
def mmr(user, id):
    return get_data_points_mmr(user, id)

@valorant.route('/elo/<user>/<id>', methods=["GET"])
def elo(user, id):
    print(user)
    return get_elo(user, id)

@valorant.route('/matches/<user>/<id>', methods=["GET"])
def matches(user, id):
    return get_data_points_matches(user, id)

@valorant.route('/account/<user>/<id>', methods=["GET"])
def account(user, id):
    return get_account_data(user, id)