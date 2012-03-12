define([
    'jquery',
    'underscore',
    'backbone',
    'text!/public/templates/pages/panePage.html',
    'src/controllers/superBar',
], function($, _, Backbone, PageTemplate, SuperBar, SuperList) {
    var PageView;

    PageView = Backbone.View.extend({
        initialize: function() {
            this.template = _.template(PageTemplate);
            this.paneStack = [];
            this.activePane = null;
        },

        render: function() {
            if (!this.template) return false;

            if (!this.rendered) {
                this.$el.html(this.template());

                // render bar
                this.bar = new SuperBar();
                this.barContainer = this.$('.bar-container');

                // render initial pane stack
                this.paneContainer = this.$('.pane-container');
                this.addPane({});
                this.rendered = true;
            }

            this.barContainer.empty();
            this.barContainer.html(this.bar.render().el);

            return this;
        },

        modifyStack: function(params, pane) {
            var activeIndex = _.indexOf(this.paneStack, pane);

            for (var i = this.paneStack.length; i > activeIndex + 1; i--) {
                this.paneStack.pop().remove();
            }

            this.addPane(params);
            
        },

        addPane: function(params) {
            var pane = this.getNextPane(params);
            pane.bind('selected', this.modifyStack, this);
            pane.bind('selected:column', this.activatePane, this);
            pane.bind('focus', this.activatePane, this);

            this.paneStack.push(pane);
            this.activatePane(pane);

            // pane is rendered in activatePane.
            this.paneContainer.append(pane.el);
            // ensure focus
            pane.$el.focus();
        },

        activatePane: function(pane){
            if (this.activePane) {
                this.activePane.active = false;
                this.activePane.$el.blur();
                this.activePane.render();
            }

            pane.active = true;
            pane.render();
            pane.$el.focus();

            this.bar.activePane = this.activePane = pane;
        },

        // Determine next pane type based on parameters.
        // Parameters should be passed between panes, with each
        // pane adding a key-value pair of the form type-id.
        getNextPane: function(params) {
        }
    }); 

    return PageView;
});
