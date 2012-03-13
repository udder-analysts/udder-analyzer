define([
    'jquery',
    'underscore',
    'backbone',
    'src/controllers/pages/page',
    'src/controllers/superList',
    'src/controllers/geneDetail',
    'src/collections/extendedGenes',
    'src/collections/extendedExperiments',
    'src/models/geneDetail'
], function($, _, Backbone, PageView, 
        SuperList, GeneDetailView, Genes, Experiments, GeneDetail
    ) {
    var GeneSearch;

    GeneSearch = PageView.extend({
        // Determine next pane type based on parameters.
        // Parameters should be passed between panes, with each
        // pane adding a key-value pair of the form type-id.
        getNextPane: function(params) {
            var pane, data;
            params = _.clone(params) || {};


            if (params.experiment) return false;

            if (params.geneDetail) {
                pane = createList(params, Experiments);
                pane.url = '/experimentsForGene/' + params.gene;
            }
            else if (params.gene) {
                pane = createDetail(params);
            }
            else {
                pane = createList(params, Genes);
            }

            return pane;

            function createDetail(params) {
                var pane, detail;
                detail = new GeneDetail({ id: params.gene });
                pane = new GeneDetailView(_.extend(params, { model: detail }));
                detail.fetch();
                return pane;
            }

            function createList(params, collectionType) {
                var pane, collection;

                console.log(collectionType.type);

                collection = new collectionType([], params);
                pane = new SuperList(_.extend(params, {
                    model: collection
                 }));
                collection.fetch();
                return pane;
            }
        }
    });

    return GeneSearch;
});
