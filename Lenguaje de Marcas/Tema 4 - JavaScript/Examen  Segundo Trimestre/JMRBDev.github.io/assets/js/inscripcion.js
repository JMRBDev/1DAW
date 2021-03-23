var nombres = [];

/* Validar inputs de formulario */
function validarForm() {
    var nombre = document.getElementById("input_nombre").value;
    var dni = document.getElementById("input_dni").value;
    var email = document.getElementById("input_email").value;
    var resultado = document.getElementById("resultado_aqui");
    resultado.innerText = "";

    var nombre_invalido = "";
    var dni_invalido = "";
    var email_invalido = "";
    var hayError = false;

    /* Validar nombre */
    if (/^[A-Za-z]+$/.test(nombre) != true || nombre.length < 3) { /* Validar nombre */
        hayError = true;
        nombre_invalido = "El nombre es inválido.";
        resultado.innerHTML = resultado.innerText + "</br></br>" + nombre_invalido + "</br></br>";
    }

    /* Validar DNI */
    var numero;
    var letraDNI;
    var letra;
   
    if(/^\d{8}[a-zA-Z]$/.test (dni) == true){
        numero = dni.substr(0, dni.length-1);
        letraDNI = dni.substr(dni.length-1, 1);
        numero = numero % 23;
        letra = 'TRWAGMYFPDXBNJZSQVHLCKET'.substring(numero, numero+1);
        if (letra != letraDNI.toUpperCase()) {
            hayError = true;
            dni_invalido = "El DNI es inválido.";
            resultado.innerHTML = resultado.innerText + "</br></br>" + dni_invalido + "</br></br>";
        }
    }else{
        hayError = true;
        dni_invalido = "El DNI es inválido.";
        resultado.innerHTML = resultado.innerText + "</br></br>" + dni_invalido + "</br></br>";
    }

    /* Validar email */
    if (/^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/.test(email) != true) { /* Validar email */
        hayError = true;
        email_invalido = "El email es inválido.";
        resultado.innerHTML = resultado.innerText + "</br></br>" + email_invalido + "</br></br>";
    }

    if (!hayError) { /* Aviso de que todo ha salido correctamente */
        resultado.innerHTML = "Todos los datos se han introducido correctamente.";
        var nuevos_datos = [nombre, dni, email];
        nombres.push(nombre);
        añadirFila(nuevos_datos);
    }
}

function añadirFila(datos) {
    let tabla_usuarios = document.getElementById("tabla_usuarios");
  
    // Insertar fila al final de la tabla
    let nuevaFila = tabla_usuarios.insertRow(-1);
  
    // Insertar celda en la fila
    let celdaNombre = nuevaFila.insertCell(0);
  
    // Añadir texto a la celda
    let nuevoNombre = document.createTextNode(datos[0]);
    celdaNombre.appendChild(nuevoNombre);

  
    // Insertar celda en la fila
    let celdaDNI = nuevaFila.insertCell(1);
  
    // Añadir texto a la celda
    let nuevoDNI = document.createTextNode(datos[1]);
    celdaDNI.appendChild(nuevoDNI);


    // Insertar celda en la fila
    let celdaEmail = nuevaFila.insertCell(2);
  
    // Añadir texto a la celda
    let nuevoEmail = document.createTextNode(datos[2]);
    celdaEmail.appendChild(nuevoEmail);
}

function mostrarEnNuevaVentana() {
    var myWindow = window.open("", "", "width=400,height=300");
    myWindow.document.write('<table id="tabla_usuarios"><th>Nombre</th><th>DNI</th><th>Email</th><tr><td>Jose</td><td>77394298B</td><td>josemrb99@gmail.com</td></tr></table>');
}

function buscarNombre() { /* No terminado */
    debugger
    var busqueda = document.getElementById("input_buscar").value;
    var encontrado = false;
    for (var i = 0; i < nombres.length; i++) {
        if (busqueda == nombres[i]) {
            encontrado = true;
            break;
        }else{
            encontrado = false;
        }
    }

    if (encontrado == true) {
        alert(nombre, dni, email);
    }else{
        alert("No se ha encontrado el usuario.")
    }
}