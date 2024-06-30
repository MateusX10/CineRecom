function mudar_tema() {
    const tema = document.getElementById('tema_do_sistema').value;
    document.body.className = tema;
    localStorage.setItem('tema', tema);
}

// Carrega o tema armazenado no carregamento da página
window.onload = function() {
    const tema_salvo = localStorage.getItem('tema') || 'light';
    document.body.className = tema_salvo;
    document.getElementById('tema_do_sistema').value = tema_salvo;
}


function confirmar_exclusao(){

    return confirm("Tem certeza que deseja excluir?");
}