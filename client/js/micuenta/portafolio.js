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
    let country = pais === 'argentina' ? 'arg' : 'usa'
    for (const activo of activos) {
        document.getElementById(`porfolio-${country}-body`).innerHTML += createRowPorfolio(activo)
    }
}

const mostrarPortafolio = () => {
    document.getElementsByClassName('loader')[1].hidden = true
    document.querySelector('#portafolio').hidden = false
}

const createRowPorfolio = activo => {
    return `
    <tr>
        <td>${activo.cantidad}</td>
        <td>${activo.titulo.descripcion}</td>
        <td>${activo.comprometido}</td>
        <td>${activo.gananciaDinero}</td>
        <td>${activo.gananciaPorcentaje}</td>
        <td>${activo.ppc}</td>
        <td>${activo.puntosVariacion}</td>
        <td>${activo.ultimoPrecio}</td>
        <td>${activo.valorizado}</td>
        <td>${activo.variacionDiaria}</td>
    </tr>`
}