define([
   'underscore',
   'backbone'
], function(_, Backbone) {
   var ExtendedFactor;

   /* 
    * TranscriptionFactor
    * name - <string> name of the TranscriptionFactor
    * reg_element <int> the ID of the associated RegulatoryElement
    */
   ExtendedFactor = Backbone.Model.extend({
    },
   // Class Properties
    {
        type: 'factor',
        displayProperties: [
            {
                name: 'Name',
                property: 'name',
                type: 'text'
            },
            {
                name: 'Models',
                property: 'models',
                type: 'number'
            },
            {
                name: 'Genes',
                property: 'genes',
                type: 'number'
            },
            {
                name: 'Occurences',
                property: 'occurences',
                type: 'number'
            }
        ]
   });

   return ExtendedFactor;
});
