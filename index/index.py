from flask import Blueprint, render_template

index_blueprint = Blueprint("index_blueprint", __name__)


@index_blueprint.route("/", methods=["GET"])
@index_blueprint.route("/index", methods=["GET"])
def index():
    return "Aqui é o index."

    # return render_template("index.html")
