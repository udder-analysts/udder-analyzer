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
        url: '/regulatoryElement',
        sortBy: 'name',
      
        displayProperties: {
            'Id': 'id'
        },
		
		initialize: function(models, options) {
            // If a transcription factor is passed in, use it to buld the url
            if (options.transcriptionFactor) {
                this.url = '/transcriptionFactor/' +  encodeURIComponent(options.transcriptionFactor)
                + '/regulatoryElement';
            }
            else if (options.gene) {
            	this.url = '/gene/' + options.gene + '/regulatoryElement';
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

   return RegulatoryElementList;
});
