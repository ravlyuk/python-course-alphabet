from flask import Blueprint, render_template, request

fruits = Blueprint('fruits', __name__)

fruits_list = ['Apple', 'Banana', 'Lemon', 'Kiwi', 'Orange']


@fruits.route('/fruits')
def fruit_manager():
    return render_template('fruits.html', title='Fruits', fruits_list=fruits_list)

@fruits.route('/fruits/<string:value>', methods=['POST', 'DELETE'])
def fruit_route_manager(value=None):
    if request.method == "POST":
        fruits_list.append(value)
        return f"\"{value}\" added!"
    elif request.method == "DELETE":
        fruits_list.remove(value)
        return f"\"{value}\" deleted!"
