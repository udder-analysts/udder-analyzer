define([
   'underscore',
   'backbone',
   'src/models/transcriptionFactor'
], function(_, Backbone, transcriptionFactor) {
   var FactorList;
   /**
    * A list of the model Comparison
    * that can be sorted by:
    * stage
    */
   FactorList = Backbone.Collection.extend({
      model: Comparison, 
      url: '/transcriptionFactor',
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

   return FactorList;
});
