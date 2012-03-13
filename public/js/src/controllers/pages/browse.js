define([
    'jquery',
    'underscore',
    'backbone',
    'src/controllers/pages/page',
    'src/controllers/superList',
    'src/controllers/elementDetail',
    'src/controllers/elementBar',
    'src/collections/species',
    'src/collections/comparisons',
    'src/collections/experiments',
    'src/collections/genes',
    'src/collections/factors',
    'src/collections/elements',
    'src/models/elementDetail'
], function($, _, Backbone, PageView, SuperList, ElementDetailView, ElementBar, 
        Species, Comparisons, Experiments, Genes, Factors, Elements, ElementDetail
    ) {
    var BrowseView;

    BrowseView = PageView.extend({
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
