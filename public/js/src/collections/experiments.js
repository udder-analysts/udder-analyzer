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
        sortOn: 'dateof',
        sortOrder: 'asc',
		filter: {},
        dirty: false,

		initialize: function(models, options) {
            this.timerange = {};

            if (options.geneDetail) {
                this.url = '/experimentsForGene/' + encodeURIComponent(options.gene);
            }
		    // If a comparison is passed in, use it to buld the url
			else if (options.species && options.comparison) {
				this.url = '/species/' + encodeURIComponent(options.species) + '/comparisons/' +
				encodeURIComponent(options.comparison) + '/experiments';
			}
		},
        sync: function(method, model, options) {
            var params;

            params = {
        	    dataType: 'json',
                data: {
                    sortby: this.sortOn,
                    order: this.sortOrder,
                    filter: this.filter
                }
            };

            this.dirty = true;
            $.ajax(this.url, _.extend(options, params));
        }
   },{
        type: Experiment.type
    });

   return ExperimentList;
});
