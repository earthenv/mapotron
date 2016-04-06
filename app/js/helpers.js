// For convenience...
/**
 * https://gist.github.com/1049426
 *
 * Usage:
 *
 *   "{0} is a {1}".format("Tim", "programmer");
 *
 */
String.prototype.format = function(i, safe, arg) {
  function format() {
      var str = this,
          len = arguments.length+1;

      for (i=0; i < len; arg = arguments[i++]) {
          safe = typeof arg === 'object' ? JSON.stringify(arg) : arg;
          str = str.replace(RegExp('\\{'+(i-1)+'\\}', 'g'), safe);
      }
      return str;
  }
  format.native = String.prototype.format;
  return format;
}();

angular.module('env-filters', [])
.filter('percentage', function ($window) {
    return function (input, decimals, suffix) {
        decimals = angular.isNumber(decimals)? decimals :  1;
        suffix = suffix || '%';
        if ($window.isNaN(input)) {
            return '';
        }
        return Math.round(input/10000 * Math.pow(10, decimals + 2))/Math.pow(10, decimals) + suffix
    };
}).filter('theta', function ($window,$filter) {
    return function (input) {
        function calcMonthDay(days){
          var m=0, d=0, months = [{"m":"Jan","d":31},{"m":'Feb',"d":28},{"m":'Mar',"d":31},{"m":'Apr',"d":30},{"m":'May',"d":31},{"m":'Jun',"d":30},{"m":'Jul',"d":31},{"m":'Aug',"d":31},{"m":'Sep',"d":30}, {"m":'Oct',"d":31},{"m":'Nov',"d":30},{"m":'Dec',"d":31}];
            while(d<days&&m<12) {
              d+=months[m].d;
              m++;
            }
            return {m:months[m-1].m,d:Math.ceil((days-(d-months[m-1].d)))};
        }
        var md = calcMonthDay(parseFloat(input)*(((0.1/360)*365)));

        return md.m + ' ' + md.d;
      }

}).filter('sci', function ($window,$filter) {
    return function (input) {
        return Math.round(parseFloat(input)*0.1);
      }

}).filter('standard-deviation', function ($window,$filter) {
    return function (input) {
      if (input < 0) {
        return null
      } else {
        return $filter('number')(input/100,0)
      }
    };
}).filter('hotspots', function ($window) {
    return function (input) {
        return input
    };
}).filter('predict', function ($window,$filter) {
    return function (input) {
        if (input < 0) {
          return null
        } else {
          return $filter('number')(input,10)
        }
    };
}).filter('seasonality', function ($window) {
    return function (input) {
        return input
    };
}).filter('km2', function ($window) {
    return function (input, decimals, suffix) {
        suffix = suffix || ' km²';
        if ($window.isNaN(parseFloat(input))) {
            return '';
        }
        return input + suffix
    };
}).filter('units', function ($window,$filter) {
  return function(value, units) {
    return $filter(units)(value);
  }
})
