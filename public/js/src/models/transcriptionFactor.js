define([
   'underscore',
   'backbone'
], function(_, Backbone) {
   var TranscriptionFactor;

   /* 
    * TranscriptionFactor
    * name - <string> name of the TranscriptionFactor
    * reg_element <int> the ID of the associated RegulatoryElement
    */
   TranscriptionFactor = Backbone.Model.extend({
      defaults: {
         selected: false
      },

      toggleSelect: function() {
         this.set({ select: !this.get('select') });
      }
   });

   return TranscriptionFactor;
});
