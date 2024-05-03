function getCookie(name){

    const value = `; ${document.cookie}` ;

    const parts = value.split(`; ${name}=`);

    if(parts.length == 2) return parts.pop().split(';').shift();
    
}

function submit(id) {

    const textareaValue = document.getElementById(`textarea${id}`).value;

    const content = document.getElementById(`content${id}`);

    console.log(content);

    const modal = document.getElementById(`exampleModal${id}`);

    fetch(`/edit/${id}`, {
        method: "POST",
        headers: {"Content-type": "application/json", "X-CSRFToken": getCookie("csrftoken")},
        body: JSON.stringify({
        'content': textareaValue

        })

    })

    .then(response => response.json())
    .then(result => {

        content.innerHTML = result.data;

        modal.classList.remove('show');
        modal.setAttribute('aria-hidden', 'true');
        modal.setAttribute('style', 'display: none');

        const modals = document.getElementsByClassName("modal-backdrop");

        for (let i = 0; i < modals; i++) {
            document.body.removeChild(modals[i]);
        }

    })

};