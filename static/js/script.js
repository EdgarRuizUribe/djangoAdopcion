(function(){
    btnNewTel = document.querySelector("#btnNuevoTel")

        let count = 0

        btnNewTel.addEventListener('click',() => {
            console.log("primero", count)
            if (count < 3){
                telSort = document.querySelector("#id_telephone_set-"+count+"-sort")
                telNumber = document.querySelector("#id_telephone_set-"+count+"-number")
                console.log(count)
                console.log(telNumber.value,"<------------",typeof telNumber)
                telSort.hidden = false
                telNumber.hidden = false
                if(telNumber.value == ""){
                    console.log("hola crayola")
                }
            }
            if (count === 2){
                console.log("entro 4")
                btnNewTel.setAttribute('disabled', 'true')
            }
            
            count += 1
        })
})()