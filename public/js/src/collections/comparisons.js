define([
   'underscore',
   'backbone',
   'src/models/comparison'
], function(_, Backbone, Comparison) {
   var ComparisonList;
   /**
    * A list of the model Comparison
    * that can be sorted by:
    * stage
    */
    ComparisonList = Backbone.Collection.extend({
        model: Comparison, 

        url: '/comparisons',

        sortOn: 'comparison',
        sortOrder: 'asc',

        dirty: false,

        //displayProperties: {
        //    'Stage': 'stage'
        //},

        initialize: function(models, options) {
            // If a species is passed in, use it to buld the url
            if (options.species) {
                this.url = '/species/' + encodeURIComponent(options.species) + '/comparisons';
            }
        },

        sync: function(method, model, options) {
            var params;

            params = {
                dataType: 'json',
                data: {
                    sortby: this.sortOn,
                    order: this.sortOrder
                }
            };

            this.dirty = true;
            $.ajax(this.url, _.extend(options, params));
        }   
    });

    return ComparisonList;
});

