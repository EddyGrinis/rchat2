from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo

# lai definetu formu, jadod tai vards
class RegistrationForm(FlaskForm):
    """ Registration form """

    # formai būs trīs lauki: un pievieno validators
    username = StringField('username_label',
        validators=[InputRequired(message="Lietotajvards ir obligats"), Length(min=4, max=25, message="Lietotajvardam jabut no 4 lidz 25 simbolus garam")])
    password = PasswordField('password_label',
        validators=[InputRequired(message="Parole ir obligata"), Length(min=4, max=25, message="Parolei jabut no 4 lidz 25 simbolus garai")])
    confirm_pswd = PasswordField('confirm_pswd_label',
        validators=[InputRequired(message="Parole ir obligata"), EqualTo('password', message="Parolem jasakrit")])
    submit_button = SubmitField('Create')
