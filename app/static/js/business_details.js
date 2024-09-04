$(document).ready(function () {
    // Initialize the tabs and form behavior
    initializeTabs();
    initializeFinancialYearHandler();
    populateFinancialYearDropdown();

    initializeMonthlyExpenseHandler(); // Initialize the handler for monthly expenses
    populateMonthDropdown(); // Populate the month dropdown
    
});

// Function to initialize tab navigation
function initializeTabs() {
    // Show the first tab content
    $('.tabcontent').removeClass('active');
    $('#tab1').addClass('active');

    // Handle tab navigation buttons
    $('.next-tab').click(function () {
        var nextTabId = $(this).data('next');
        switchTab(nextTabId);
    });

    $('.prev-tab').click(function () {
        var prevTabId = $(this).data('prev');
        switchTab(prevTabId);
    });

    // Handle tab link clicks
    $('.tablinks').click(function () {
        var tabId = $(this).data('tab');
        if (!$(this).attr('disabled')) {
            switchTab(tabId);
        }
    });
}

// Function to switch between tabs
function switchTab(tabId) {
    $('.tabcontent').removeClass('active');
    $('.tablinks').removeClass('active');
    $('#' + tabId).addClass('active');
    $('[data-tab="' + tabId + '"]').addClass('active');
}

// Function to initialize financial year handling (add/remove entries)
function initializeFinancialYearHandler() {
    // Handle adding financial year entries
    $('#add_financial_year').click(function () {
        addFinancialYearEntry();
    });

    // Handle removing financial year entries
    $(document).on('click', '.remove_financial_year', function () {
        removeFinancialYearEntry($(this));
    });
}

// Function to add a financial year entry
function addFinancialYearEntry() {
    var year = $('#financial_year').val();
    var turnover = $('#turnover_input').val();

    if (year && turnover) {
        var newEntry = `
            <div class="financial-year-entry">
                <div class="form-row">
                    <div class="form-group">
                       

                        <label for="amount">Financial Year</label>
                        <input type="text" class="form-control" value="${year}" >
                    </div>
                    <div class="form-group">
                        

                        <label for="amount">Turnover</label>
                        <input type="text" class="form-control" value="${turnover}" >
                    </div>
                    <div class="form-group">
                        <button type="button" class="remove_financial_year btn-submit">-</button>
                    </div>
                </div>
            </div>
        `;
        $('#financial_year_list').append(newEntry);
        // Reset fields after adding
        resetFinancialYearFields();
    }
}

// Function to reset financial year input fields after adding
function resetFinancialYearFields() {
    $('#financial_year').val('');
    $('#turnover_input').val('');
}

// Function to remove a financial year entry
function removeFinancialYearEntry(element) {
    element.closest('.financial-year-entry').remove();
}

// Function to populate the financial year dropdown
function populateFinancialYearDropdown() {
    var currentYear = new Date().getFullYear();  // Get the current year (e.g., 2024)
    var startYear = currentYear - 5;  // Go back 5 years

    // Clear any existing options to avoid duplicates
    $('#financial_year').empty();

    // Populate the dropdown in descending order
    for (var year = currentYear; year >= startYear; year--) {
        $('#financial_year').append(new Option(year, year));
    }

    // Set the current year as the selected option by default
    $('#financial_year').val(currentYear);
}

// Function to initialize the handlers for monthly expenses
function initializeMonthlyExpenseHandler() {
    // Handle adding monthly expense entries
    $('#add_monthly_expense').click(function () {
        addMonthlyExpenseEntry();
    });

    // Handle removing monthly expense entries
    $(document).on('click', '.remove_monthly_expense', function () {
        removeMonthlyExpenseEntry($(this));
    });
}

// Function to add a monthly expense entry
function addMonthlyExpenseEntry() {
    var month = $('#month_input').val();
    var amount = $('#expense_input').val();

    if (month && amount) {
        var newEntry = `
            <div class="monthly-expense-entry">
                <div class="form-row">
                    <div class="form-group">
                         <label for="expense">Expense</label>
                         <input type="text" class="form-control" value="${month}" >
                    </div>
                    <div class="form-group">
                    <label for="amount">Amount</label>
                    <input type="text" class="form-control" value="${amount}" >
                </div>
                    <div class="form-group">
                        <button type="button" class="remove_monthly_expense btn-submit">-</button>
                    </div>
                </div>
            </div>
        `;
        $('#monthly_expense_list').append(newEntry);
        // Reset fields after adding
        resetMonthlyExpenseFields();
    }
}

// Function to reset month and expense input fields after adding
function resetMonthlyExpenseFields() {
    $('#month_input').val('');
    $('#expense_input').val('');
}

// Function to remove a monthly expense entry
function removeMonthlyExpenseEntry(element) {
    element.closest('.monthly-expense-entry').remove();
}