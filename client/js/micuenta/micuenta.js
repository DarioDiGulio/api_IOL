const getData = () => {
    fetch('http://localhost:8282/micuenta')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            let ars = data.cuentas[0]
            let dolar = data.cuentas[1]
            setDataArs(ars)
            setDataDolar(dolar)
            document.getElementsByClassName('loader')[0].hidden = true
            document.querySelector('#micuenta').hidden = false
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
        });
}

const setDataArs = data => {
    let id = 'ars.table'
    document.getElementById(`${id}.comprometido`).innerText = data.comprometido
    document.getElementById(`${id}.disponible`).innerText = data.disponible
    document.getElementById(`${id}.estado`).innerText = data.estado
    document.getElementById(`${id}.margen`).innerText = data.margenDescubierto
    document.getElementById(`${id}.moneda`).innerText = data.moneda
    document.getElementById(`${id}.saldo`).innerText = data.saldo
    document.getElementById(`${id}.valorizados`).innerText = data.titulosValorizados
    document.getElementById(`${id}.total`).innerText = data.total
}

const setDataDolar = data => {
    let id = 'dolar.table'
    document.getElementById(`${id}.comprometido`).innerText = data.comprometido
    document.getElementById(`${id}.disponible`).innerText = data.disponible
    document.getElementById(`${id}.estado`).innerText = data.estado
    document.getElementById(`${id}.margen`).innerText = data.margenDescubierto
    document.getElementById(`${id}.moneda`).innerText = data.moneda
    document.getElementById(`${id}.saldo`).innerText = data.saldo
    document.getElementById(`${id}.valorizados`).innerText = data.titulosValorizados
    document.getElementById(`${id}.total`).innerText = data.total
}
