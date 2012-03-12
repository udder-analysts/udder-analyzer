define([
    'order!jquery',
    'underscore',
    'backbone',
    'text!/public/templates/components/superBar.html',
], function($, _, Backbone, SuperBarTemplate) {
    var SuperBar;

    SuperBar = Backbone.View.extend({
        className: 'superbar',
        template: _.template(SuperBarTemplate),

        events: {
            'focus': 'focus',
            'blur': 'blur',
        },

        initialize: function(options) {
        },

        focus: function() {
            console.log('focus');
        },

        blur: function() {
            console.log('blur');
        },

        render: function() {
            console.log('render bar');
            // If this is the initial render
            if (!this.rendered) {
                this.setElement(this.template());
                this.rendered = true;
            }

            this.delegateEvents();
            return this;
        }
    });

    return SuperBar;
});
