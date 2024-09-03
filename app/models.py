from app import db

class BusinessDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_name = db.Column(db.String(128))
    business_type = db.Column(db.String(128))
    industry = db.Column(db.String(128))
    mission_statement = db.Column(db.Text)
    founded = db.Column(db.Integer)
    vision_statement = db.Column(db.Text)
    founders = db.Column(db.String(256), nullable=False)
    location = db.Column(db.String(128), nullable=False)
    number_of_employees = db.Column(db.Integer, nullable=False)
    business_stage = db.Column(db.String(128), nullable=False)
    business_model = db.Column(db.String(128), nullable=False)
    turnover_year1 = db.Column(db.Float, nullable=False)
    turnover_year2 = db.Column(db.Float, nullable=False)
    turnover_year3 = db.Column(db.Float, nullable=False)
    turnover_year4 = db.Column(db.Float, nullable=False)
    gross_profit = db.Column(db.Float, nullable=False)
    net_profit = db.Column(db.Float, nullable=False)
    monthly_inflow = db.Column(db.Float, nullable=False)
    monthly_outflow = db.Column(db.Float, nullable=False)
    monthly_cashflow = db.Column(db.Float, nullable=False)
    fixed_expense1 = db.Column(db.Float, nullable=False)
    fixed_expense2 = db.Column(db.Float, nullable=False)
    fixed_expense3 = db.Column(db.Float, nullable=False)
    fixed_expense4 = db.Column(db.Float, nullable=False)
    variable_expenses = db.Column(db.Float, nullable=False)
    cash_flow_projection = db.Column(db.Float, nullable=False)
    overdraft_limit = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<BusinessDetails {self.business_name}>'
