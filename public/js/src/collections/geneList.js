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

   return GeneList;
});
