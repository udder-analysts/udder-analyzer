define([
   'underscore',
   'backbone'
], function(_, Backbone) {
    var ElementDetail;

    /* 
     * ElementDetail
     * species - <string> name of species
     * comparison - <string> the comparison
     * experiment
     * beginning
     * model
     * sense
     * match_quality
     * sequence
     * factors
     */
    ElementDetail = Backbone.Model.extend({
        defaults: {
            species: 'unknown',
            comparison: 'unknown', 
            experiment: 'unknown',
            beginning: 'unknown',
            model: 'unknown',
            sense: 'unknown',
            match_quality: 'unknown',
            sequence: 'unknown',
            factors: 'unknown',
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
        type: 'elementDetail',
        displayProperties: {
            'species': 'species',
            'comparison': 'comparison', 
            'experiment': 'experiment,
            'beginning': 'beginning',
            'model': 'model',
            'sense': 'sense',
            'match_quality': 'match_quality',
            'sequence': 'sequence',
            'factors': 'factors'
        }
    });

    return ElementDetail;
});
