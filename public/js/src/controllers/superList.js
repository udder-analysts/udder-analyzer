define([
    'order!jquery',
    'underscore',
    'backbone',
    'text!/public/templates/components/superPane.html',
    'text!/public/templates/components/superList.html',
    'order!public/js/lib/jquery.fixedheadertable.js'
], function($, _, Backbone, SuperPaneTemplate, SuperListTemplate) {
    var SuperList;

    SuperList = Backbone.View.extend({
        className: 'pane',
        paneTemplate: _.template(SuperPaneTemplate),
        listTemplate: _.template(SuperListTemplate),

        events: {
            'focus': 'focus',
            'blur': 'blur',
            'click tr': 'select'
        },

        initialize: function(options) {
            this.model.bind('reset', this.render, this);
            
            this.columns = this.model.model.displayProperties;
            this.type = this.model.model.type;
            this.selected = null;
        },

        focus: function() {
            console.log('focus');
        },

        blur: function() {
            console.log('blur');
        },

        select: function(e) {
            var el = $(e.currentTarget), id, params = {};

            // If the header row was clicked do nothing
            // or if the clicked row is already selected.
            if (el.hasClass('header') || el.hasClass('selected')) return false;

            // Otherwise highlight the selected row and notify the page of the
            // selection. This list's model type and selected item's id must be
            // added to the params to be passed to the next pane.
            if (this.selected) this.selected.removeClass('selected');
            el.addClass('selected');
            this.selected = el;

            id = el.attr('data-id');
            params[this.type] = id;

            this.trigger('selected', _.extend(this.options, params), this);
        },

        render: function() {
            // If this is the initial render
            if (!this.rendered) {
                var width = _.keys(this.columns).length * 100;

                // Render the general pane structure so it can be added
                // to the page
                var paneContext = {
                    title: this.type,
                    width: (width < 300) ? 300 : width 
                };

                this.setElement(this.paneTemplate(paneContext));
                this.rendered = true;
            }

            // If the collection has loaded
            if (this.model.length) {
                var listContext = {
                    columns: _.keys(this.columns),
                    properties: _.values(this.columns),
                    models: this.model.models
                };

                this.$('.content').empty();
                this.$('.content').html(this.listTemplate(listContext));

                // init the fixedHeader
                this.$('table').fixedHeaderTable({themeClass: 'supertable'});
            }

            this.delegateEvents();
            return this;
        }
    });

    return SuperList;
});
