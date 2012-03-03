define([
   'underscore',
   'backbone',
   'src/models/species'
], function(_, Backbone, Species) {
   var SpeciesList;

   SpeciesList = Backbone.Collection.extend({
      model: Species,
      url: '/species',
      sortBy: 'name',
      sync: function(method, model, options) {
        var params;

        params = {
            data: {
                sortBy: this.sortBy,
                timeRange: {
                    from: this.timerange.from,
                    to: this.timerange.to
                }
            }
        };

        $.ajax(this.url, _.extend(options, params));
      }  
   });
   
   return SpeciesList;
});
