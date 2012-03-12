define([
   'underscore',
   'backbone'
], function(_, Backbone) {
   var Comparison;

   /* 
    * Comparison
    * type - <string> type of Comparison
    */
   Comparison = Backbone.Model.extend({
      defaults: {
         selected: false
      },

      toggleSelect: function() {
         this.set({ select: !this.get('select') });
      }
    },
    // Class Properties
    {
        type: 'comparison',
        displayProperties: [
            {
                name: 'Comparison',
                property: 'comparison',
                type: 'text'
            }
        ]
   });

   return Comparison;
});
