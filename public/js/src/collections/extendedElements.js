define([
   'underscore',
   'backbone',
   'src/models/extendedElement'
], function(_, Backbone, ExtendedElement) {
   var ExtendedElements;
   /**
    * A list of the model RegulatoryExtendedElement
    * that can be sorted by:
    * stage
    */
    ExtendedElements = Backbone.Collection.extend({
        model: ExtendedElement, 
        sortOn: 'beginning',
        order: 'asc',
        dirty: false,

        initialize: function(models, options) {
            this.options = options;
        },

        url: function() {
            return '/factors/' + this.options.factor + '/elements';
        },

        sync: function(method, model, options) {
            var params;

            params = {
        	    dataType: 'json',
                data: {
                    sortby: this.sortOn,
                    order: this.order
                }
            };

            this.dirty = true;
            $.ajax(this.url(), _.extend(options, params));
        }   
   });

   return ExtendedElements;
});
