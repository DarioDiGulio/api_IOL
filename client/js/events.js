
if (isLogin) {
    document.getElementById('button-submit').addEventListener('click', () => {
        let user = document.querySelector('#user').value
        let password = document.querySelector('#password').value
        login(user, password)
    })
} else if (isDashboard) {

    document.getElementById('button-miCuenta').addEventListener('click', () => {
        document.querySelector('#miCuenta-block').hidden = false
        getData()
    })

    document.getElementById('button-portafolio').addEventListener('click', () => {
        document.querySelector('#portafolio-block').hidden = false
        getDataPortafolio('argentina')
        getDataPortafolio('estados_Unidos')
    })
}


