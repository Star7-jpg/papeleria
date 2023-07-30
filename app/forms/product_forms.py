from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class CreateProductForm(FlaskForm):
    nombre = StringField('Nombre', 
                           validators=[DataRequired()])

    precio = StringField('precio', 
                           validators=[DataRequired()])

    descripcion = StringField('descripcion', 
                           validators=[DataRequired()])

    id_marca = StringField('marca', 
                           validators=[DataRequired()])
    
    id_categoria = StringField('categoria', 
                           validators=[DataRequired()])
    
    submit = SubmitField('Guardar')

class UpdateProductForm(FlaskForm):
    nombre = StringField('nombre', 
                           validators=[DataRequired()])

    precio = StringField('precio', 
                           validators=[DataRequired()])

    descripcion = StringField('descripcion', 
                           validators=[DataRequired()])

    id_marca = StringField('marca', 
                           validators=[DataRequired()])
    
    id_categoria = StringField('categoria', 
                           validators=[DataRequired()])
     
    submit = SubmitField('Guardar')