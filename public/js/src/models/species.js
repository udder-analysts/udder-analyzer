define([
   'underscore',
   'backbone'
], function(_, Backbone) {
    var Species;

    /* 
     * Species
     * name - <string> name of species
     */
    Species = Backbone.Model.extend({
        defaults: {
             name: 'unknown',
            selected: false
        }
    },
    // Class Properties
    {
        type: 'species',
        displayProperties: [
            {
                property: 'name',
                name: 'Name',
                type: 'text'
            }
        ]
    });

    return Species;
});
