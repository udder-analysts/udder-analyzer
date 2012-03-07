define([
    'jquery',
    'underscore',
    'backbone',
    'text!/public/templates/pages/browse.html',
    'src/controllers/superList',
    'src/collections/species',
    'src/collections/comparisons',
    'src/collections/experiments',
    'src/collections/genes',
    'src/collections/factors',
    'src/collections/elements'
], function($, _, Backbone, BrowseTemplate, SuperList, 
        Species, Comparisons, Experiments, Genes, Factors, Elements
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
                this.paneContainer = this.$('.pane-container');
                this.addPane({});
                this.rendered = true;
            }

            return this;
        },

        addPane: function(params) {
            var pane = BrowseView.getNextPane(params);
            this.paneStack.push(pane);
            this.activePane = pane;
            this.activePane.bind('selected', this.addPane, this);

            this.paneContainer.append(pane.render().el);
        }
    }, 
    // Class properties
    {
        // Determine next pane type based on parameters.
        // Parameters should be passed between panes, with each
        // pane adding a key-value pair of the form type-id.
        getNextPane: function(params) {
            var pane, data;
            params = params || {};
            
            console.log(params);

            /*
            // if element - element deail
            if (params.element) {
                pane = createList(params, ElementDetail);
            }
            // if factor - element list
            else*/ if (params.factor) {
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
            if (params.species) {
                pane = createList(params, Comparisons);
            }
            // if nothing - species list
            else {
                pane = createList(params, Species);
            }

            return pane;

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
