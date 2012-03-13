define([
    'order!jquery',
    'underscore',
    'backbone',
    'text!/public/templates/components/geneBar.html',
], function($, _, Backbone, GeneBarTemplate) {
    var GeneBar;

    GeneBar = Backbone.View.extend({
        className: 'superbar',
        template: _.template(GeneBarTemplate),

        events: {
            'focus': 'focus',
            'blur': 'blur',
            'click .btn': 'filter'
        },

        initialize: function(options) {
        },

        focus: function() {
            console.log('focus');
        },

        blur: function() {
            console.log('blur');
        },

        filter: function() {
            var regulation;

            regulation = this.$('.regulation').val();
            this.model.regulation = regulation;
            this.model.fetch();
        },

        render: function() {
            // If this is the initial render
            if (!this.rendered) {
                this.setElement(this.template());
                this.rendered = true;
            }

            this.delegateEvents();
            return this;
        }

    });

    return GeneBar;
});
