function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const handleClick = (buttonId) => {
    const but = document.getElementById(buttonId);
    const allBut = document.querySelectorAll('.field-button');
    const csrftoken = getCookie('csrftoken');
    const butId = buttonId.split("-").pop();
    const url =  "farm/" + butId + "/select";
    fetch(url, {
        method: "POST",
        mode: "same-origin",
        headers: {
            'X-CSRFToken': csrftoken,
        },

    })
    .then(response => response.json())
    .then(data => {
        if (data.result == "change") {
            window.location.reload();
        } else {
            ;
        }
    })
    .catch(error => {
        console.error('Fetch Error:', error);
    });

}

