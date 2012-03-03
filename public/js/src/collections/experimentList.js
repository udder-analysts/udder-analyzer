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
      sync: function(method, model, options) {
        var params;

        params = {
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
