
        
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
let line;
let polygon;

function initMap() {
                    //맵 보여주는 함수
    var selectedOption = $('#farmSelect').find('option:selected');
    var locationString = selectedOption.data("loc");
    var listString = selectedOption.data("obj");
    // 지도 위치
    var loca = JSON.parse(locationString.replace(/'/g, '"'));
    var initialLatLng = new google.maps.LatLng(loca.lat, loca.lng);
    // 경계선 위치
    var fieldPaths = JSON.parse(listString.replace(/'/g, '"'));
    console.log(fieldPaths);

    var mapOptions = {
        center: initialLatLng,
        zoom: 20,
        mapTypeControl: false,
        mapTypeId: google.maps.MapTypeId.HYBRID,
    };
    let map = new google.maps.Map(document.getElementById('map'), mapOptions);

    polygon = new google.maps.Polygon({
        paths: fieldPaths,
        strokeColor: '#FF0000', // 선 색상
        strokeOpacity: 0.6, // 선 투명도
        strokeWeight: 5, // 선 두께
        fillColor: '#FFFFFF', // 내부 색상
        fillOpacity: 0.2 // 내부 투명도
    });
    polygon.setMap(map);

    $('#farmSelect').change(function () {
        if (polygon) {
            polygon.setMap(null);
        }

        var selectedOption = $(this).find('option:selected');
        var locationString = selectedOption.data("loc");
        
        var loca = JSON.parse(locationString.replace(/'/g, '"'));
        var locationLatLng = new google.maps.LatLng(loca.lat, loca.lng);;
        map.setCenter(locationLatLng);
        
        var listString = selectedOption.data("obj");
        var fieldPaths = JSON.parse(listString.replace(/'/g, '"'));
        polygon = new google.maps.Polygon({
            paths: fieldPaths,
            strokeColor: '#FF0000', // 선 색상
            strokeOpacity: 0.6, // 선 투명도
            strokeWeight: 5, // 선 두께
            fillColor: '#FFFFFF', // 내부 색상
            fillOpacity: 0.2 // 내부 투명도
        });
        polygon.setMap(map);
    });
    //polyline 그리기 위한 좌표값, 임의의 값임

    // 사용자가 지도를 클릭할 때마다 마커 추가




    // "create_startpoint" 버튼을 클릭했을 때 start_point를 설정할 수 있도록 이벤트를 등록
        document.getElementById('create_startpoint_button').addEventListener('click', function() {
        // 기존의 이벤트 리스너를 모두 제거합니다.
            google.maps.event.clearListeners(map, 'click');
            // 지도 클릭 이벤트를 등록하여 클릭한 위치를 endPoint에 저장
            map.addListener('click', function(event) {
            // 새로운 끝점을 선택할 때마다 이전의 끝점 마커를 제거합니다.
                if (endMarker) {
                    addStart(map, event.latLng);
                    drawLine(map);

                }
                else {
                    addStart(map, event.latLng);

                }
            });
        }); 



    document.getElementById('create_endpoint_button').addEventListener('click', function() {
    // 기존의 이벤트 리스너를 모두 제거합니다.
        google.maps.event.clearListeners(map, 'click');
        // 지도 클릭 이벤트를 등록하여 클릭한 위치를 endPoint에 저장
        map.addListener('click', function(event) {
        // 새로운 끝점을 선택할 때마다 이전의 끝점 마커를 제거합니다.
            if (startMarker) {
                // startMarker가 이미 있다면 endMarker를 추가하고 선을 그린다
                addEnd(map, event.latLng);
                drawLine(map);
            }
            else {
                alert('시작점을 먼저 설정해주십시오.');
            }
        });
        
    });
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
    startPoint = location;
    
}

function addEnd(map, location) {
    // 새로운 시작점 마커를 추가합니다.
    if (endMarker) {endMarker.setMap(null);}

    endMarker = new google.maps.Marker({
        position: location,
        map: map,
        icon: 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png' // 파란색 마커 아이콘 사용
    });
    endPoint = location;
}

//startPoint를 서버로 전송하는 함수
document.getElementById('save_button').addEventListener('click', function() {
    savePoint();
});

function drawLine(map) {

    // 이전에 그린 선이 있다면 제거
    if (line) {
        line.setMap(null);
    }

    // Polyline 그리기
    line = new google.maps.Polyline({
        path: [startPoint, endPoint],
        geodesic: true,
        strokeColor: '#0000FF',
        strokeOpacity: 1.0,
        strokeWeight: 2,
        icons: [{
            icon: {
                path: google.maps.SymbolPath.FORWARD_CLOSED_ARROW,
                scale: 5
            },
            offset: '100%'
        }]
    });

    line.setMap(map);
}   

function savePoint() {
    var workNameInput = document.getElementById('work_name_input');
    var workName = workNameInput.value.trim();
    
    if (startMarker != undefined && endMarker != undefined)
    {
        pointsCoordinates.length = 0;
        pointsCoordinates.push(startMarker.getPosition().toJSON());
        pointsCoordinates.push(endMarker.getPosition().toJSON());
    }
    else {
        pointsCoordinates.length = 0;
        pointsCoordinates.push({lat: 0, lng: 0});
        pointsCoordinates.push({lat: 0, lng: 0});
    }

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
        if (workName === '') {
            var warningElements = document.querySelectorAll('.text-danger');
            warningElements.forEach(function(element) {
            element.innerText = '';
            document.getElementById('work_name_warning').innerText = '작업 이름을 입력하세요!';
            })
        }
        else if(session_data == null || session_data[0] === 0 && session_data[2] === 0) {
            var warningElements = document.querySelectorAll('.text-danger');
            warningElements.forEach(function(element) {
            element.innerText = '';
            document.getElementById('location_warning').innerText = '경로 설정을 제대로 하십시오!';
            })
        }
        else {
            alert("경작지가 성공적으로 추가되었습니다!");
            document.getElementById('yourForm').submit();
        }
    },
    error: function(xhr, status, error) {
        console.error('Error:', error);
    }
    });
}

window.onload = function() {
    initMap();
};