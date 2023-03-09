function camposvalidar() {
    var ele1 = document.getElementById("correo").value;
    console.log(ele1);
    var ele2 = document.getElementById("pass1").value;
    var ele3 = document.getElementById("pass2").value;

    var ele = document.getElementById("info");
    var bandera = true;
    ele.innerHTML = "";

    var expr = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    var numeros = "0123456789";
    var bnumeros = false;
    for (i = 0; i < ele2.length; i++) {
        if (numeros.indexOf(ele2.charAt(i), 0) != -1) {
            var bnumeros = true ;
        }
    }

    if (ele1.length == 0 || ele1.length == 0 || ele1.length == 0) {
        ele.innerHTML += "Debe llenar todos los campos* <br>";
        bandera = false;

    }
    if (!expr.test(ele1)) {
        ele.innerHTML += "El correo es invalido* <br>";
        bandera = false;
    }
    if (ele2 != ele3) {
        ele.innerHTML += "Las contrasenas deben ser iguales* <br>";
        bandera = false;
    }
    if (ele2.length < 6) {
        ele.innerHTML += "Las contrasena debe contener mas de 6 caracteres* <br>";
        bandera = false;
    }
    if (bnumeros == false) {
        ele.innerHTML += "Las contrasena debe contener almenos un caracter numerico* <br>";
        bandera = false;
    }
    if (bandera == true) {
        alert("Su formulario ha sido enviado con exito");
    }
}
var boton = document.getElementById("boton");
boton.addEventListener("click", camposvalidar);