
    document.addEventListener("DOMContentLoaded", function() {
    // Show the first tab content
    document.querySelectorAll('.tabcontent').forEach(function(content) {
        content.classList.remove('active');
    });
    document.getElementById('tab1').classList.add('active');

    // Handle tab navigation buttons
    document.querySelectorAll('.next-tab').forEach(function(button) {
        button.addEventListener('click', function() {
            var nextTabId = this.getAttribute('data-next');
            switchTab(nextTabId);
        });
    });

    document.querySelectorAll('.prev-tab').forEach(function(button) {
        button.addEventListener('click', function() {
            var prevTabId = this.getAttribute('data-prev');
            switchTab(prevTabId);
        });
    });

    function switchTab(tabId) {
        // Hide all tab contents
        document.querySelectorAll('.tabcontent').forEach(function(content) {
            content.classList.remove('active');
        });

        // Remove active class from all tab buttons
        document.querySelectorAll('.tablinks').forEach(function(link) {
            link.classList.remove('active');
        });

        // Show the target tab content
        document.getElementById(tabId).classList.add('active');

        // Set the corresponding tab button to active
        document.querySelector('[data-tab="' + tabId + '"]').classList.add('active');

        // Remove scroll behavior to keep the page position unchanged
        // This prevents the page from scrolling up or down when switching tabs.
    }
});






















// $(document).ready(function() {
//     // Show the first section
//     $('.form-section').first().addClass('active');

//     // Handle navigation buttons
//     $('.next-section').click(function() {
//         var nextSection = $(this).data('next');
//         $(this).closest('.form-section').removeClass('active');
//         $('#' + nextSection).addClass('active');
//         $('html, body').animate({ scrollTop: $('#' + nextSection).offset().top }, 800);
//     });

//     $('.prev-section').click(function() {
//         var prevSection = $(this).data('prev');
//         $(this).closest('.form-section').removeClass('active');
//         $('#' + prevSection).addClass('active');
//         $('html, body').animate({ scrollTop: $('#' + prevSection).offset().top }, 800);
//     });
// });