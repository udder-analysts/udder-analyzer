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
            name: 'unknown', 
            abbreviation: 'unknown',
            chromosome: 'unknown',
            begin: 'unknown',
            end: 'unknown',
            sequence: 'unknown',
        },
        dirty: false,

        url: function() {
            return '/geneDetails/' + this.id;
        },

        sync: function(method, model, options) {
            var params;

            params = {
                dataType: 'json'
            };

            this.dirty = true;
            $.ajax(this.url(), _.extend(options, params));
        }
    },
    // Class Properties
    {
        type: 'geneDetail'
    });

    return GeneDetail;
});
