from flask import Blueprint, render_template, request

vegetables = Blueprint('vegetables', __name__, )

vegetables_list = ['Tomato', 'Potato', 'Cucumber', 'Pepper', 'Сabbage']


@vegetables.route("/vegetables")
@vegetables.route('/vegetables/<string:value>', methods=['GET', 'POST', 'DELETE'])
def vegetables_manager(value=None):
    if request.method == "POST":
        vegetables_list.append(value)
        return f"\"{value}\" added!"
    elif request.method == "DELETE":
        vegetables_list.remove(value)
        return f"\"{value}\" deleted!"
    elif request.method == "GET":
        return render_template('vegetables.html', title='Vegetables', vegetables_list=vegetables_list)
