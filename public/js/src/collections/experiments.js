define([
   'underscore',
   'backbone',
   'src/models/experiment'
], function(_, Backbone, Experiment) {
   var ExperimentList;
   /**
    * A list of the model Experiment
    * that can be sorted by:
    * experimenter
    * date
    * genes total
    * up
    * down
    */
    ExperimentList = Backbone.Collection.extend({
        model: Experiment,
        url: '/experiment',
        sortBy: 'name',
        displayProperties: {
            'Stage': 'stage'
		},

		initialize: function(models, options) {
            this.timerange = {};

		    // If a comparison is passed in, use it to buld the url
			if (options.comparison) {
				this.url = '/comparison/' + encodeURIComponent(options.comparison) + '/experiment';
			}
			else if(options.gene) {
			    this.url = '/gene/' + encodeURIComponent(options.gene) + '/experiment/';
			}
		},
        sync: function(method, model, options) {
            var params;

            params = {
        	    dataType: 'json',
                data: {
                    sortBy: this.sortBy,
                    timeRange: {
                        from: this.timerange.from,
                        to: this.timerange.to
                    }
                }
            };

            $.ajax(this.url, _.extend(options, params));
        }
   });

   return ExperimentList;
});
