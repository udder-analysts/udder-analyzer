define([
   'underscore',
   'backbone'
], function(_, Backbone) {
   var ExtendedGene;

   /* 
    * Gene
    * id <int> The auto-incremented id of the gene
    * name <string> The name of the gene
    * abbreviation <string> The abbreviation of the gene name
    * species <string> The species of the gene
    * chromosome <int> The particular chromosome the gene is found in
    * beginsite <int> the beginning of the sequence
    * endsite <int> the end of the sequence
    */
   ExtendedGene = Backbone.Model.extend({}, {
        type: 'gene',
        displayProperties: [
            {
                name: 'Name',
                property: 'name',
                type: 'text'
            },
            {
                name: 'Abbrev',
                property: 'abbreviation',
                type: 'text'
            },
            {
                name: 'Species',
                property: 'species',
                type: 'text'
            },
            {
                name: 'Comparisons',
                property: 'comparisons',
                type: 'text',
            },
            {
                name: 'Experiments',
                property: 'experiments',
                type: 'text'
            },
            {
                name: 'Chromosome',
                property: 'chromosome',
                type: 'number'
            },
            {
                name: 'Begin Site',
                property: 'beginsite',
                type: 'number'
            },
            {
                name: 'End Site',
                property: 'endsite',
                type: 'number'
            }
        ]
   });

   return ExtendedGene;
});
