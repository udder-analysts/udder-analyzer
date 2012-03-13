define([
    'jquery',
    'underscore',
    'backbone',
    'src/controllers/pages/page',
    'src/controllers/superList',
    'src/controllers/elementDetail',
    'src/collections/extendedFactors',
    'src/collections/extendedElements',
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
           
            console.log(params);

            if (params.element) {
                pane = createDetail(params);
            }
            else if (params.factor) {
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

            function createList(params, Collection) {
                var pane, collection;

                console.log(Collection.type);

                collection = new Collection([], params);
                pane = new SuperList(_.extend(params, { 
                    model: collection
                 }));
                collection.fetch();
                return pane;
            }
        }
    });

    displayProperties = {};
    displayProperties[Factors.type] = [
        {
            name: 'Name',
            property: 'name',
            type: 'text'
        },
        {
            name: 'Models',
            property: 'models',
            type: 'number'
        },
        {
            name: 'Genes',
            property: 'genes',
            type: 'number'
        },
        {
            name: 'Occurences',
            property: 'occurences',
            type: 'number'
        }
    ];
    displayProperties[Elements.type] = [ 
        {
            name: 'Comparison',
            property: 'comparison',
            type: 'text'
        },
        {
            name: 'Experimenter',
            property: 'experimenter',
            type: 'text'
        },
        {
            name: 'Date',
            property: 'dateof',
            type: 'date'
        },
        {
            name: 'Location',
            property: 'location',
            type: 'text'
        },
        {
            name: 'Gene',
            property: 'gene_name',
            type: 'text'
        },
        {
            name: 'Beginning',
            property: 'beginning',
            type: 'number'
        },
        {
            name: 'Length',
            property: 'length',
            type: 'number'
        },
        {
            name: 'Sense',
            property: 'sense',
            type: 'number'
        },
        {
            name: 'Model',
            property: 'model',
            type: 'text'
        }
    ];

    return FactorSearch;
});
