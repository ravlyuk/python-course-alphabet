from flask import Blueprint, render_template, request

vegetables = Blueprint('vegetables', __name__, )

vegetables_list = ['Tomato', 'Potato', 'Cucumber', 'Pepper', 'Сabbage']




@vegetables.route("/vegetables")
def vegetables_manager():
    return render_template('vegetables.html', title='Vegetables', vegetables_list=vegetables_list)

@vegetables.route('/vegetables/<string:value>', methods=['POST', 'DELETE'])
def vegetables_route_manager(value=None):
    if request.method == "POST":
        vegetables_list.append(value)
        return f"\"{value}\" added!"
    elif request.method == "DELETE":
        vegetables_list.remove(value)
        return f"\"{value}\" deleted!"
