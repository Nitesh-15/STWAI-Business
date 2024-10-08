from flask import render_template, redirect, url_for, flash
from app import app, db
from app.forms import BusinessDetailsForm,LoginForm,RegisterForm
from app.models import BusinessDetails

# Root route that redirects to /business-details
@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/business-details', methods=['GET', 'POST'])
def business_details():
    form = BusinessDetailsForm()
    if form.validate_on_submit():
        # Creating a new BusinessDetails instance
        business = BusinessDetails(
            business_name=form.business_name.data,
            business_type=form.business_type.data,
            industry=form.industry.data,
            mission_statement=form.mission_statement.data,
            vision_statement=form.vision_statement.data,
            founded=form.founded.data,
            founders=form.founders.data,
            location=form.location.data,
            number_of_employees=form.number_of_employees.data,
            business_stage=form.business_stage.data,
            business_model=form.business_model.data,
            turnover_year1=form.turnover_year1.data,
            turnover_year2=form.turnover_year2.data,
            turnover_year3=form.turnover_year3.data,
            turnover_year4=form.turnover_year4.data,
            gross_profit=form.gross_profit.data,
            net_profit=form.net_profit.data,
            monthly_inflow=form.monthly_inflow.data,
            monthly_outflow=form.monthly_outflow.data,
            monthly_cashflow=form.monthly_cashflow.data,
            fixed_expense1=form.fixed_expense1.data,
            fixed_expense2=form.fixed_expense2.data,
            fixed_expense3=form.fixed_expense3.data,
            fixed_expense4=form.fixed_expense4.data,
            variable_expenses=form.variable_expenses.data,
            cash_flow_projection=form.cash_flow_projection.data,
            overdraft_limit=form.overdraft_limit.data
        )
        # Adding and committing the new record to the database
        db.session.add(business)
        db.session.commit()
        # Flashing a success message
        flash('Business details have been saved successfully.', 'success')
        return redirect(url_for('business_details'))
    
    # Rendering the template with the form
    return render_template('business_details.html', form=form)

@app.route('/view-business-details')
def view_business_details():
    business_details = BusinessDetails.query.all()  # Fetch all records from the database
    return render_template('view_business_details.html', business_details=business_details)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()  # Use the LoginForm
    if form.validate_on_submit():  # Handle form submission
        username = form.username.data
        password = form.password.data
        
        # For now, we'll use a simple check for demonstration
        if username == 'admin' and password == 'password':  # Replace with your authentication logic
            flash('Login successful!', 'success')
            return redirect(url_for('business_details'))
        else:
            flash('Login failed. Please check your username and password.', 'danger')
    
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        
        # For now, you can create a new user instance and save it to the database
        #new_user = User(username=username, email=email)
        #new_user.set_password(password)  # Assuming you have a method to hash passwords
        
        # Add the new user to the database
        #db.session.add(new_user)
        #db.session.commit()
        
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)