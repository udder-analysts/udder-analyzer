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
        },
    },
    // Class Properties
    {
        type: 'element',
        displayProperties: [
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
            },
            {
                name: 'La',
                property: 'la',
                type: 'number'
            },
            {
                name: 'LaSlash',
                property: 'la_slash',
                type: 'number'
            },
            {
                name: 'Lq',
                property: 'lq',
                type: 'number'
            },
            {
                name: 'Ld',
                property: 'ld',
                type: 'number'
            },
            {
                name: 'Lpv',
                property: 'lpv',
                type: 'number'
            }
        ]
    });

    return RegulatoryElement;
});
