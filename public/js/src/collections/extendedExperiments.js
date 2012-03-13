define([
   'underscore',
   'backbone',
   'src/models/extendedExperiment'
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
        sortOn: 'dateof',
        sortOrder: 'asc',
		filter: {},
        dirty: false,

		initialize: function(models, options) {
            this.gene = options.gene;
		},

        url: function() {
            return '/experimentsForGene/' + encodeURIComponent(this.gene);
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
            $.ajax(this.url(), _.extend(options, params));
        }
   },{
        type: Experiment.type
    });

   return ExperimentList;
});
