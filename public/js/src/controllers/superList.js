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
            'click tr': 'selectItem',
            'click span.column': 'selectColumn',
            'click div.sort': 'sort'
        },

        initialize: function(options) {
            this.model.bind('reset', this.render, this);
            
            this.properties = this.model.model.displayProperties;
            this.type = this.model.model.type;

            this.active = false;
            this.selectedColumn = this.properties[0].property;
            this.sortColumn = this.selectedColumn;
            this.sortAsc = true;
            this.selectedItem = null;
        },

        focus: function() {
            if (!this.active) this.trigger('focus', this);
        },

        blur: function() {
            this.trigger('blur', this);
        },

        activate: function() {
        },

        deactivate: function() {
        },

        // Select a column to be filtered/searched on by the superbar.
        // If the pane is not active, activate it.
        selectColumn: function(e) {
            var prop, type, el = $(e.currentTarget).parent(); 

            prop = el.attr('data-prop');
            type = el.attr('data-type');

            if (this.selectedColumn == prop) return false;

            this.selectedColumn = prop;
            this.trigger('selected:column', this, prop);
        },

        sort: function(e) {
            var prop, sortMod, el = $(e.currentTarget).parent();

            prop = el.attr('data-prop');

            // If the list is already being sorted on this property
            // invert sort order.
            if (this.sortColumn == prop) {
                this.sortAsc = !this.sortAsc;
            }
            // Otherwise reset the sortColumn and sort order.
            else {
                this.sortColumn = prop;
                this.sortAsc = true;
            }

            // Set the collection comparator.
            sortMod = this.sortAsc ? 1 : -1;
            this.model.comparator = function(model1, model2) {
                var prop1 = model1.get(prop),
                    prop2 = model2.get(prop),
                    ret;

                if (typeof prop1 == 'string') prop1 = prop1.toLowerCase();
                if (typeof prop2 == 'string') prop2 = prop2.toLowerCase();

                if (prop1 < prop2) ret = -1;
                else if (prop1 > prop2) ret = 1;
                else ret = 0;

                return ret * sortMod;
            }

            // Set the dirty bit so the list will rerender after sort is done.
            this.model.dirty = true;
            this.model.sort();
        },

        selectItem: function(e) {
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
            // If this is the initial render, render the pane components
            if (!this.rendered) {
                var width = this.properties.length * 110;

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

                // Only rerender the list if the underlying data has changed
                if (this.model.dirty) {
                    var listContext = {
                        properties: this.properties,
                        models: this.model.models
                    };

                    this.$('.content').empty();
                    this.$('.content').html(this.listTemplate(listContext));

                    // init the fixedHeader
                    this.$('table').fixedHeaderTable({themeClass: 'supertable'});

                    // select default column (first column)
                    this.model.dirty = false;
                }
            }
            // Otherwise display a loading indicator
            else {
                //render loading indicator
            }


            var tableHeaders = this.$('th');

            //
            // Render active indicators
            //
            this.$('span', tableHeaders).removeClass('selected');
            if (this.active) {
                this.$('.title').addClass('active');
                this.$('[data-prop=' + this.selectedColumn + '] > span', tableHeaders).addClass('selected');
            }
            else {
                this.$('.title').removeClass('active');
                this.$('[data-prop=' + this.selectedColumn + '] > span', tableHeaders).removeClass('selected');
            }


            //
            // Render sort indicators
            //
            this.$('div', tableHeaders).removeClass('asc desc').addClass('inactive');
            this.$('[data-prop=' + this.sortColumn + '] > div', tableHeaders).addClass( this.sortAsc ? 'asc' : 'desc' );
            

            this.delegateEvents();
            return this;
        }
    });

    return SuperList;
});
