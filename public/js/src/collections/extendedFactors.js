define([
   'underscore',
   'backbone',
   'src/models/extendedFactor'
], function(_, Backbone, ExtendedFactor) {
   var ExtendedFactors;
   /**
    * A list of the model Comparison
    * that can be sorted by:
    * stage
    */
   ExtendedFactors = Backbone.Collection.extend({
      model: ExtendedFactor, 
      url: '/factors',
      sortOn: 'name',
      sortOrder: 'asc',
      dirty: false,

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

   return ExtendedFactors;
});
