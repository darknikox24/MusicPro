
let url = "https://apis.digital.gob.cl/fl/feriados"


fetch(url)
    .then(function(respuesta) {
        return respuesta.json()
    })
    .then(function(respuesta) {
       

        console.log(respuesta[0].nombre + " " + respuesta[0].fecha)

        let enlaceFeriado = document.getElementById("feriado")

        enlaceFeriado.innerText = respuesta[0].nombre + " " + respuesta[0].fecha

    })


let urlIndicadores = "https://mindicador.cl/api"

fetch(urlIndicadores)
    .then(function(respuesta){
        return respuesta.json()
    }) 
    .then(function(respuesta) {
       
        let enlaceUf = document.getElementById("uf")

        enlaceUf.innerText = "UF: " + respuesta.uf.valor
        
    })