function filtrar_comunas() {
    const cod_seleccionado = $(this).val()
    $("#comuna_cod").val("")
    $("#comuna_cod option").each(function() {
        const comuna = $(this)
        const cod_comuna = comuna.val()
    if (cod_seleccionado == cod_comuna.substring(0, 2)) {
        comuna.show()
    } else {
        comuna.hide()
    }
    })
}
$('#region_cod').on('change', filtrar_comunas)

