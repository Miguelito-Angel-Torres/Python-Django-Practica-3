// function significa que la funcion se ejecuta cuando ya estas adentro del html
(function(){
    // en esta variable : tengo la identificacion
    const btnEliminacion = document.querySelectorAll(".btnEliminacion");
     
    // recorrido de cada elemento(botton)
    btnEliminacion.forEach(btn=>{
        btn.addEventListener('click',(e) =>{
            const confirmacion = confirm('¿Estas seguro?')
            // Con este metodo le digo que mi evento no haga nada
            if(!confirmacion){
                e.preventDefault();
            }
        });
    });

})();

