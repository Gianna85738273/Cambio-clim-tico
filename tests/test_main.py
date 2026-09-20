from main import app

app.config["TESTING"] = True
cliente = app.test_client()

def test_pagina_principal():
    respuesta = cliente.get("/")
    contenido = respuesta.get_data(as_text=True)

    assert respuesta.status_code == 200
    assert "EcoHuella" in contenido

def test_impacto_bajo():
    respuesta = cliente.post(
        "/",
        data={
            "transporte": "0",
            "energia": "0",
            "residuos": "0",
        },
    )

    contenido = respuesta.get_data(as_text=True)
    assert respuesta.status_code == 200
    assert "Tu impacto es bajo" in contenido
    assert "Ya alcanzaste el puntaje mínimo" in contenido

def test_impacto_medio():
    respuesta = cliente.post(
        "/",
        data={
            "transporte": "1",
            "energia": "1",
            "residuos": "1",
        },
    )

    contenido = respuesta.get_data(as_text=True)
    assert respuesta.status_code == 200
    assert "Tu impacto es medio" in contenido
    assert "En los trayectos cortos" in contenido

def test_impacto_alto():
    respuesta = cliente.post(
        "/",
        data={
            "transporte": "2",
            "energia": "2",
            "residuos": "2",
        },
    )

    contenido = respuesta.get_data(as_text=True)
    assert respuesta.status_code == 200
    assert "Tu impacto es alto" in contenido
    assert "Reemplazá algunos viajes en auto" in contenido