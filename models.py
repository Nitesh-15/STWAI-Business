from app import db

class BusinessDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_name = db.Column(db.String(128))
    business_type = db.Column(db.String(128))
    industry = db.Column(db.String(128))
    mission_statement = db.Column(db.Text)
    vision_statement = db.Column(db.Text)
    founded = db.Column(db.Integer)
    founders = db.Column(db.String(256))
    location = db.Column(db.String(128))
    number_of_employees = db.Column(db.Integer)
    business_stage = db.Column(db.String(128))
    business_model = db.Column(db.String(128))
    turnover_year1 = db.Column(db.Float)
    turnover_year2 = db.Column(db.Float)
    turnover_year3 = db.Column(db.Float)
    turnover_year4 = db.Column(db.Float)
    gross_profit = db.Column(db.Float)
    net_profit = db.Column(db.Float)
    monthly_inflow = db.Column(db.Float)
    monthly_outflow = db.Column(db.Float)
    monthly_cashflow = db.Column(db.Float)
    fixed_expense1 = db.Column(db.Float)
    fixed_expense2 = db.Column(db.Float)
    fixed_expense3 = db.Column(db.Float)
    fixed_expense4 = db.Column(db.Float)
    variable_expenses = db.Column(db.Float)
    cash_flow_projection = db.Column(db.Float)
    overdraft_limit = db.Column(db.Float)

    def __repr__(self):
        return f'<BusinessDetails {self.business_name}>'
