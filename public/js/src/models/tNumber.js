define([
   'underscore',
   'backbone'
], function(_, Backbone) {
   var TNumber;

   /* 
    * TNumber
    * tnumber <string> The tNumber 
    * reg_element <int> the regulatory element associated with the tNumber
    */
   TNumber = Backbone.Model.extend({
      defaults: {
         selected: false
      },

      toggleSelect: function() {
         this.set({ select: !this.get('select') });
      }
   });

   return TNumber;
});
