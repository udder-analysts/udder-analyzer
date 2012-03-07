define([
   'underscore',
   'backbone'
], function(_, Backbone) {
   var GeneSequence;

   /* 
    * GeneSequence
    * id <int> id of GeneSequence (also id of Genes)
    * sequence <string> 2000 character string of ACTG which is the sequence
    */
   GeneSequence = Backbone.Model.extend({
      defaults: {
         name: 'unknown',
         selected: false
      },

      toggleSelect: function() {
         this.set({ select: !this.get('select') });
      }
       },
    // Class Properties
    {
        type: 'geneSequence',
        displayProperties: {
            'Sequence': 'sequence',
            'Id': 'id'
        }
   });

   return GeneSequence;
});
