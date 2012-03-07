require.config({
    paths: {
        'jquery': 'lib/jquery-1.7.1.min',
        'underscore': 'lib/underscore-1.3.1',
        'backbone': 'lib/backbone-0.9.1',
        'publisher': 'lib/publisher'
    }
});

require([
    'jquery',
    'underscore',
    'backbone',
    'src/router'
], function($, _, Backbone, App) {
    var app = new App();
    Backbone.history.start();
});
