define([
    'jquery',
    'underscore',
    'backbone',
    'text!/public/templates/pages/fileUpload.html'
], function($, _, Backbone, UploadTemplate) {
    var PageController;

    PageController = Backbone.View.extend({
        initialize: function() {
            this.template = _.template(UploadTemplate);
        },

        render: function() {
            this.$el.html(this.template());
            return this;
        }
    });

    return PageController;
});
