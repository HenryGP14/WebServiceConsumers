const selectCountry = document.querySelector("#country");
const selectMedallas = document.querySelector("#medal");

$.ajax({
    type: "GET",
    contentType: "application/json; charset=utf-8",
    url: "http://192.168.56.1:4000/paises",
    dataType: "json",
    success: function (data) {
        data.forEach((element) => {
            option = document.createElement("option");
            option.value = element.iso3;
            option.text = element.pais;
            selectCountry.appendChild(option);
        });
    },
    error: function (data) {
        alert("Ocurrió un error al intentar obtener los países");
    },
});

$.ajax({
    type: "GET",
    contentType: "application/json; charset=utf-8",
    url: "http://192.168.56.1:4000/medallas",
    dataType: "json",
    success: function (data) {
        data.forEach((element) => {
            option = document.createElement("option");
            option.value = element.medalla;
            option.text = element.medalla;
            selectMedallas.appendChild(option);
        });
    },
    error: function (data) {
        alert("Ocurrió un error al intentar obtener las medallas");
    },
});

selectCountry.addEventListener("change", (event) => {
    document.getElementById("img_pais").src =
        "/static/img/paises/" + selectCountry.value + ".png";

    $.ajax({
        type: "GET",
        contentType: "application/json; charset=utf-8",
        url: "http://192.168.56.1:4000/triunfo-pais/" + event.target.value,
        dataType: "json",
        success: function (data) {
            $(".card").empty();
            data.forEach((element) => {
                if (element.sexo == "Femenino") {
                    img = '<img src="/static/img/people/Masculino.png" alt="">';
                } else {
                    img = '<img src="/static/img/people/Femenino.png" alt="">';
                }
                card =
                    '<div class="card-people">' +
                    '<div class="img-people">' +
                    img +
                    "</div>" +
                    '<div class="content">' +
                    "<p><strong>Nombre:</strong>" +
                    element.participante +
                    "</p>" +
                    "<p><strong>Deporte:</strong>" +
                    element.deporte +
                    "</p>" +
                    "<p><strong>Competición:</strong>" +
                    element.competicion +
                    "</p>" +
                    "</div>" +
                    "</div>";
                $(".card").prepend(card);
            });
        },
        error: function (data) {
            alert("Ocurrió un error al intentar obtener los datos");
        },
    });
});

selectMedallas.addEventListener("change", (event) => {
    document.getElementById("img_medal").src =
        "/static/img/medals/" + selectMedallas.value + ".png";
    $.ajax({
        type: "GET",
        contentType: "application/json; charset=utf-8",
        url: "http://192.168.56.1:4000/triunfo-medalla/" + event.target.value,
        dataType: "json",
        success: function (data) {
            $(".card").empty();
            data.forEach((element) => {
                img = "";
                if (element.sexo == "Femenino") {
                    img = '<img src="/static/img/people/Masculino.png" alt="">';
                } else {
                    img = '<img src="/static/img/people/Femenino.png" alt="">';
                }
                card =
                    '<div class="card-people">' +
                    '<div class="img-people">' +
                    img +
                    "</div>" +
                    '<div class="content">' +
                    "<p><strong>Nombre:</strong>" +
                    element.participante +
                    "</p>" +
                    "<p><strong>Deporte:</strong>" +
                    element.deporte +
                    "</p>" +
                    "<p><strong>Competición:</strong>" +
                    element.competicion +
                    "</p>" +
                    "</div>" +
                    "</div>";
                $(".card").prepend(card);
                //$("#img_medal").attr("src", element.ruta_foto);
            });
        },
        error: function (data) {
            alert("Ocurrió un error al intentar obtener los datos");
        },
    });
});
