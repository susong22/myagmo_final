window.onload = function() {
    initMap();
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

function submitForm() {
    var form = document.getElementById('addFieldForm');
    if (form) {
        alert("경작지가 성공적으로 추가되었습니다!")
        form.submit();
    };
}

function initMap() {
                    //맵 보여주는 함수
    var mapOptions = {
        center: {lat: 36.2808, lng: 127.1426},
        zoom: 20,
        mapTypeControl: false,
        mapTypeId: google.maps.MapTypeId.HYBRID,
    };
    let map = new google.maps.Map(document.getElementById('map'), mapOptions);
    //polyline 그리기 위한 좌표값, 임의의 값임

    // 사용자가 지도를 클릭할 때마다 마커 추가


    expected_path_lonlat = [
    {"lat": 36.2808, "lng": 127.1426},
    {"lat": 36.2804, "lng": 127.1431},
    {"lat": 36.2808, "lng": 127.1435},
    {"lat": 36.2811, "lng": 127.1431},
    {"lat": 36.2808, "lng": 127.1426},
    ]
                    //polyline 디자인
    const flightPath = new google.maps.Polyline({
        path: expected_path_lonlat,
        geodesic: true,
        strokeColor: "#FF0000",
        strokeOpacity: 1.0,
        strokeWeight: 2,
    });


// 여기가 ------------------------------------------------------------------------------
    document.getElementById('addMarker').addEventListener('click', function() {
        // 기존의 이벤트 리스너를 모두 제거합니다.
        google.maps.event.clearListeners(map, 'click');
        // 지도 클릭 이벤트를 등록하여 클릭한 위치를  저장
        map.addListener('click', function(event) {
            addMarker(map, event.latLng);
        endLatLng = event.latLng; // 클릭한 위치의 좌표를 endLatLng에 저장
        });
    });

flightPath.setMap(map);
}
//init map 끝

// 사용자가 지도에 마커 추가
function addMarker(map, location) {
    let marker = new google.maps.Marker({
        position: location,
        map: map,
        draggable: true // 마커를 드래그할 수 있도록 설정
    });
    

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
        if (session_data !== null && session_data[1] > 0 && session_data[3] > 0) {
            submitForm();
        }
        else {
            alert("위치를 정확하게 입력해주세요.");
        }
    },
    error: function(xhr, status, error) {
        console.error('Error:', error);
    }
    });
}
// 맵을 초기화하는 함수를 호출합니다.



