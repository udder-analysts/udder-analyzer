define([
    'jquery',
    'underscore',
    'backbone',
    'text!/public/templates/pages/browse.html',
    'src/controllers/superBar',
    'src/controllers/superList',
    'src/controllers/elementDetail',
    'src/collections/species',
    'src/collections/comparisons',
    'src/collections/experiments',
    'src/collections/genes',
    'src/collections/factors',
    'src/collections/elements',
    'src/models/elementDetail'
], function($, _, Backbone, BrowseTemplate, SuperBar, SuperList, ElementDetailView, 
        Species, Comparisons, Experiments, Genes, Factors, Elements, ElementDetail
    ) {
    var BrowseView;

    BrowseView = Backbone.View.extend({
        initialize: function() {
            this.template = _.template(BrowseTemplate);
            this.paneStack = [];
            this.activePane = null;
        },

        render: function() {
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
            var pane = BrowseView.getNextPane(params);
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
        }
    }, 
    // Class properties
    {
        // Determine next pane type based on parameters.
        // Parameters should be passed between panes, with each
        // pane adding a key-value pair of the form type-id.
        getNextPane: function(params) {
            var pane, data;
            params = _.clone(params) || {};
            
            // if element - element deail
            if (params.element) {
                pane = createDetail(params);
            }
            // if factor - element list
            else if (params.factor) {
                pane = createList(params, Elements);
            }
            // if gene - factor list
            else if (params.gene) {
                pane = createList(params, Factors);
            }
            // if experiment - gene list
            else if (params.experiment) {
                pane = createList(params, Genes);
            }
            // if comparison - experiment list
            else if (params.comparison) {
                pane = createList(params, Experiments);
            }
            // if species - comparison list
            else if (params.species) {
                pane = createList(params, Comparisons);
            }
            // if nothing - species list
            else {
                pane = createList(params, Species);
            }

            return pane;

            function createDetail(params) {
                var pane, detail;
                detail = new ElementDetail({ id: params.element });
                pane = new ElementDetailView(_.extend(params, { model: detail }));
                detail.fetch();
                return pane;
            }

            function createList(params, collectionType) {
                var pane, collection;
                collection = new collectionType([], params);
                pane = new SuperList(_.extend(params, { model: collection }));
                collection.fetch();
                return pane;
            }
        }
    });

    return BrowseView;
});
