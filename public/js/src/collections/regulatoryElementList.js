define([
   'underscore',
   'backbone',
   'src/models/regulatoryElement'
], function(_, Backbone, RegulatoryElement) {
   var RegulatoryElementList;
   /**
    * A list of the model RegulatoryElement
    * that can be sorted by:
    * stage
    */
   RegulatoryElementList = Backbone.Collection.extend({
      model: RegulatoryElement, 
      url: '/regulatoryElement',
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

   return RegulatoryElementList;
});
