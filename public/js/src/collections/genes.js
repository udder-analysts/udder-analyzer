define([
   'underscore',
   'backbone',
   'src/models/gene'
], function(_, Backbone, Gene) {
   var GeneList;
   /**
    * A list of the model Gene
    * that can be sorted by:
    * name (or abbr?)
    * chromosome
    * begin site
    * end site
    */
   GeneList = Backbone.Collection.extend({
      model: Gene,
      url: '/gene',
      sortBy: 'name',
      
      	displayProperties: {
        'Name': 'name'
        },
		
		initialize: function(models, options) {
            // If an experiment is passed in, use it to buld the url
            if (options.experiment) {
                this.url = '/experiment/' + encodeURIComponent(options.experiment) + '/gene';
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

   return GeneList;
});
