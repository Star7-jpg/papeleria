from flask import Flask

#Importar vistas
from views.home_views import home_views
from views.category_views import category_views
from views.error_views import error_views
from views.supplier_views import supplier_views
from views.brand_views import brand_views
from views.user_views import user_views
from views.product_views import product_views
from views.sale_views import sale_views

app = Flask(__name__)
app.config['SECRET_KEY'] = 'My Secret Key'

#Registrar Views
app.register_blueprint(home_views)
app.register_blueprint(category_views)
app.register_blueprint(supplier_views)
app.register_blueprint(brand_views)
app.register_blueprint(user_views)
app.register_blueprint(product_views)
app.register_blueprint(sale_views)

app.register_blueprint(error_views)

if __name__ == '__main__':
    app.run(debug=True)