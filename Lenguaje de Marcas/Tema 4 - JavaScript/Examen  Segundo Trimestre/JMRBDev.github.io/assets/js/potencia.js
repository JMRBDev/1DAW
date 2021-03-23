function calcularPotencia() {
    var base = document.getElementById("input_base").value;
    var exponente = document.getElementById("input_exponente").value;
    var resultado = 1;
    var posible = false;

    if (parseFloat(base) < 0) {
        alert("La base debe ser positiva.");
        posible = false;
    } else if (base == "") {
        alert("La base es un campo requerido.");
        posible = false;
    } else if (/^\d+$/.test (base) == false) {
        alert("La base debe estar compuesta por un número.");
        posible = false;
    } else {
        posible = true;
    }
    if (parseFloat(exponente) < 0) {
        alert("El exponente debe ser positivo.");
        posible = false;
    } else if (parseFloat(exponente) == 0) {
        alert("El exponente es 0, pruebe con otro número.");
        posible = false;
    } else if (exponente == "") {
        alert("El exponente es un campo requerido.");
        posible = false;
    } else if (/^\d$/.test (exponente) == false) {
        alert("El exponente debe estar compuesto por un número.");
        posible = false;
    } else {
        posible = true
    }

    if (posible) {
        for (var i = 1; i < parseFloat(exponente) + 1; i++) {
            resultado = parseFloat(resultado) * parseFloat(base);
        }
        document.getElementById("resultado").innerHTML = "Resultado: " + resultado.toString();
    } else {
        document.getElementById("resultado").innerHTML = "No se ha podido completar la acción.";
    }
}

function borrarFormulario() {
    document.getElementById("formulario_potencia").reset();
    document.getElementById("resultado").innerHTML = "Resultado: ";
}