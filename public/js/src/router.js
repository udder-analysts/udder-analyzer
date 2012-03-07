define([
    'jquery',
    'underscore',
    'backbone',
    'src/controllers/pages/browse',
    'src/controllers/pages/fileUpload',
    'src/controllers/pages/geneSearch'
], function($, _, Backbone, BrowseView, UploadView, GeneSearchView) {
    var App;

    App = Backbone.Router.extend({
        routes: {
            '': 'browse',
            'browse': 'browse',
            'upload': 'fileUpload',
            'gene-search': 'geneSearch'
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
        }
    });

    return App;
});
