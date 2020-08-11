const getSerieHistorica = () => {
    fetch(`http://localhost:8282/seriehistorica`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            setSerieHistorica(data.response)
        })
        .then(() => {
            mostrarHistorico()
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
        });
}

const setSerieHistorica = (data) => {
    for (let i = 0; i < 100; i++) {
        document.getElementById(`historico-body`).innerHTML += createRowSerieHistorica(data[i])
    }
    /*     for (const item of data) {
            document.getElementById(`historico-body`).innerHTML += createRowSerieHistorica(item)
        } */
}

const mostrarHistorico = () => {
    document.getElementsByClassName('loader')[3].hidden = true
    document.querySelector('#historico').hidden = false
}

const createRowSerieHistorica = item => {
    return `
    <tr>
        <th>${item.apertura}</th>
        <th>${item.cantidadOperaciones}</th>
        <th>${item.cierreAnterior}</th>
        <th>${item.fechaHora}</th>
        <th>${item.interesesAbiertos}</th>
        <th>${item.maximo}</th>
        <th>${item.minimo}</th>
        <th>${item.moneda}</th>
        <th>${item.montoOperado}</th>
        <th>${item.precioAjuste}</th>
        <th>${item.precioPromedio}</th>
        <th>${item.puntas}</th>
        <th>${item.tendencia}</th>
        <th>${item.ultimoPrecio}</th>
        <th>${item.variacion}</th>
        <th>${item.volumenNominal}</th>
    </tr>`
}