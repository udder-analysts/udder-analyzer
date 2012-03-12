define([
    'jquery',
    'underscore',
    'backbone',
    'src/controllers/pages/page',
    'src/controllers/superList',
    'src/controllers/geneDetail',
    'src/collections/genes',
    'src/models/geneDetail'
], function($, _, Backbone, PageView, 
        SuperList, GeneDetailView, Genes, GeneDetail
    ) {
    var GeneSearch;

    GeneSearch = PageView.extend({
        // Determine next pane type based on parameters.
        // Parameters should be passed between panes, with each
        // pane adding a key-value pair of the form type-id.
        getNextPane: function(params) {
            var pane, data;
            params = _.clone(params) || {};
            
            if (params.gene) {
                pane = createDetail(params);
            }
            else {
                pane = createList(params, Genes);
            }

            return pane;

            function createDetail(params) {
                var pane, detail;
                detail = new GeneDetail({ id: params.element });
                pane = new GeneDetailView(_.extend(params, { model: detail }));
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

    return GeneSearch;
});
