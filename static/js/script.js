(function(){

    let count = 0

    btnNewTel = document.querySelector("#btnNuevoTel")
    
    for(let i = 0; i < 3; i++){

        if(document.querySelector("#id_telephone_set-"+i+"-number").value != ""){

            telSort = document.querySelector("#id_telephone_set-"+i+"-sort")
            telNumber = document.querySelector("#id_telephone_set-"+i+"-number")
            
            telSort.hidden = false
            telNumber.hidden = false

            console.log(count)
            count += 1
        }
        if (count > 2){
            console.log("btn desactivado")
            btnNewTel.setAttribute('disabled', 'true')
        }
    }

    btnNewTel.addEventListener('click',() => {
        
        console.log("primero", count)
        if (count < 3){
            telSort = document.querySelector("#id_telephone_set-"+count+"-sort")
            telNumber = document.querySelector("#id_telephone_set-"+count+"-number")
            telSort.hidden = false
            telNumber.hidden = false
        }
        if (count >= 2){
            console.log("btn desactivado")
            btnNewTel.setAttribute('disabled', 'true')
        }
        count += 1
    })
})()