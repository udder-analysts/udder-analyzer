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
      url: '/transcriptionFactor',
      sortBy: 'name',
      
      displayProperties: {
      'Name': 'name'
      },
		
		initialize: function(models, options) {
            // If a gene is passed in, use it to buld the url
            if (options.gene) {
                this.url = '/gene/' + encodeURIComponent(options.gene) + '/transcriptionFactor';
            }
        },
      
      sync: function(method, model, options) {
        var params;

        params = {
        	dataType: 'json',
            data: {
                sortBy: this.sortBy
            }
        };

        $.ajax(this.url, _.extend(options, params));
      }   
   });

   return FactorList;
});
