// on s'assure que la page est chargée
window.onload = function(){
     let macarte= L.map("carte").setView([48.852969, 2.349993].13)
     L.tileLayer("https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png{
        attribution: "données OpenStreetMap France",
        minZoom: 1,
        maxZoom: 20
        }).addTo(macarte)
     }
}