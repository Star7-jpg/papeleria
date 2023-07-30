from flask import Blueprint, render_template, redirect, url_for, request, flash
from models.categories import Category
from forms.category_forms import CreateCategoryForm, UpdateCategoryForm

category_views = Blueprint ('category', __name__)

@category_views.route('/categories/')
def categories():
    categories = Category.get_all()
    return render_template('categories/categories.html',
                           categories=categories)

@category_views.route('/categories/create/', methods=('GET','POST'))
def create_cat():
    form = CreateCategoryForm()
    if form.validate_on_submit():
            nombre = form.nombre.data
            cat = Category(nombre)
            cat.save()
            return redirect(url_for('category.categories'))
    
    return render_template('categories/create_cat.html', form=form)

@category_views.route('/categories/<int:id_categoria>/update/', methods=('GET', 'POST'))
def update_cat(id_categoria):
    form = UpdateCategoryForm() #Obtener Cat desde id
    cat = Category.get(id_categoria)
    if form.validate_on_submit():
         cat.nombre = form.nombre.data

         cat.save()
         return redirect(url_for('category.categories'))
    form.nombre.data = cat.nombre

    return render_template('categories/create_cat.html', form=form) #enviar datos a form

@category_views.route('/categories/<int:id_categoria>/delete/', methods=('POST', 'GET'))
def delete_cat(id_categoria):
    #Obtener Cat desde id
    cat = Category.get(id_categoria)
    cat.delete()
    #enviar datos a form
    return redirect(url_for('category.categories'))