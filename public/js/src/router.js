define([
    'jquery',
    'underscore',
    'backbone',
    'src/controllers/pages/browse',
    'src/controllers/pages/fileUpload',
    'src/controllers/pages/geneSearch',
    'src/controllers/pages/factorSearch'
], function($, _, Backbone, BrowseView, UploadView, GeneSearchView, FactorSearchView) {
    var App;

    App = Backbone.Router.extend({
        routes: {
            '': 'browse',
            'browse': 'browse',
            'upload': 'fileUpload',
            'gene-search': 'geneSearch',
            'factor-search': 'factorSearch'
        },

        initialize: function() {
            // 
        },

        browse: function() {
            // if no browse view
            if (!this.browseView) {
                // init browse view
                this.browseView = new BrowseView();
            }
            // detach current content
            $('#content').contents().detach();
            // render browse view
            $('#content').html(this.browseView.render().el);
        },

        fileUpload: function() {
            // if no upload view
            if (!this.uploadView) {
                // init upload view
                this.uploadView = new UploadView();
            }
            // detach current content
            $('#content').contents().detach();
            // render upload view
            $('#content').html(this.uploadView.render().el);
        },

        geneSearch: function() {
            // if no gene search view
            if (!this.geneSearchView) {
                // init gene search view
                this.geneSearchView = new GeneSearchView();
            }
            // detach current content
            $('#content').contents().detach();
            // render view
            $('#content').html(this.geneSearchView.render().el);
        },

        factorSearch: function() {
            if (!this.factorSearchView) {
                this.factorSearchView = new FactorSearchView();
            }
            $('#content').contents().detach();
            $('#content').html(this.factorSearchView.render().el);
        }
    });

    return App;
});
