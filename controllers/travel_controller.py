from flask import Flask, render_template

from repositories import destination_repository

from flask import Blueprint

destinations_blueprint = Blueprint("destinations", __name__)

@destinations_blueprint.route("/destinations")
def destinations():
    destinations = destination_repository.select_all()
    return render_template("destinations/index.html", all_destinations = destinations)