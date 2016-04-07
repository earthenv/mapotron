'use strict';

angular.module('mapotron.controllers',[]);

// Declare app level module which depends on filters, and services
angular.module('mapotron', [
  'ngAnimate',
  'as.sortable',
  'mapotron.directives',
  'mapotron.controllers',
  'mapotron.services',
  'ui.router',
  'angular.filter',
  'ui.bootstrap',
  'uiGmapgoogle-maps',
  'env-filters'
]).config(function(uiGmapGoogleMapApiProvider) {
    uiGmapGoogleMapApiProvider.configure({
        key: 'AIzaSyByw04NVoEsh8bfC0X_sBBA5_-pAovcD1c',
        v: '3.23', //defaults to latest 3.X anyhow
        libraries: 'places,weather,geometry,visualization'
    });
})
.config(function($stateProvider, $urlRouterProvider, $locationProvider) {

  $urlRouterProvider.otherwise("/3/0/0");

  $stateProvider
    .state(
      'map', //this view contains the bones of the Species Info pages (name, pic, & search bar)
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
        url: '/{z}/{x}/{y}?collections&layers&markers&basemap&embed'
      }
    )
    //Gets rid of the # in the querystring. Wont work on IE
    $locationProvider.html5Mode(true);

});
