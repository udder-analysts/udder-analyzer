define([
   'underscore',
   'backbone',
   'src/models/species'
], function(_, Backbone, Species) {
    var SpeciesList;
    /**
     * A list of the model Species
     * that can be sorted by:
     * name
     */
    SpeciesList = Backbone.Collection.extend({
        model: Species,
        url: '/species',
        sortOn: 'name',
        sortOrder: 'asc',

        intialize: function(models, options) {
            this.dirty = false;
        },

        sync: function(method, model, options) {
            var params;

            params = {
                dataType: 'json',
                data: {
                    sortby: this.sortOn,
                    order: this.sortOrder
                }
            };

            this.dirty = true;

            $.ajax(this.url, _.extend(options, params));
        }
    });
   
    return SpeciesList;
});
