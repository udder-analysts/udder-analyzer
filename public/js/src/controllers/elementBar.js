define([
    'order!jquery',
    'underscore',
    'backbone',
    'text!/public/templates/components/elementBar.html',
], function($, _, Backbone, ElementBarTemplate) {
    var ElementBar;

    ElementBar = Backbone.View.extend({
        className: 'superbar',
        template: _.template(ElementBarTemplate),

        events: {
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
            var sense, senseFrom, senseTo, lval, lvaMin, lvaMax;

            sense = this.$('.sense').val();
            beginMin = this.$('.begin-min').val();
            beginMax = this.$('.begin-max').val();

            lval = this.$('.lval').val();
            lvalMin = this.$('.lval-min').val();
            lvalMax = this.$('.lval-max').val();

            this.model.sense = sense;
            this.model.locFrom = beginMin;
            this.model.locTo = beginMax;
            
            this.model.lval = lval;
            this.model.lvalMin = lvalMin;
            this.model.lvalMax = lvalMax;

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

    return ElementBar;
});
