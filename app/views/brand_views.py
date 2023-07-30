from flask import Blueprint, render_template, redirect, url_for, request, flash
from models.brand import Brand
from forms.brand_forms import CreateBrandForm, UpdateBrandForm

brand_views = Blueprint ('marca', __name__)

@brand_views.route('/brand/')
def brand():
    brand = Brand.get_all()
    return render_template('brand/brand.html',
                           brand=brand)

@brand_views.route('/brand/create/', methods=('GET','POST'))
def create_bra():
    form = CreateBrandForm()
    if form.validate_on_submit():
            nombre = form.nombre.data

            bra = Brand(nombre)
            bra.save()
            return redirect(url_for('marca.brand'))
    
    return render_template('brand/create_bra.html', form=form)

@brand_views.route('/brand/<int:id_marca>/update/', methods=('GET', 'POST'))
def update_bra(id_marca):
    form = UpdateBrandForm() #Obtener Cat desde id
    bra = Brand.get(id_marca)
    if form.validate_on_submit():
        bra.nombre = form.nombre.data

        bra.save()
        return redirect(url_for('marca.brand'))
    form.nombre.data = bra.nombre

    return render_template('brand/create_bra.html', form=form) #enviar datos a form

@brand_views.route('/brand/<int:id_marca>/delete/', methods=('POST', 'GET'))
def delete_bra(id_marca):
    #Obtener Cat desde id
    bra = Brand.get(id_marca)
    bra.delete()
    #enviar datos a form
    return redirect(url_for('marca.brand'))