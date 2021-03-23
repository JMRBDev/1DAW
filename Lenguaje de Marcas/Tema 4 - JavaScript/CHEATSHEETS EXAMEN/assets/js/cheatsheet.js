// Botón de scroll hacia arriba
mybutton = document.getElementById("scrollUp_btn");

function topFunction() {
    document.body.scrollTop = 0; // Safari
    document.documentElement.scrollTop = 0; // Chrome, Firefox, IE y Opera
}





/* Validación DNI */
function validarDNI(dni) {
    var numero
    var letraDNI
    var letra
   
    if(/^\d{8}[a-zA-Z]$/.test (dni) == true){
        numero = dni.substr(0, dni.length-1);
        letraDNI = dni.substr(dni.length-1, 1);
        numero = numero % 23;
        letra = 'TRWAGMYFPDXBNJZSQVHLCKET'.substring(numero, numero+1);
        if (letra != letraDNI.toUpperCase()) {
        alert('Dni erroneo, la letra del NIF no se corresponde');
        }else{
            alert('Dni correcto');
        }
    }else{
       alert('Dni erroneo, formato no válido');
    }
}

/* Validación email */
function validarEmail(email) {
    if (/^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/.test(email)) {
        alert("La dirección de email " + email + " es correcta.");
    }else{
        alert("La dirección de email es incorrecta.");
    }
}

/* Validacion telefono +34 900 900900 */
function validarTlf(numeroTlf) {
    if (/^\+\d{2,3}\s\d{9}$/.test(numeroTlf)) {
        alert("El número de teléfono " + numeroTlf + " es correcto.");
    }else{
        alert("El número de teléfono es incorrecto.");
    }
}

/* Validacion telefono (900) 900900 */
function validarTlf(numeroTlf) {
    if (/^\(\d{3}\)\s\d{6}$/.test(numeroTlf)) {
        alert("El número de teléfono " + numeroTlf + " es correcto.");
    }else{
        alert("El número de teléfono es incorrecto.");
    }
}

/* Validar que checkbox está seleccionado */
function validarCheckBox() {
    elemento = document.getElementById("campo");

    if( !elemento.checked ) {
        return false;
    }
}

function validarCheckBoxBucle() {
    formulario = document.getElementById("formulario");

    for(var i=0; i<formulario.elements.length; i++) {
        var elemento = formulario.elements[i];
        if(elemento.type == "checkbox") {
            if(!elemento.checked) {
                return false;
            }
        }
    }
}

/* Validar que radio btn está seleccionado */
function validarRadioBtn() {
    opciones = document.getElementsByName("opciones");

    var seleccionado = false;
    for(var i=0; i<opciones.length; i++) {
        if(opciones[i].checked) {
            seleccionado = true;
            break;
        }
    }

    if(!seleccionado) {
        return false;
    }
}


/* ------------------------ */
/* Trabajar con formularios */
/* ------------------------ */

/* Escribir nombre y apellido desde formulario */
function nombreApellidos() {
    var nombre = document.getElementById("input_nombre").value;
    var apellido = document.getElementById("input_apellido").value;
    var email = document.getElementById("input_email").value;
    var generoHombre = document.getElementById("radio_genero_hombre").value;
    var generoMujer = document.getElementById("radio_genero_mujer").value;
    var terminos = document.getElementById("checkbox_terminos").value;

    document.getElementById("resultado_aqui").innerHTML = "Nombre: " + nombre + " " + apellido;
}

/* Validar inputs de formulario */
function validarForm() {
    debugger
    var nombre1 = document.getElementById("input_nombre1").value;
    var apellido1 = document.getElementById("input_apellido1").value;
    var email1 = document.getElementById("input_email1").value;
    var generoHombre1 = document.getElementById("radio_genero_hombre1");
    var generoMujer1 = document.getElementById("radio_genero_mujer1");
    var terminos1 = document.getElementById("checkbox_terminos1");
    var resultado1 = document.getElementById("resultado_aqui1");

    var nombre_invalido1 = "";
    var apellido_invalido1 = "";
    var email_invalido1 = "";
    var genero_invalido1 = "";
    var terminos_invalido1 = "";
    var hayError = false;

    if (/^[A-Za-z]+$/.test(nombre1) != true || nombre1.length < 3) { /* Validar nombre */
        hayError = true;
        nombre_invalido1 = "El nombre es inválido.";
        resultado1.innerHTML = resultado1.innerText + "</br></br>" + nombre_invalido1 + "</br></br>";
    }
    if (/^[A-Za-z]+$/.test(apellido1) != true) { /* Validar apellido */
        hayError = true;
        apellido_invalido1 = "El apellido es inválido.";
        resultado1.innerHTML = resultado1.innerText + "</br></br>" + apellido_invalido1 + "</br></br>";
    }
    if (/^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/.test(email1) != true) { /* Validar email */
        hayError = true;
        email_invalido1 = "El email es inválido.";
        resultado1.innerHTML = resultado1.innerText + "</br></br>" + email_invalido1 + "</br></br>";
    }
    if (generoHombre1.checked == true) { /* Validar géneros, solo se puede marcar uno */
        generoHombre1.value = 1;
        generoMujer1.value = 0;
    } else {
        generoHombre1.value = 0;
        generoMujer1.value = 1;
    }
    if (generoHombre1.checked == false && generoMujer1.checked == false) { /* Validar géneros, hay que seleccionar uno forzosamente */
        hayError = true;
        genero_invalido1 = "No se ha seleccionado ningún género.";
        resultado1.innerHTML = resultado1.innerText + "</br></br>" + genero_invalido1 + "</br></br>";
    }
    if (terminos1.checked == false) {
        hayError = true;
        terminos_invalido1 = "Para continuar debe aceptar los términos y condiciones de uso.";
        resultado1.innerHTML = resultado1.innerText + "</br></br>" + terminos_invalido1 + "</br></br>";
    }

    if (!hayError) { /* Aviso de que todo ha salido correctamente */
        alert("Todos los datos se han introducido correctamente");
    }
}