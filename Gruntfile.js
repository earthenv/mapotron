module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    uglify: {
      options: {
         mangle: false
      },
      build: {
        src: [
           'app/js/helpers.js',
	   'bower_components/angular/angular.min.js',
	   'bower_components/angular-ui-router/release/angular-ui-router.js',
	   'bower_components/lodash/dist/lodash.min.js',
           'bower_components/angular-google-maps/dist/angular-google-maps.js',
           'app/js/app.js',
           'app/js/controllers.js'],
        dest: 'app/app.min.js'
      }
    }
  });

  // Load the plugin that provides the "uglify" task.
  grunt.loadNpmTasks('grunt-contrib-uglify');

  // Default task(s).
  grunt.registerTask('default', ['uglify']);

};

