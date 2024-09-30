document.getElementById('nuevo-proceso-form').addEventListener('submit', function(event) {
    event.preventDefault(); 
    const id = document.getElementById('id').value;
    const nombre = document.getElementById('nombre').value;
    const tamano = document.getElementById('tamano').value;
    const idRecurso = document.getElementById('id-recurso').value;

    alert(`Proceso agregado:\nID: ${id}\nNombre: ${nombre}\nTamaño: ${tamano} KB\nID de Recurso: ${idRecurso}`);
    this.reset();
});

var acc = document.getElementsByClassName("accordion");
for (let i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var panel = this.nextElementSibling;

        if (panel.style.display === "block") {
            panel.style.display = "none";
        } else {
            panel.style.display = "block";
        }
    });
}
