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
        url: '/experiments',
        sortBy: 'name',
        //displayProperties: {
        //    'Stage': 'stage'
		//},
		filter: {},

		initialize: function(models, options) {
            this.timerange = {};

		    // If a comparison is passed in, use it to buld the url
			if (options.species && options.comparison) {
				this.url = '/species/' + encodeURIComponent(options.species) + '/comparisons/' +
				encodeURIComponent(options.comparison) + '/experiments';
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
                    },
                    filter: this.filter,
                    value: this.value
                }
            };

            $.ajax(this.url, _.extend(options, params));
        }
   });

   return ExperimentList;
});
