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
    'src/model/species.js'
], function($, _, Backbone, Species) {
    console.log("hello world");
});
