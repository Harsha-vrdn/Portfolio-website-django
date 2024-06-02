document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.querySelector('.menu-toggle');
    const navbarNav = document.querySelector('.navbar-nav');

    menuToggle.addEventListener('click', function() {
        navbarNav.classList.toggle('active');
    });
});

// Get the modal
var modal = document.getElementById("contactModal");

// Get the button that opens the modal
var btn = document.querySelector(".btn-container .btn.btn-color-1:nth-child(2)");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
btn.onclick = function() {
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
