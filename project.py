from flask import request, g, redirect, url_for
from flask import Flask, jsonify, render_template
from db_setup import Base, User, Category, CatalogItem
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
import json


engine = create_engine('sqlite:///catalog.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)


@app.route('/')
@app.route('/catalog/')
def showCatalog():
    categories = session.query(Category).order_by('name').all()
    items = session.query(CatalogItem).order_by('id').limit(5)
    return render_template('home.html', categories=categories, items=items)


@app.route('/catalog/newcategory', methods=['GET', 'POST'])
def newCategory():
    categories = session.query(Category).order_by('name').all()
    if request.method == 'POST':
        if request.form['name']:
            newCategory = Category(name=request.form['name'])
            session.add(newCategory)
            session.commit()
            return redirect(url_for('showCatalog'))
    else:
        return render_template('newcategory.html', categories=categories)


@app.route('/catalog/<category>/items')
def viewCategory(category):
    categories = session.query(Category).order_by('name').all()
    currentCat = session.query(Category).filter_by(name=category).one()
    catId = currentCat.id
    items = session.query(CatalogItem).filter_by(category_id=catId).all()
    return render_template('viewcategory.html',
                           category=currentCat,
                           items=items,
                           categories=categories)


@app.route('/catalog/newitem', methods=['GET', 'POST'])
def newItem():
    categories = session.query(Category).order_by('name').all()
    if request.method == 'POST':
        if request.form['name']:
            newItem = CatalogItem(name=request.form['name'],
                                  description=request.form['description'],
                                  category_id=request.form['category'],
                                  )
            session.add(newItem)
            session.commit()
            return redirect(url_for('showCatalog'))
    else:
        categories = session.query(Category).all()
        return render_template('newitem.html', categories=categories)


@app.route('/catalog/<item>')
def viewItem(item):
    categories = session.query(Category).order_by('name').all()
    item = session.query(CatalogItem).filter_by(name=item).first()
    category = session.query(Category).filter_by(id=item.category_id).one()
    return render_template('viewitem.html',
                           item=item,
                           category=category,
                           categories=categories)


@app.route('/catalog/<item>/edit', methods=['GET', 'POST'])
def editItem(item):
    categories = session.query(Category).order_by('name').all()
    item = session.query(CatalogItem).filter_by(name=item).first()
    if request.method == 'POST':
        if request.form['name']:
            item.name = request.form['name']
            item.description = request.form['description']
            category_id = request.form['category']
            session.add(item)
            session.commit()
            return redirect(url_for('viewItem', item=request.form['name']))
    else:
        return render_template('edititem.html',
                               item=item,
                               categories=categories)


@app.route('/catalog/<item>/delete', methods=['GET', 'POST'])
def deleteItem(item):
    categories = session.query(Category).order_by('name').all()
    item = session.query(CatalogItem).filter_by(name=item).first()
    if request.method == 'POST':
        session.delete(item)
        session.commit()
        return redirect(url_for('showCatalog'))
    else:
        return render_template('deleteitem.html', item=item)


@app.route('/catalog.json')
def showJSON():
    categories = session.query(Category).order_by('name').all()
    return "Page for displaying JSON info."


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
