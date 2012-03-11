define([
   'underscore',
   'backbone'
], function(_, Backbone) {
   var Experiment;

   /* 
    * Experiment
    * experimenter <string> The name of the person performing experiment
    * date <string> The date the experiment took place
    * location <string> The location the experiment took place
    * comparison <string> The comparison being made in the experiment
    * species <string> The name of the species the experiment is studying
    */
   Experiment = Backbone.Model.extend({
      defaults: {
         selected: false
      },

      toggleSelect: function() {
         this.set({ select: !this.get('select') });
      }
       },
    // Class Properties
    {
        type: 'experiment',
        displayProperties: {
            'Experimenter': 'experimenter',
            'Date': 'dateof',
            'Location': 'location'
        }
   });

   return Experiment;
});
