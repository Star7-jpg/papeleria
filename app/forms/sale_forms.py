from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class CreateSaleForm(FlaskForm):
    fecha = StringField('Fecha', 
                           validators=[DataRequired()])

    total = StringField('Total', 
                           validators=[DataRequired()])

    id_producto = StringField('Producto', 
                           validators=[DataRequired()])

    id_usuario = StringField('Usuario', 
                           validators=[DataRequired()])
    
    
    submit = SubmitField('Guardar')

class UpdateSaleForm(FlaskForm):
    fecha = StringField('Fecha', 
                           validators=[DataRequired()])

    total = StringField('Total', 
                           validators=[DataRequired()])

    id_producto = StringField('Producto', 
                           validators=[DataRequired()])

    id_usuario = StringField('Usuario', 
                           validators=[DataRequired()])
    
     
    submit = SubmitField('Guardar')