// Traer las provincias
var labelsProv = [];
var dataProv = [];

$.ajax({
    type: "GET",
    contentType: "application/json; charset=utf-8",
    url: "http://localhost:8000/WebService",
    dataType: "json",
    success: function (data) {
        data.forEach((element) => {
            labelsProv.push(element.nombre);
            dataProv.push(element.poblacion_total);
        });
        dibujarChartProvincias();
    },
    error: function (data) {
        alert("Ocurrió un error al intentar traer las provincias");
    },
});

// Traer los cantones
var selecProvincias = document.getElementById("todas-provincias");
var labelsCant = [];
var dataCant = [];

selecProvincias.addEventListener("change", (event) => {
    var provincia = event.target.value;
    labelsCant = [];
    dataCant = [];
    $.ajax({
        type: "GET",
        contentType: "application/json; charset=utf-8",
        url: "http://localhost:8000/WebService?nom-provincia=" + provincia,
        dataType: "json",
        success: function (data) {
            var listaCatones = document.getElementById("lista-cantones");
            listaCatones.innerHTML = "";
            data.forEach((element) => {
                labelsCant.push(element.nombre);
                dataCant.push(element.poblacion_total);

                listaCatones.innerHTML +=
                    '<p class="canton margin-0">' + element.nombre + "</p>";
            });
            mostrarDatosProvincia(provincia);
            dibujarchartCantones();
        },
        error: function (data) {
            alert("Ocurrió un error al intentar traer los cantones");
        },
    });
});

// ******* CHART **********
function dibujarChartProvincias() {
    var contextoProv = document
        .getElementById("chart-provincias")
        .getContext("2d");
    var chartProvincias = new Chart(contextoProv, {
        type: "bar",
        data: {
            labels: labelsProv,
            datasets: [
                {
                    label: "Censo 2010",
                    data: dataProv,
                },
            ],
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                },
            },
        },
    });
}

function dibujarchartCantones() {
    $("#chart-cantones").remove();
    document.getElementById("addc").innerHTML =
        '<canvas id="chart-cantones"></canvas>';
    var contextoCant = document
        .getElementById("chart-cantones")
        .getContext("2d");

    chartCantones = new Chart(contextoCant, {
        type: "line",
        data: {
            labels: labelsCant,
            datasets: [
                {
                    label: "Censo 2010",
                    data: dataCant,
                },
            ],
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                },
            },
        },
    });
}

function mostrarDatosProvincia(event) {
    var nombreprovincia = document.getElementById("nombre-provincia");
    var capital = document.getElementById("capital");
    var poblaciontotal = document.getElementById("poblacion-total");
    var superficie = document.getElementById("superficie");
    var totalhombres = document.getElementById("total-hombres");
    var totalmujeres = document.getElementById("total-mujeres");

    $.ajax({
        type: "GET",
        contentType: "application/json; charset=utf-8",
        url: "http://localhost:8000/WebService?provincia=" + event,
        dataType: "json",
        success: function (data) {
            nombreprovincia.innerHTML =
                "<strong>" + data[0].nombre + "</strong>";
            capital.innerHTML = "<strong>" + data[0].capital + "</strong>";
            poblaciontotal.innerHTML =
                "<strong>" + data[0].poblacion_total + "</strong>";
            superficie.innerHTML =
                "<strong>" + data[0].superficie + "</strong>";
            totalhombres.innerHTML = "<strong>" + data[0].hombres + "</strong>";
            totalmujeres.innerHTML = "<strong>" + data[0].mujeres + "</strong>";
        },
        error: function (data) {
            alert("Ocurrió un error al intentar traer los cantones");
        },
    });
}
