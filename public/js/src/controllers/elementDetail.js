define([
    'jquery',
    'underscore',
    'backbone',
    'text!/public/templates/components/superPane.html',
    'text!/public/templates/components/elementDetail.html'
], function($, _, Backbone, SuperPaneTemplate, ElementDetailTemplate) {
    var ElementDetail;

    ElementDetail = Backbone.View.extend({
        className: 'pane',
        paneTemplate: _.template(SuperPaneTemplate),
        detailTemplate: _.template(ElementDetailTemplate),

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
                    title: 'Element Detail',
                    width: 500
                };

                this.setElement(this.paneTemplate(paneContext));
                this.rendered = true;
            }


            if (this.model.dirty) {
                console.log(this.model.toJSON());

                this.$('.content').html(
                    this.detailTemplate(this.model.toJSON()));
            }

            if (this.active)
                this.$('.title').addClass('active');
            else
                this.$('.title').removeClass('active');
            
        }
    });

    return ElementDetail;
});
