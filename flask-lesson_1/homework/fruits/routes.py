from flask import Blueprint, render_template, request

fruits = Blueprint('fruits', __name__)

fruits_list = ['Apple', 'Banana', 'Lemon', 'Kiwi', 'Orange']


@fruits.route('/fruits')
@fruits.route('/fruits/<string:value>', methods=['GET', 'POST', 'DELETE'])
def fruit_manager(value=None):
    if request.method == "POST":
        fruits_list.append(value)
        return f"\"{value}\" added!"
    elif request.method == "DELETE":
        fruits_list.remove(value)
        return f"\"{value}\" deleted!"
    elif request.method == "GET":
        return render_template('fruits.html', title='Fruits', fruits_list=fruits_list)
