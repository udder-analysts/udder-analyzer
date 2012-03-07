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
        },

        toggleSelect: function() {
            this.set({ select: !this.get('select') });
        }
    },
    // Class Properties
    {
        type: 'species',
        displayProperties: {
            'Name': 'name',
            'id': 'id'
        }
    });

    return Species;
});
