const getDataPortafolio = mercado => {
    fetch(`http://localhost:8282/portafolio/${mercado}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            setData(data.pais, data.activos)
        })
        .then(() => {
            mostrarPortafolio()
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
        });
}

const setData = (pais, activos) => {
    let id = `portafolio.${pais}`
    for (const activo of activos) {
        document.getElementById(`${id}.cantidad`).innerText = activo.cantidad
        document.getElementById(`${id}.titulo`).innerText = activo.titulo.descripcion
        document.getElementById(`${id}.comprometido`).innerText = activo.comprometido
        document.getElementById(`${id}.gananciaDinero`).innerText = activo.gananciaDinero
        document.getElementById(`${id}.gananciaPorcentaje`).innerText = activo.gananciaPorcentaje
        document.getElementById(`${id}.ppc`).innerText = activo.ppc
        document.getElementById(`${id}.puntosVariacion`).innerText = activo.puntosVariacion
        document.getElementById(`${id}.ultimoPrecio`).innerText = activo.ultimoPrecio
        document.getElementById(`${id}.valorizado`).innerText = activo.valorizado
        document.getElementById(`${id}.variacionDiaria`).innerText = activo.variacionDiaria
    }
}

const mostrarPortafolio = () => {
    document.getElementsByClassName('loader')[1].hidden = true
    document.querySelector('#portafolio').hidden = false
}