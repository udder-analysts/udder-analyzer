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
      sortOn: 'name',
      sortOrder: 'asc',
      dirty: false,
      
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
                sortby: this.sortOn,
                order: this.sortOrder,
                reg: this.regulation
            }
        };

        this.dirty = true;
        $.ajax(this.url, _.extend(options, params));
      }
   });

   return GeneList;
});
