/**
 * Created by funkycoda on 7/11/2014.
 */

styles = [
    {
        "featureType": "landscape",
        "stylers": [
            {"color": "#f4f4f4"}
        ]
    }, {
        "featureType": "water",
        "stylers": [
            {"visibility": "simplified"}
        ]
    }, {
        "featureType": "water",
        "elementType": "labels",
        "stylers": [
            {"visibility": "off"}
        ]
    }, {
        "featureType": "water",
        "stylers": [
            {"color": "#808080"}
        ]
    }, {
        "featureType": "administrative",
        "stylers": [
            {"visibility": "on"}
        ]
    }, {
        "featureType": "administrative.country",
        "elementType": "labels",
        "stylers": [
            {"visibility": "on"}
        ]
    }, {
        "featureType": "road",
        "stylers": [
            {"visibility": "off"}
        ]
    }, {
        "featureType": "poi",
        "stylers": [
            {"visibility": "off"}
        ]
    }
];

styles_dark = [
    { elementType: "geometry", stylers: [{ color: "#242f3e" }] },
    { elementType: "labels.text.stroke", stylers: [{ color: "#242f3e" }] },
    { elementType: "labels.text.fill", stylers: [{ color: "#746855" }] },
    {
        featureType: "administrative",
        stylers: [{ "visibility": "on" }],
      },
      {
        featureType: "administrative.country",
        elementType: "labels.text.fill",
        stylers: [{ color: "#d59563", "visibility": "on" }],
      },
        {
      featureType: "poi",
      elementType: "labels.text.fill",
      stylers: [{ color: "#d59563", visibility: "off" }],
    },
    {
      featureType: "road",
      elementType: "geometry",
      stylers: [{ color: "#38414e", visibility: "off" }],
    },
    {
      featureType: "water",
      elementType: "geometry",
      stylers: [{ color: "#17263c" }],
    },
    {
      featureType: "water",
      elementType: "labels.text.fill",
      stylers: [{ color: "#515c6d" }],
    },
    {
      featureType: "water",
      elementType: "labels.text.stroke",
      stylers: [{ color: "#17263c" }],
    },
  ];

//var basicMapType = new google.maps.StyledMapType(styles,
//    {name: "Basic"});
