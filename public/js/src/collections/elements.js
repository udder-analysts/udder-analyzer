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
        sortBy: 'name',
        order: 'asc',
      
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
            	this.url = '/genes/' + options.gene + '/elements';
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

   return RegulatoryElementList;
});
