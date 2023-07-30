from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class CreateSupplierForm(FlaskForm):
    nombre = StringField('Nombre', 
                           validators=[DataRequired()])

    localidad = StringField('Localidad', 
                           validators=[DataRequired()])

    telefono = StringField('Telefono', 
                           validators=[DataRequired()])

    direccion = StringField('Direccion', 
                           validators=[DataRequired()])
    
    submit = SubmitField('Guardar')

class UpdateSupplierForm(FlaskForm):
    nombre = StringField('nombre', 
                           validators=[DataRequired()])

    localidad = StringField('Localidad', 
                           validators=[DataRequired()])

    telefono = StringField('Telefono', 
                           validators=[DataRequired()])

    direccion = StringField('Direccion', 
                           validators=[DataRequired()])
     
    submit = SubmitField('Guardar')