'use strict';

/* Directives */


angular.module('mapotron.directives', []).
  directive('appVersion', ['version', function(version) {
    return function(scope, elm, attrs) {
      elm.text(version);
    };
  }]).directive('imageonload', function() {
    return {
        restrict: 'A',
        link: function(scope, element, attrs) {
            element.bind('error', function(event) {
            	var self = this;
                scope.images = scope.images.filter(
                	function(image){ return image != self.src}
                );
            });
        }
    };
});