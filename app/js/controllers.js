angular.module('mapotron.controllers')
  .controller('mapotronCtrl',
  	['$rootScope','$scope', '$state','$location',

   		function($rootScope, $scope, $state, $location) {

      $rootScope.$state = $state;
      $scope.max=0.5;
      $scope.showLegend = true;
      $scope.hasLengend = false;
      $scope.showControls = true;
      $scope.map = {
            center: {latitude:0,longitude:0},
            zoom: 2,
            options: {
                streetViewControl: false,
                panControl: false,
                maxZoom: 18,
                minZoom: 1,
                styles:  [
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
	],
                zoomControlOptions: {
        style: google.maps.ZoomControlStyle.LARGE,
        position: google.maps.ControlPosition.TOP_RIGHT
    },
            },
            overlayMapTypes: _.map(
                  layers,
                  function(layer) {
                    return {
                      options: {
                        getTileUrl : function (coords, zoom) {
                          return '/api/tile/{0}/{1}/{2}/{3}.png'
                            .format(layer.id,zoom,coords.x,coords.y);
                        },
                        tileSize: new google.maps.Size(256, 256),
                        name: layer,
                        opacity: 0.7,
                        maxZoom: 18
                      },
                      id: layer.id,
                      title: layer.title,
                      show: false,
                      refresh: true,
                      opacity: function(_opacity) {
                          if(angular.isDefined(_opacity)) {
                            this.options.opacity = parseFloat(_opacity);
                          }
                          return this.options.opacity;
                        }
                    }
                  }
                )
        };
      }

  ]);
