define([
   'underscore',
   'backbone'
], function(_, Backbone) {
   var RegulatoryElement;

   /* 
    * RegulatoryElement
    * id <int> The auto-incremented ID of the regulatory element
    * beginning <int>
    * length <int>
    * sense  <int>
    * model <string>
    * reg_sequence <string>
    * la <float>
    * la_slash <float>
    * lq <float>
    * ld <float>
    * lpv <float>
    * sc <float>
    * sm <float>
    * spv <float>
    * ppv <float>
    * gene_id <int> The ID of the associated gene
    * experiment_id <int> The ID of the associated experiment
    */
   RegulatoryElement = Backbone.Model.extend({
      defaults: {
         selected: false
      },

      toggleSelect: function() {
         this.set({ select: !this.get('select') });
      }
   });

   return RegulatoryElement;
});
