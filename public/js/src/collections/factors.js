define([
   'underscore',
   'backbone',
   'src/models/factor'
], function(_, Backbone, Factor) {
   var FactorList;
   /**
    * A list of the model Comparison
    * that can be sorted by:
    * stage
    */
   FactorList = Backbone.Collection.extend({
      model: Factor, 
      url: '/factors',
      sortBy: 'name',
      order: 'asc',
      
      //displayProperties: {
      //'Name': 'name'
      //},
		
		initialize: function(models, options) {
            // If a gene is passed in, use it to buld the url
            if (options.experiment && options.gene) {
                this.url = '/experiments/' + encodeURIComponent(options.experiment)
                + '/genes/' + encodeURIComponent(options.gene) + '/factors';
            }
        },
      
      sync: function(method, model, options) {
        var params;

        params = {
        	dataType: 'json',
            data: {
                sortBy: this.sortBy,
                order: this.order
            }
        };

        $.ajax(this.url, _.extend(options, params));
      }   
   });

   return FactorList;
});
