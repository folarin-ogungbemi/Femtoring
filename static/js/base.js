document.addEventListener("DOMContentLoaded", function() {
    const caretDown = document.querySelector('.fa-caret-down');
    const openTrashModal = document.querySelector('.open-trash-modal');
    const closeMessage = document.querySelector('.close-message');
    const deleteMessageModal = document.querySelector('.modal');
    const userMessage = document.querySelector('.user-message');
    const messageAlert = document.getElementById('message-alert-container')

    const OpenMessageToggler = () =>{
        userMessage.classList.toggle('is-active');
    }
    const ModalFunc= () =>{
        deleteMessageModal.classList.add('is-active');
    }

    if (messageAlert != undefined) {
        setTimeout(function(){ 
            messageAlert.classList.add('visually-hidden')
         }, 4000);
    }

    caretDown.addEventListener('click', () => OpenMessageToggler());
    openTrashModal.addEventListener('click', () => ModalFunc());
    closeMessage.addEventListener('click', () => {
        deleteMessageModal.classList.remove('is-active');
        userMessage.classList.remove('is-active');
    });

});