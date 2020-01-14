function getData()
{
    var nombre=document.getElementById("nombre").value;
    var edad=document.getElementById("edad").value;
    alert("Tu nombre es : "+nombre+ " y tienes " +edad+ " años");  
}
function saludo()
{
alert("Buenos días");
}
function sumar (){
    //declaro las variables
    var resultado;
    var operando1;
    var operando2;
// realizo las operaciones
operando1= parseInt(document.getElementById ("operando1").value);
operando2= parsenInt(document.getElementById ("operando2").value);
resultado=operando1+operando2;
document.getElementById("resultado").value=resultado;
}
