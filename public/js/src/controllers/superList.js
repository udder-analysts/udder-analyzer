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
            if (el.hasClass('header')) return false;

            // Otherwise highlight the selected row and notify the page of the
            // selection. This list's model type and selected item's id must be
            // added to the params to be passed to the next pane.
            if (this.selected) this.selected.removeClass('selected');
            el.addClass('selected');
            this.selected = el;

            id = el.attr('data-id');
            params[this.type] = id;

            this.trigger('selected', _.extend(this.options, params));
        },

        render: function() {
            // If this is the initial render
            if (!this.rendered) {
                // Render the general pane structure so it can be added
                // to the page
                var paneContext = {
                    title: this.type,
                };

                this.$el.html(this.paneTemplate(paneContext));
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

                /*
                // render a row for each model, appending to tbody fragment
                this.model.each(this.renderRow, this);
                // add all rows to DOM at once
                */

                // init the fixedHeader
                this.$('table').fixedHeaderTable({themeClass: 'supertable'});
            }

            this.delegateEvents();
            return this;
        },

        renderRow: function(model) {
            var context;
            
            // For each displayable property, add a table cell
            // finally set the data-id attribute to this model's id
            
            this.tablebody.append(
                $('<tr data-id="' + model.id + '"><td>' + model.get('name') + '</td><td>' + model.id + '</td></tr>')
            );
            
            // return row
        }
    });

    return SuperList;
});
