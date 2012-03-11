define([
    'jquery',
    'underscore',
    'backbone'
], function($, _, Backbone) {
    var elementDetailView;

    elementDetailView = Backbone.View.extend({
        className: 'pane',
        paneTemplate: _.template(SuperPaneTemplate),
        detailTemplate: _.template(ElementDetailTemplate),

        events: {
        },

        initialize: function(options) {
        },

        focus: function() {
            
        },

        blur: function() {
        },

        render: function() {
            if (!this.rendered) {
                this.$el.html(this.paneTemplate(paneContext));
                this.$('.content').html(
                    this.detailTemplate(this.model.toJSON()));
                this.rendered = true;

            }
            
        }
    });

    return elementDetailView;
});
