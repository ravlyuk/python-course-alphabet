from flask import Blueprint, render_template, request

vegetables = Blueprint('vegetables', __name__, )

vegetables_list = ['Tomato', 'Potato', 'Cucumber', 'Pepper', 'Сabbage']


@vegetables.route("/vegetables")
def vegetables_main():
    return render_template('vegetables.html', title='Vegetables', vegetables_list=vegetables_list)


@vegetables.route('/vegetables/<string:value>', methods=['POST'])
def vegetables_post(value=None):
    vegetables_list.append(value)
    return f"\"{value}\" added!"


@vegetables.route('/vegetables/<string:value>', methods=['DELETE'])
def vegetables_delete(value=None):
    vegetables_list.remove(value)
    return f"\"{value}\" deleted!"
