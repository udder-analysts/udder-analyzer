define([
   'underscore',
   'backbone',
   'src/models/element'
], function(_, Backbone, Element) {
   var RegulatoryElementList;
   /**
    * A list of the model RegulatoryElement
    * that can be sorted by:
    * stage
    */
    RegulatoryElementList = Backbone.Collection.extend({
        model: Element, 
        url: '/elements',
        sortOn: 'beginning',
        order: 'asc',
        dirty: false,
      
        //displayProperties: {
         //   'Name': 'name'
       // },
		
		initialize: function(models, options) {
            // If a transcription factor is passed in, use it to buld the url
            if (options.experiment && options.gene && options.factor) {
                this.url = '/experiments/' + encodeURIComponent(options.experiment)
                + '/genes/' + encodeURIComponent(options.gene) + '/factors/' +  encodeURIComponent(options.factor)
                + '/elements';
            }
            else if (options.gene) {
            	this.url = '/genes/' + encodeURIComponent(options.gene) + '/elements';
            }
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
            $.ajax(this.url, _.extend(options, params));
        }   
   });

   return RegulatoryElementList;
});
