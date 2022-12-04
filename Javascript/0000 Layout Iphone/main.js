airplane_button = document.getElementById("airplane")
cellData_button = document.getElementById("cell-data")
wifi_button = document.getElementById("wifi")
bluetooth_button = document.getElementById("bluetooth")
airdrop_button = document.getElementById("airdrop")
hotspot_button = document.getElementById("hotspot")

// Laranja
airplane_button.addEventListener("click", () => {
    airplane_button.classList.toggle("laranja")
    wifi_button.classList.remove("azul")
    airdrop_button.classList.remove("azul")
    cellData_button.classList.remove("verde")
    hotspot_button.classList.remove("verde")
})

// Azul
wifi_button.addEventListener("click", () => {
    wifi_button.classList.toggle("azul")
    airplane_button.classList.remove("laranja")
    hotspot_button.classList.remove("verde")
})

bluetooth_button.addEventListener("click", () => {
    bluetooth_button.classList.toggle("azul")
})

airdrop_button.addEventListener("click", () => {
    airdrop_button.classList.toggle("azul")
    
})

// Verde
cellData_button.addEventListener("click", () => {
    cellData_button.classList.toggle("verde")
    airplane_button.classList.remove("laranja")
    hotspot_button.classList.toggle("opacity")
})

hotspot_button.addEventListener("click", () => {
    if (hotspot_button.classList.opacity) {

    } else {
        hotspot_button.classList.toggle("verde")
        wifi_button.classList.remove("azul")
    }
})