from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, Item

main = Blueprint('main', __name__)

@main.route('/')
def index():
    items = Item.query.all()
    return render_template('index.html', items=items)

@main.route('/add', methods=['POST'])
def add_item():
    name = request.form.get('name')
    description = request.form.get('description')
    new_item = Item(name=name, description=description)
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/edit/<int:id>', methods=['POST'])
def edit_item(id):
    item = Item.query.get(id)
    item.name = request.form.get('name')
    item.description = request.form.get('description')
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/delete/<int:id>')
def delete_item(id):
    item = Item.query.get(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('main.index'))
