define([
   'underscore',
   'backbone',
   'src/models/species'
], function(_, Backbone, Species) {
   var SpeciesList;
   /**
    * A list of the model Species
    * that can be sorted by:
    * name
    */
   SpeciesList = Backbone.Collection.extend({
      model: Species,
      url: '/species',
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
   
   return SpeciesList;
});
