const getDataOperaciones = (estado, pais) => {
    fetch(`http://localhost:8282/operaciones/${estado}/${pais}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            setDataOperacines(data, pais)
        })
        .then(() => {
            mostrarOperaciones()
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
        });
}

const setDataOperacines = (data, pais) => {
    let id = `operaciones.${pais}`
    let country = pais === 'argentina' ? 'arg' : 'usa'
    for (const operacion of data) {
        document.getElementById(`operaciones-${country}-body`).innerHTML += createRowOperacion(operacion)
    }
}

const mostrarOperaciones = () => {
    document.getElementsByClassName('loader')[2].hidden = true
    document.querySelector('#operaciones').hidden = false
}

const createRowOperacion = operacion => {
    return `
    <tr>
        <td>${operacion.numero}</td>
        <td>${operacion.fechaOrden}</td>
        <td>${operacion.tipo}</td>
        <td>${operacion.estado}</td>
        <td>${operacion.mercado}</td>
        <td>${operacion.simbolo}</td>
        <td>${operacion.cantidad}</td>
        <td>${operacion.monto}</td>
        <td>${operacion.modalidad}</td>
        <td>${operacion.precio}</td>
        <td>${operacion.fechaOperada}</td>
        <td>${operacion.cantidadOperada}</td>
        <td>${operacion.precioOperado}</td>
        <td>${operacion.montoOperado}</td>
    </tr>`
}