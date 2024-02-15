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


document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const searchButton = document.getElementById('searchButton');
    const searchResults = document.getElementById('searchResults');

    searchButton.addEventListener('click', function() {
        const csrftoken = getCookie('csrftoken');
        const searchTerm = searchInput.value.trim();

        // AJAX 요청
        fetch('farm/autocomplete/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrftoken,  // Django CSRF 토큰을 사용할 경우
            },
            body: new URLSearchParams({
                'search_term': searchTerm,
            }),
        })
        .then(response => response.json())
        .then(data => {
            // 결과를 처리하여 셀렉트 박스에 옵션 추가
            updateResults(data.results);
            searchButton.setAttribute('aria-expanded', true);
        });
    });

    function updateResults(results) {
        // 드롭다운 메뉴 초기화 후 결과 추가
        const parsedResults = JSON.parse(results);
        searchResults.innerHTML = '';
        parsedResults.forEach(result => {

            const li = document.createElement('li');
            const a = document.createElement('a');
            a.classList.add('dropdown-item');
            a.href = '#';
            a.textContent = result.fields.field_name;
            // 각 아이템을 클릭했을 때의 동작을 추가
            
            a.addEventListener('click', function() {
                // 클릭한 아이템에 대한 동작 수행
                handleItemClick(result.fields);
            });
            li.appendChild(a);
            searchResults.appendChild(li);
        });
    }

    function handleItemClick(result) {
        // 클릭한 아이템에 대한 동작 구현
        console.log('Clicked item:', result.field_name);
        const url = "farm/"+ "search_change/"
        const csrftoken = getCookie('csrftoken');

        const jsonData = JSON.stringify({ "result": result.field_name });
        fetch(url,{
            method: 'POST',
            headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
            },
            body: jsonData,
        })
        .then(response => response.json())
        .then(data => {
            // 응답 데이터를 이용하여 추가 동작 수행
            window.location.reload();
        })
        .catch(error => {
            console.error('Fetch Error:', error);
        });
                
                
        // 여기에 클릭한 아이템에 대한 추가 동작을 구현할 수 있습니다.
    }
});

