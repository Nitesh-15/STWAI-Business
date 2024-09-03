from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired

class BusinessDetailsForm(FlaskForm):
    business_name = StringField('Business Name', validators=[DataRequired()])
    business_type = StringField('Business Type', validators=[DataRequired()])
    industry = StringField('Industry', validators=[DataRequired()])
    mission_statement = TextAreaField('Mission Statement', validators=[DataRequired()])
    vision_statement = TextAreaField('Vision Statement', validators=[DataRequired()])
    founded = IntegerField('Founded', validators=[DataRequired()])
    founders = StringField('Founders', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    number_of_employees = IntegerField('Number of Employees', validators=[DataRequired()])
    business_stage = StringField('Business Stage', validators=[DataRequired()])
    business_model = StringField('Business Model', validators=[DataRequired()])
    turnover_year1 = FloatField('Turnover FY Year 1', validators=[DataRequired()])
    turnover_year2 = FloatField('Turnover FY Year 2', validators=[DataRequired()])
    turnover_year3 = FloatField('Turnover FY Year 3', validators=[DataRequired()])
    turnover_year4 = FloatField('Turnover FY Year 4', validators=[DataRequired()])
    gross_profit = FloatField('Gross Profit %', validators=[DataRequired()])
    net_profit = FloatField('Net Profit %', validators=[DataRequired()])
    monthly_inflow = FloatField('Monthly Inflow', validators=[DataRequired()])
    monthly_outflow = FloatField('Monthly Outflow', validators=[DataRequired()])
    monthly_cashflow = FloatField('Monthly Cashflow', validators=[DataRequired()])
    fixed_expense1 = FloatField('Monthly Fixed Expense 1', validators=[DataRequired()])
    fixed_expense2 = FloatField('Monthly Fixed Expense 2', validators=[DataRequired()])
    fixed_expense3 = FloatField('Monthly Fixed Expense 3', validators=[DataRequired()])
    fixed_expense4 = FloatField('Monthly Fixed Expense 4', validators=[DataRequired()])
    variable_expenses = FloatField('Variable Expenses', validators=[DataRequired()])
    cash_flow_projection = FloatField('Cash Flow Projection', validators=[DataRequired()])
    overdraft_limit = FloatField('Overdraft Account Limit', validators=[DataRequired()])
    submit = SubmitField('Submit')

# class loginForm(FlaskForm) :
# 
