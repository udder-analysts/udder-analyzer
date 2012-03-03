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
      url: '/comparison',
      sortBy: 'name',
      sync: function(method, model, options) {
        var params;

        params = {
            data: {
                sortBy: this.sortBy
            }
        };

        $.ajax(this.url, _.extend(options, params));
      }   
   });

   return ComparisonList;
});

