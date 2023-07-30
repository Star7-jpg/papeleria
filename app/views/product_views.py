from flask import Blueprint, render_template, redirect, url_for, request, flash
from models.product import Product
from forms.product_forms import CreateProductForm, UpdateProductForm

product_views = Blueprint ('producto', __name__)

@product_views.route('/product/')
def product():
    product = Product.get_all()
    return render_template('product/product.html',
                           product=product)

@product_views.route('/product/create/', methods=('GET','POST'))
def create_pro():
    form = CreateProductForm()
    if form.validate_on_submit():
            nombre = form.nombre.data
            precio = form.precio.data
            descripcion = form.descripcion.data
            id_marca = form.id_marca.data
            id_categoria = form.id_categoria.data
            pro = Product(nombre, precio, descripcion, id_marca, id_categoria)
            pro.save()
            return redirect(url_for('producto.product'))
    
    return render_template('product/create_pro.html', form=form)

@product_views.route('/product/<int:id_producto>/update/', methods=('GET', 'POST'))
def update_pro(id_producto):
    form = UpdateProductForm() #Obtener Cat desde id
    pro = Product.get(id_producto)
    if form.validate_on_submit():
        pro.nombre = form.nombre.data
        pro.precio = form.precio.data
        pro.descripcion = form.descripcion.data
        pro.id_marca = form.id_marca.data
        pro.id_categoria = form.id_categoria.data
        pro.save()
        return redirect(url_for('producto.product'))
    form.nombre.data = pro.nombre
    form.precio.data = pro.precio
    form.descripcion.data = pro.descripcion
    form.id_marca.data = pro.id_marca
    form.id_categoria.data = pro.id_categoria
    return render_template('product/create_pro.html', form=form) #enviar datos a form

@product_views.route('/product/<int:id_producto>/delete/', methods=('POST', 'GET'))
def delete_pro(id_producto):
    #Obtener Cat desde id
    pro = Product.get(id_producto)
    pro.delete()
    #enviar datos a form
    return redirect(url_for('producto.product'))