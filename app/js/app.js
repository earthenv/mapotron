'use strict';

angular.module('mapotron.controllers',[]);

// Declare app level module which depends on filters, and services
angular.module('mapotron', [
  'mapotron.controllers',
  'ui.router',
  'uiGmapgoogle-maps'
])
.config(function($stateProvider, $urlRouterProvider, $locationProvider) {

  $urlRouterProvider.otherwise("/");

  $stateProvider
    .state(
      'map',
      {
        abstract: true,
        templateUrl: 'app/partials/mapotron.html',
        controller: 'mapotronCtrl'
      }
    )
    .state(
      'map.basic',
      {
        views: {
          'map' : {templateUrl: 'app/partials/map.html'},
          'controls': {templateUrl: 'app/partials/map_controls.html'},
          'legend': {templateUrl: 'app/partials/map_legend.html'}
        },
        url: '/'
      }
    )
    //Gets rid of the # in the querystring. Wont work on IE
    $locationProvider.html5Mode(true);

});
