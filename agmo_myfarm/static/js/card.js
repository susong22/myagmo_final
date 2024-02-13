const handleDelClick = (buttonId) => {
    const butId = buttonId.split("-").pop();
    const csrftoken = getCookie('csrftoken');
    const url =  butId + "/delete";
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


