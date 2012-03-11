define([
   'underscore',
   'backbone'
], function(_, Backbone) {
    var GeneDetail;

    /* 
     * GeneDetail
     * species
     * gname
     * abbrev
     * chromosome
     * begin
     * end
     * sequence
     */
    GeneDetail = Backbone.Model.extend({
        defaults: {
            species: 'unknown',
            gname: 'unknown', 
            abbreviation: 'unknown',
            chromosome: 'unknown',
            begin: 'unknown',
            end: 'unknown',
            sequence: 'unknown',
            selected: false
        },

        toggleSelect: function() {
            this.set({ select: !this.get('select') });
        }
    },
    sync: function(method, model, options) {
        var params;

        params = {
            dataType: 'json'
        };

        $.ajax(this.url, _.extend(options, params));
    },   
    // Class Properties
    {
        type: 'geneDetail',
        displayProperties: {
            'species': 'species',
            'gname': 'name', 
            'abbreviation': 'abbreviation,
            'chromosome': 'chromosome',
            'begin': 'begin',
            'end': 'end',
            'sequence': 'sequence'
        }
    });

    return GeneDetail;
});
