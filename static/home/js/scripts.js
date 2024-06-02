document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.querySelector('.menu-toggle');
    const navbarNav = document.querySelector('.navbar-nav');

    menuToggle.addEventListener('click', function() {
        navbarNav.classList.toggle('active');
    });
});

