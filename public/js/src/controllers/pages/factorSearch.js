define([
    'jquery',
    'underscore',
    'backbone',
    'src/controllers/pages/page',
    'src/controllers/superList',
    'src/controllers/elementDetail',
    'src/collections/factors',
    'src/collections/elements',
    'src/models/elementDetail'
], function($, _, Backbone, PageView, SuperList, ElementDetailView, Factors, Elements, ElementDetail) {
    var FactorSearch;

    FactorSearch = PageView.extend({
        // Determine next pane type based on parameters.
        // Parameters should be passed between panes, with each
        // pane adding a key-value pair of the form type-id.
        getNextPane: function(params) {
            var pane, data;
            params = _.clone(params) || {};
            
            if (params.element) {
                pane = createDetail(params);
            }
            if (params.factor) {
                pane = createList(params, Elements);
            }
            else {
                pane = createList(params, Factors);
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

    return FactorSearch;
});
