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
        
let pointsCoordinates = [];
let startMarker, endMarker;
var startLatLng, endLatLng;
var startPoint; // 클릭한 시작점의 좌표를 저장할 변수
var endPoint;

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

    // "create_startpoint" 버튼을 클릭했을 때 start_point를 설정할 수 있도록 이벤트를 등록
    document.getElementById('create_startpoint_button').addEventListener('click', function() {
    // 기존의 이벤트 리스너를 모두 제거합니다.
        google.maps.event.clearListeners(map, 'click');
        // 지도 클릭 이벤트를 등록하여 클릭한 위치를 endPoint에 저장
        map.addListener('click', function(event) {
        // 새로운 끝점을 선택할 때마다 이전의 끝점 마커를 제거합니다.
            addStart(map, event.latLng);
            startLatLng = event.latLng; // 클릭한 위치의 좌표를 startLatLng에 저장
        });
    }); 



    document.getElementById('create_endpoint_button').addEventListener('click', function() {
    // 기존의 이벤트 리스너를 모두 제거합니다.
        google.maps.event.clearListeners(map, 'click');
        // 지도 클릭 이벤트를 등록하여 클릭한 위치를 endPoint에 저장
        map.addListener('click', function(event) {
        // 새로운 끝점을 선택할 때마다 이전의 끝점 마커를 제거합니다.
            addEnd(map, event.latLng);
            endLatLng = event.latLng; // 클릭한 위치의 좌표를 endLatLng에 저장
        });
    });

flightPath.setMap(map);
}
//init map 끝


function addStart(map, location) {
    // 새로운 시작점 마커를 추가합니다.
    
    if (startMarker) {startMarker.setMap(null);}
    
    startMarker = new google.maps.Marker({
        position: location,
        map: map,
        icon: 'http://maps.google.com/mapfiles/ms/icons/red-dot.png' // 빨간색 마커 아이콘 사용
    });
    
}

function addEnd(map, location) {
    // 새로운 시작점 마커를 추가합니다.
    if (endMarker) {endMarker.setMap(null);}

    endMarker = new google.maps.Marker({
        position: location,
        map: map,
        icon: 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png' // 파란색 마커 아이콘 사용
    });
}

//startPoint를 서버로 전송하는 함수
document.getElementById('save_button').addEventListener('click', function() {
    savePoint();
});

function savePoint() {
    
    pointsCoordinates.push(startMarker.getPosition().toJSON());
    pointsCoordinates.push(endMarker.getPosition().toJSON());

    // 서버로 마커 좌표를 전송
$.ajax({
    url: 'save_points/',
    type: 'POST',
    headers: {
        'X-CSRFToken': getCookie('csrftoken')
    },
    contentType: 'application/json',
    data: JSON.stringify({ 'points': pointsCoordinates }),
    success: function(data) {
        var session_data = data.data;
        if (session_data !== null && session_data[0] > 0 && session_data[2] > 0) {
            alert("경작지가 성공적으로 추가되었습니다!")
            document.getElementById('yourForm').submit();
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