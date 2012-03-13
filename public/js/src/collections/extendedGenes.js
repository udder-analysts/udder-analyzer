define([
   'underscore',
   'backbone',
   'src/models/extendedGene'
], function(_, Backbone, ExtendedGene) {
   var ExtendedGenes;
   /**
    * A list of the model Gene
    * that can be sorted by:
    * name (or abbr?)
    * chromosome
    * begin site
    * end site
    */
   ExtendedGenes = Backbone.Collection.extend({
      model: ExtendedGene,
      url: '/genes',
      sortOn: 'name',
      sortOrder: 'asc',
      dirty: false,
      
		initialize: function(models, options) {
        },
      
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
   },
   {
    type: ExtendedGene.type
   });

   return ExtendedGenes;
});
