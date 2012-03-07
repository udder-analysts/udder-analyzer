define([
    'jquery',
    'underscore',
    'backbone',
    'text!/public/templates/pages/geneSearch.html'
], function($, _, Backbone, GeneSearchTemplate) {
    var PageController;

    PageController = Backbone.View.extend({
        initialize: function() {
            this.template = _.template(GeneSearchTemplate);
        },

        render: function() {
            this.$el.html(this.template());
            return this;
        }
    });

    return PageController;
});
