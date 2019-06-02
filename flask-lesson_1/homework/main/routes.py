from flask import Blueprint, render_template, redirect, url_for

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/main")
def main_func():
    return render_template("main.html", title="Main")


@main.route("/porn")
def porn():
    return redirect(url_for('vegetables.vegetables_manager'))


@main.route("/error")
def error():
    return render_template("error_404.html", title='Error 404')
