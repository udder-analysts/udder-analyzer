define([
    'jquery',
    'underscore',
    'backbone',
    'text!/public/templates/components/superPane.html',
    'text!/public/templates/components/geneDetail.html'
], function($, _, Backbone, SuperPaneTemplate, GeneDetailTemplate) {
    var GeneDetail;

    GeneDetail = Backbone.View.extend({
        className: 'pane',
        paneTemplate: _.template(SuperPaneTemplate),
        detailTemplate: _.template(GeneDetailTemplate),

        events: {
            'focus': 'focus',
            'blur': 'blur'
        },

        initialize: function(options) { 
            this.model.bind('change', this.render, this);
        },

        focus: function() {
            if (!this.active) this.trigger('focus', this);
        },

        blur: function() {
            this.trigger('blur', this);
        },

        render: function() {
            if (!this.rendered) {

                var paneContext = { 
                    title: 'Gene Detail',
                    width: 300
                };

                this.setElement(this.paneTemplate(paneContext));
                this.rendered = true;
            }

            if (this.model.dirty) {
                this.$('.content').html(
                    this.detailTemplate(this.model.toJSON()));
            }

            if (this.active)
                this.$('.title').addClass('active');
            else
                this.$('.title').removeClass('active');
            
        }
    });

    return GeneDetail;
});
