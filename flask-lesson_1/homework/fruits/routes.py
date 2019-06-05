from flask import Blueprint, render_template, request

fruits = Blueprint('fruits', __name__)

fruits_list = ['Apple', 'Banana', 'Lemon', 'Kiwi', 'Orange']


@fruits.route('/fruits')
def fruits_main():
    return render_template('fruits.html', title='Fruits', fruits_list=fruits_list)


@fruits.route('/fruits/<string:value>', methods=['POST'])
def fruit_post(value=None):
    fruits_list.append(value)
    return f"\"{value}\" added!"


@fruits.route('/fruits/<string:value>', methods=['DELETE'])
def fruit_delete(value=None):
    fruits_list.remove(value)
    return f"\"{value}\" deleted!"
