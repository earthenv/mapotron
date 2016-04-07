angular.module('mapotron.controllers')
  .controller('mapotronCtrl',
  	['getLayers','$rootScope','$compile','$http','$scope', '$state','$location', '$window', 'uiGmapGoogleMapApi','uiGmapIsReady',
   		function( getLayers, $rootScope, $compile,$http,$scope, $state, $location,  $window, uiGmapGoogleMapApi,uiGmapIsReady) {
        uiGmapGoogleMapApi.then(function(maps) {
        $scope.max=0.5;
        $rootScope.collections = getLayers();
        $rootScope.$watch(
          'map.overlayMapTypes',
          function(n,o) {
            if(n) {
              var overlays = [];
              angular.forEach(
                n,
                function(layer, index) {
                  if(layer.show) {
                   overlays.push(layer.name);
                 }
                }
              );
              $state.transitionTo(
                'map.basic',
                angular.extend($state.params,{layers: overlays.join(',')}),
                {notify: false}
              );

            }
          },
          true
        );
        $rootScope.$watch(
          'map.windows',
          function(n,o) {
              var markers = [];
              angular.forEach(
                n,
                function(marker, index) {
                  markers.push(marker.latitude.toFixed(5) + ' ' + marker.longitude.toFixed(5));

                }
              )
              $state.transitionTo(
                'map.basic',
                angular.extend($state.params,{markers: markers.join(',')}),
                {notify: false}
              );

          },
          true
        );

        $rootScope.map = {
          center: {
            latitude: parseFloat($state.params.y) || 0,
            longitude: parseFloat($state.params.x) || 0
          },
          zoom:  parseInt($state.params.z) || 3,
          events: {
            places_changed: function(place) {
              console.log(place);
            },
            maptypeid_changed: function(map, event, id) {
              var basemap = (map.getMapTypeId()==='hybrid')?'earth':'map';
              $state.transitionTo(
                'map.basic',
                angular.extend($state.params,{basemap:basemap}),
                {notify: false}
              );
            },
            bounds_changed: function() {
              var map = $scope.map.control.getGMap(),
                z = map.getZoom(),
                c = map.getCenter(),
                y = c.lat(),
                x = c.lng();

              $state.transitionTo(
                'map.basic',
                angular.extend($state.params,{z:z, x:x.toFixed(3),y:y.toFixed(3)}),
                {notify: false}
              );

              if(!$scope.$$phase) {
                $scope.$apply();
              }
            },
            click: function(map, event, coords) {
              var length = $scope.map.windows.push(
                {
                  id: coords[0].latLng.lat()+'-'+coords[0].latLng.lng(),
                  show: true,
                  options:{animation:0},
                  latitude: coords[0].latLng.lat(),
                  longitude:  coords[0].latLng.lng(),
                  data: undefined,
                  templateUrl: 'app/partials/map_infowindow.html'
                }
              );

              if(!$scope.$$phase) {
                $scope.$apply();
              }
              $http({"url":'/api/query/sample/'+$rootScope.collection+'/'+coords[0].latLng.lng()+'/'+coords[0].latLng.lat()}).then(
                function(result) {
                  $scope.map.windows[length-1].data= {model:result.data};
                  if(!$scope.$$phase) {
                    $scope.$apply();
                  }
              });
            }
          },
          windows: [],
          options: {
              scrollwheel: ($state.params.embed !== 'true'),
              streetViewControl: false,
              panControl: false,
              maxZoom: 18,
              minZoom: 1,
              styles: styles,
              rotateControl: true,
              mapTypeId: ($state.params.basemap=='earth')?google.maps.MapTypeId.SATELLITE:google.maps.MapTypeId.ROADMAP,
              rotateControlOptions: {
                position: google.maps.ControlPosition.TOP_RIGHT

              },
              fullscreenControl: true,
              fullscreenControlOptions: {
                position: google.maps.ControlPosition.TOP_RIGHT

              },
              mapTypeControl: true,
              mapTypeControlOptions: {
                style: google.maps.MapTypeControlStyle.LARGE,
                position: google.maps.ControlPosition.TOP_RIGHT

              },
              zoomControl: true,
              zoomControlOptions: {
                style: google.maps.ZoomControlStyle.LARGE,
                position: google.maps.ControlPosition.TOP_RIGHT
              },
          },
          control: {},
          overlayMapTypes: []
        };

        $rootScope.collection = $state.params.collections || 'cloud';
        angular.forEach(
          $rootScope.collections[$rootScope.collection].layers,
          function(layer, name, self) {
            $rootScope.map.overlayMapTypes[layer.index]={
              options: {
                getTileUrl: function(coord, zoom) {
                  return '/api/tile/{0}/{1}/{2}/{3}/{4}.png'
                      .format($scope.collection,name,zoom,coord.x,coord.y);
                },
                tileSize: new google.maps.Size(256, 256),
                name: name,
                id: layer.index,
                name: name,
                refresh: true,
                opacity: 0.65,
                maxZoom: 18,
              },
              properties: layer,
              name: name,
              id: layer.index,
              show: ($state.params.layers)?($state.params.layers.split(',').indexOf(name)>=0): layer.show,
              refresh: true,
              legend: layer.legend,
              setOpacity: function(_opacity) {
                var self = this;
                if(angular.isDefined(_opacity)) {
                    this.options.opacity = parseFloat(_opacity);
                    $scope.map.control.getGMap()
                      .overlayMapTypes.forEach(
                        function(mt) {
                          if(mt.layerId===self.id)
                            mt.setOpacity(parseFloat(_opacity));
                      });
                  }
                  return this.options.opacity;
                }
              }
            }
          );
          if($state.params.markers) {
            angular.forEach(
              $state.params.markers.split(','),
              function(marker,index) {
                var lat = parseFloat(marker.split(' ')[0]),
                  lng = parseFloat(marker.split(' ')[1]),
                  index = $scope.map.windows.push(
                  {
                    id: lat+'-'+lng,
                    show: true,
                    options:{animation:0},
                    latitude: lat,
                    longitude:  lng,
                    data: undefined,
                    templateUrl: 'app/partials/map_infowindow.html'
                  }
                );
                $http({"url":'/api/query/sample/'+$rootScope.collection + '/' +lng+'/'+lat}).then(
                  function(result) {
                    $scope.map.windows[index-1].data= {model:result.data};
                    if(!$scope.$$phase) {
                      $scope.$apply();
                    }
                });
              }
            );
          }
        });

  }
]).controller('controlCtrl',['$scope','$window',function($scope,$window){
    $scope.s=($window.innerWidth<500);
  }]).controller('tableCtrl',['$scope','$filter',function($scope,$filter){

    /* filters to return layers that are on or turned on by another layers'
     * querytoggle array
     */
    $scope.queryFilter = function(layers) {
      return function(l) {
          var querytoggles = $filter('flatten')(layers.filter(
              function(layer) {
                return (layer.show && layer.properties.querytoggle)
              }
            ).map(function(layer){
              if(layer.properties.querytoggle)
                return layer.properties.querytoggle;
            }));
            return ((l.show && !l.properties.querytoggle)||(querytoggles.indexOf(l.name)>=0));

      }
    }


  }]).controller('shareCtrl',['$scope','$window','$location',function($scope,$window,$location){
    $scope.feeds= [
      {"name":"Share on Twitter","icon":"fa-twitter-square", "url":"http://twitter.com/home?status="},
      {"name":"Share on Facebook","icon":"fa-facebook-square", "url":"https://www.facebook.com/sharer/sharer.php?u="},
      {"name":"Open in new window","icon":"fa-external-link","url":""}
    ];
    $scope.share = function(feed) {
      $window.open(feed.url+ $location.absUrl());
    }

  }]).controller('placesCtrl',['$scope','$rootScope',function($scope,$rootScope){
      $scope.places = [{"name":"Nairobi","longitude":36.81667,"latitude":-1.28333},{"name":"Bogota","longitude":-74.02986,"latitude":4.624335},{"name":"Los Angeles","longitude":-118.24368,"latitude":34.05223},{"name":"Kuala Lumpur","longitude":101.68653,"latitude":3.1412},{"name":"Moscow","longitude":37.61556,"latitude":55.75222},{"name":"Lima","longitude":-77.02824,"latitude":-12.04318},{"name":"New York","longitude":-74.00597,"latitude":40.71427},{"name":"San Francisco","longitude":-122.41942,"latitude":37.77493},{"name":"Riyadh","longitude":46.72185,"latitude":24.68773},{"name":"Canberra","longitude":149.12807,"latitude":-35.28346},{"name":"Beijing","longitude":116.39723,"latitude":39.9075},{"name":"Quito","longitude":-78.52495,"latitude":-0.22985},{"name":"Mumbai","longitude":72.88261,"latitude":19.07283},{"name":"Cape Town","longitude":18.42322,"latitude":-33.92584},{"name":"Sydney","longitude":151.20732,"latitude":-33.86785},{"name":"Auckland","longitude":174.76667,"latitude":-36.86667},{"name":"London","longitude":-0.12574,"latitude":51.50853},{"name":"Abidjan","longitude":-4.01266,"latitude":5.30966},{"name":"Buenos Aires","longitude":-58.37723,"latitude":-34.61315},{"name":"Berlin","longitude":13.41053,"latitude":52.52437},{"name":"Sao Paulo","longitude":-62.9,"latitude":-7.23333}];
    }]).filter('slashify',function(){
        return function(input) {
          if(input)
            return input.replace(/ /g,'_').replace(/\(/g,'').replace(/\)/g,'');
        }
    }).filter('lat', function () {
    return function (input, decimals) {
        if (!decimals) decimals = 0;
        input = input * 1;
        var ns = input > 0 ? "N" : "S";
        input = Math.abs(input);
        var deg = input.toFixed(decimals);
        return deg + "°" + ns;
    }
})
// formats a number as a longitude (e.g. -80.02... => "80°1'24"W")
.filter('lon', function () {
    return function (input, decimals) {
        if (!decimals) decimals = 0;
        input = input * 1;
        var ew = input > 0 ? "E" : "W";
        input = Math.abs(input);
        var deg = input.toFixed(decimals);
        return deg + "°" + ew;
    }
});
