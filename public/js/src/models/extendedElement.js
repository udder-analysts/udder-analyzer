define([
   'underscore',
   'backbone'
], function(_, Backbone) {
   var ExtendedElement;

   /* 
    * ExtendedElement
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
    ExtendedElement = Backbone.Model.extend({
    },
    // Class Properties
    {
        type: 'element',
        displayProperties: [
            {
                name: 'Comparison',
                property: 'comparison',
                type: 'text'
            },
            {
                name: 'Experimenter',
                property: 'experimenter',
                type: 'text'
            },
            {
                name: 'Date',
                property: 'dateof',
                type: 'date'
            },
            {
                name: 'Location',
                property: 'location',
                type: 'text'
            },
            {
                name: 'Gene',
                property: 'gene_name',
                type: 'text'
            },
            {
                name: 'Beginning',
                property: 'beginning',
                type: 'number'
            },
            {
                name: 'Length',
                property: 'length',
                type: 'number'
            },
            {
                name: 'Sense',
                property: 'sense',
                type: 'number'
            },
            {
                name: 'Model',
                property: 'model',
                type: 'text'
            }
        ]
    });

    return ExtendedElement;
});
