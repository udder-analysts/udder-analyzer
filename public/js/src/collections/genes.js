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
      url: '/genes',
      sortBy: 'name',
      order: 'asc',
      
      	//displayProperties: {
        //'Name': 'name'
        //},
		
		initialize: function(models, options) {
            // If an experiment is passed in, use it to buld the url
            if (options.experiment) {
                this.url = '/experiments/' + encodeURIComponent(options.experiment) + '/genes';
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

   return GeneList;
});
