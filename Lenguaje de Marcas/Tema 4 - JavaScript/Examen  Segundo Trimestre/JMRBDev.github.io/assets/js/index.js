// Botón de scroll hacia arriba
mybutton = document.getElementById("scrollUp_btn");

function topFunction() {
    document.body.scrollTop = 0; // Safari
    document.documentElement.scrollTop = 0; // Chrome, Firefox, IE y Opera
}