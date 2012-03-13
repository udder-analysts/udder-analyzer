define([
    'order!jquery',
    'underscore',
    'backbone',
    'text!/public/templates/components/superBar.html',
    'src/controllers/elementBar',
    'src/controllers/geneBar'
], function($, _, Backbone, SuperBarTemplate, ElementBar, GeneBar) {
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
            var type, content;

            // If this is the initial render
            if (!this.rendered) {
                this.setElement(this.template());
                this.rendered = true;
            }

            if (this.model && this.model.model && this.model.model.type) {
                type = this.model.model.type;

                if (type == 'element' && !this.elementBar) {
                    this.elementBar = new ElementBar({ model: this.model });
                }

                if (type == 'gene' && !this.geneBar) {
                    this.geneBar = new GeneBar({ model: this.model });
                }

                if (type == 'element') {
                    content = this.elementBar.render().el;
                }
                else if (type == 'gene') {
                    content = this.geneBar.render().el;
                }

                this.$('.content').contents().detach();
                this.$('.content').html(content);
            }
            else {
                this.$('.content').contents().detach();
            }

            this.delegateEvents();
            return this;
        },

    });

    return SuperBar;
});
