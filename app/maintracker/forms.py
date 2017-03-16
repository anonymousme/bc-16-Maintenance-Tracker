from flask.ext.wtf import Form
from wtforms import StringField, SelectField, SubmitField, TextAreaField, PasswordField
from wtforms import ValidationError
from wtforms.validators import Required, length
from wtforms.validators import Required, Email, Length, EqualTo
from ..model import User




class MaintananceForm(Form):
	item_name = StringField('Item Name', validators=[Required()])
	item_issue = StringField('Item Issue', validators=[Required()])
	item_type = StringField('Item Type', validators=[Required()])
	status = SelectField(
        'Status',
        choices=[('good', 'Good'), ('needs repair', 'Needs Repair'), ('Under Repair', 'Under Repair')]
    )
	submit = SubmitField('Raise')

class ApproveForm(Form):
	item_name = StringField('Item Name', validators=[Required()])
	item_issue = StringField('Item Issue', validators=[Required()])
	item_type = StringField('Item Type', validators=[Required()])
	comment = TextAreaField("Admin's Comment")
	submit = SubmitField('Approve')


class AddUserForm(Form):

	first_name = StringField('FirstName', validators=[Required(), Length(1, 20)])
	last_name = StringField('LastName', validators=[Required(), Length(1, 20)])
	email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
	phone_number = StringField('PhoneNumber', validators=[Required(), Length(1, 64)])
	password = PasswordField('Password', validators=[Required(), EqualTo('conf_password', message='Passwords must match.')])
	conf_password = PasswordField('Confirm password', validators=[Required()])
	submit = SubmitField('Add User')

	
	def validate_email(self, field):
		
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Email already registered.')	