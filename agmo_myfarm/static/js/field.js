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
            
            
        } else {
            ;
        }
    })

}

document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const searchResults = document.getElementById('searchResults');

    searchInput.addEventListener('input', function() {
        const searchTerm = searchInput.value.trim();
        const csrftoken = getCookie('csrftoken');
        const butId = buttonId.split("-").pop();
        const url =  "farm/" + butId + "/select";
        // AJAX 요청
        fetch(url, {
            method: "POST",
            mode: "same-origin",
            headers: {
                'X-CSRFToken': csrftoken,
            },
        })
        .then(response => response.json())
        .then(data => {
            // 결과를 처리하여 셀렉트 박스에 옵션 추가
            updateResults(data.results);
        });
    });

    function updateResults(results) {
        // 셀렉트 박스 초기화 후 옵션 추가
        searchResults.innerHTML = '';
        results.forEach(result => {
            const option = document.createElement('option');
            option.textContent = result;
            searchResults.appendChild(option);
        });
    }
});