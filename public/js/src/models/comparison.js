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
   });

   return Comparison;
});
