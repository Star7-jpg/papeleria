from flask import Blueprint, render_template, redirect, url_for, request, flash
from models.sale import Sale
from forms.sale_forms import CreateSaleForm, UpdateSaleForm

sale_views = Blueprint ('ventas', __name__)

@sale_views.route('/sale/')
def sale():
    sale = Sale.get_all()
    return render_template('sale/sale.html',
                           sale=sale)

@sale_views.route('/sale/create/', methods=('GET','POST'))
def create_sal():
    form = CreateSaleForm()
    if form.validate_on_submit():
            fecha = form.fecha.data
            total = form.total.data
            id_producto = form.id_producto.data
            id_usuario = form.id_usuario.data

            sal = Sale(fecha, total, id_producto, id_usuario)
            sal.save()
            return redirect(url_for('ventas.sale'))
    
    return render_template('sale/create_sal.html', form=form)
