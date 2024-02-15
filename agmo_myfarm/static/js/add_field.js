window.onload = function() {
    initMap({lat: 36.2808, lng: 127.1426});
};
        
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
        
let markers = [];
var startPoint; // 클릭한 시작점의 좌표를 저장할 변수
var endPoint;
let label_num;
let line;

function submitForm() {
    var form = document.getElementById('addFieldForm');
    if (form) {
        alert("경작지가 성공적으로 추가되었습니다!")
        form.submit();
    };
}

function initMap(location) {
        //맵 보여주는 함수
    var mapOptions = {
        center: location,
        zoom: 20,
        mapTypeControl: false,
        mapTypeId: google.maps.MapTypeId.HYBRID,
    };
    map = new google.maps.Map(document.getElementById('map'), mapOptions);
    // 사용자가 지도를 클릭할 때마다 마커 추가


// 여기가 ------------------------------------------------------------------------------
    document.getElementById('addMarker').addEventListener('click', function() {
        // 기존의 이벤트 리스너를 모두 제거합니다.
        google.maps.event.clearListeners(map, 'click');
        // 지도 클릭 이벤트를 등록하여 클릭한 위치를  저장
        map.addListener('click', function(event) {
            label_num = (markers.length + 1).toString();
            addMarker(map, event.latLng, label_num);
            endLatLng = event.latLng; // 클릭한 위치의 좌표를 endLatLng에 저장
        });
    });
}
//init map 끝

// 사용자가 지도에 마커 추가
function addMarker(map, location, label) {
    
    let marker = new google.maps.Marker({
        position: location,
        map: map,
        label: label,
        draggable: true // 마커를 드래그할 수 있도록 설정
    });

    if (markers.length > 0) {
        let previousMarker = markers[markers.length - 1];
        let line = new google.maps.Polyline({
            path: [previousMarker.position, marker.position],
            geodesic: true,
            strokeColor: '#FF0000',
            strokeOpacity: 1.0,
            strokeWeight: 2
        });
        line.setMap(map); // setMap 메소드로 지도에 선을 추가합니다.
    }
    

    // 사용자가 마커를 클릭했을 때 마커를 이동할 수 있도록 설정
    marker.addListener("click", function() {
        this.setDraggable(true);
    });

    // 사용자가 마커를 드래그하여 이동했을 때 마커 위치 업데이트
    marker.addListener("dragend", function(event) {
        updateMarker(this, event.latLng);
    });
    markers.push(marker);
    console.log(markers);


}

// 마커 위치 업데이트
function updateMarker(marker, location) {
    marker.setPosition(location);
}

// 마커들을 서버에 저장
document.getElementById("subMarker").addEventListener("click", function() {
    saveMarkers();
    google.maps.event.clearListeners(map, 'click');
});


function saveMarkers() {
    let markerCoordinates = [];
    var fieldNameInput = document.getElementById('field_name_input');
    var fieldName = fieldNameInput.value.trim()
    markers.forEach(function(marker) {
        markerCoordinates.push(marker.getPosition().toJSON());
    });

    // 서버로 마커 좌표를 전송
$.ajax({
    url: 'save_markers/',
    type: 'POST',
    headers: {
        'X-CSRFToken': getCookie('csrftoken')
    },
    contentType: 'application/json',
    data: JSON.stringify({ "markers": markerCoordinates }),
    success: function(data) {
        var session_data = data.data;
        
        if (fieldName === ''){
            
            var warningElements = document.querySelectorAll('.text-danger');
            warningElements.forEach(function(element) {
            element.innerText = '';
            document.getElementById('field_name_warning').innerText = '경작지 이름을 입력하세요!';
        })
    }
        else if (session_data == null || session_data[1] === 0 || session_data[3] === 0) {
            var warningElements = document.querySelectorAll('.text-danger');
            warningElements.forEach(function(element) {
            element.innerText = '';
            document.getElementById('location_warning').innerText = '경작지의 경계를 설정해주세요!';
            })
        }
    
        else {
            submitForm();
            }
            
        }
    ,
    error: function(xhr, status, error) {
        console.error('Error:', error);
    }
    });
}
// 맵을 초기화하는 함수를 호출합니다.

// 마커를 초기화
document.getElementById("reset_marker").addEventListener("click", function() {
    if (line) {
        line.setMap(null);
        line = null; // 폴리라인 객체 초기화
    }
    markers.forEach(function(marker) {
        marker.setMap(null);  // 각 마커를 지도에서 제거
    });
    
    
    markers = [];  // 배열 비우기

    alert('마커가 초기화되었습니다! ');
});