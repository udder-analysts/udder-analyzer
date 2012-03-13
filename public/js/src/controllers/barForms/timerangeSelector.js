define([
    'jQuery',
    'underscore',
    'backbone',
    'text!/public/templates/components/rangeSelector.html'
], function($, _, Backbone, RangeSelectorTemplate) {
    var RangeSelector;

    RangeSelector = Backbone.View.extend({
        template: _.template(RangeSelectorTemplate),

        events: {
            'click .btn': 'filter'
        },

        initialize: function() {
        },

        filter: function() {
            this.model.lValue = this.prop;
            this.model.lvalFrom = this.$('min').value();
            this.model.lvalTo = this.$('max').value();

            this.fetch();
        },

        render: function() {
            if (!this.rendered) {
                this.setElement(this.template());
                this.rendered = true;
            }

            this.delegateEvents();
            return this;
        }
    });

    return RangeSelector;
});
