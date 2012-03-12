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
    },
   // Class Properties
    {
        type: 'factor',
        displayProperties: [
            {
                name: 'Name',
                property: 'name',
                type: 'text'
            }
        ]
   });

   return TranscriptionFactor;
});
