$(document).ready(function () {
    $("#btnenviar").click(function(e){
        if(valida_formulario()!=""){
            swal("Error de Formulario", valida_formulario(), "error");
        }else{
            swal("Compra Realizada", "Nos pondremos en contacto contigo", "success");
        }
        e.preventDefault();

        document.getElementById('formulario').reset();
    })
});


function valida_formulario(){
    var html="";
    var nombre= $("#txtnombre").val();
    var apellidopaterno= $("#txtapellidopaterno").val();
    var apellidomaterno= $("#txtapellidomaterno").val();
    var direccion= $("#txtdireccion").val();
    var rut =$("#txtrut").val();
    var comuna= $("#cbxciudad").val();
    var comentario = $("#txtcomentario").val();
    var telefono = $("#txttelefono").val();

    if(nombre==""){
        html+="- Debe ingresar un Nombre \n";
    }
    if(apellidopaterno==""){
        html+="- Debe ingresar un Apellido Paterno \n";
    }
    if(apellidomaterno==""){
        html+="- Debe ingresar un Apellido Materno \n";
    }
    if(direccion==""){
        html+="- Debe ingresar una Direccion \n";
    }
    if(rut==""){
        html+="- Debe ingresar un rut \n"
    }
    else if(validarRut(rut) == false){
        html+="- Rut ingresado no valido \n";
    }
    if(telefono ==""){
        html+="- Debe ingresar un numero de telefono \n"
    }
    else if(telefono.length < 8 || telefono.length > 11){
        html+="- Telefono ingresado no valido\n"
    }
    if(comuna == 0){
        html += "- Debe seleccionar una comuna \n";
    }
    if(comentario.length > 50){
        html += "- El comentario no puede tener mas de 50 caracteres";
    }
    
    return html;
 }

function validarRut(rutCompleto) {
    rutCompleto = rutCompleto.replace("‐", "-");

    if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test(rutCompleto))
        return false;
   
    var tmp = rutCompleto.split('-');
    var digv = tmp[1];
    var rut = tmp[0];
    if (digv == 'K') digv = 'k';
    return (dv(rut) == digv);
}


function dv(T) {
    var M = 0,
        S = 1;
    for (; T; T = Math.floor(T / 10))
        S = (S + T % 10 * (9 - M++ % 6)) % 11;
    return S ? S - 1 : 'k';
}
