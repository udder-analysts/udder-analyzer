define([
   'underscore',
   'backbone'
], function(_, Backbone) {
   var JobParameters;

   /* 
    * JobParameters
    * gene_id <int> the ID of the gene
    * exp_id <int> the ID of the experiment
    * regulation <string>
    * time_len <string>
    * email <string>
    * TRANSFAC_strings <int>
    * my_site_strings <string>
    * selected1 <int>
    * TRANSFAC_matrices <int>
    * IMD_matrices <int>
    * GBIL_gibbsmat_matrices <int>
    * JASPAR_matrices <int>
    * myweight_matrices <string>
    * selected2 <int>
    * combine_with <string>
    * factor_attribute1 <string>
    * matches <string>
    * use_only_core_pos <int>
    * max_allowed_mismatch <int>
    * min_log_likelihood_ratio_score <int>
    * min_string_length <int>
    * min_lg_likelihood_ratio <int>
    * group_selection1 <string>
    * max_lg_likelihood_deficit <int>
    * min_core_similarity <float>
    * min_matrix_similarity <float>
    * second_lg_likelihood_deficit <int>
    * count_sig_threshold <float>
    * selected3 <int>
    * pseudocounts <float>
    * group_selection2 <string>
    * at_content <int>
    * explicit_A_dist <float>
    * explicit_C_dist <float>
    * explicit_G_dist <float>
    * explicit_T_dist <float>
    * handle_ambig_bases <string>
    * tessJob <string>
    */
   JobParameters = Backbone.Model.extend({
      defaults: {
         selected: false
      },

      toggleSelect: function() {
         this.set({ select: !this.get('select') });
      }
       },
    // Class Properties
    {
        type: 'jobParameters',
        displayProperties: {
            'Regulation':'regulation' ,
			'TimeLength': 'time_len' ,
			'Email':'email' ,
			'TRANSFACStrings' : 'TRANSFAC_strings' ,
			'MySiteStrings' : 'my_site_strings' ,
			'Selected1': 'selected1' ,
			'TRANSFACMatrices' : 'TRANSFAC_matrices' ,
			'IMDMatrices' : 'IMD_matrices' ,
			'GBILGibbsmatMatrices':'GBIL_gibbsmat_matrices' ,
			'JASPARMatrices':'JASPAR_matrices' ,
			'MyWeightMatrices' : 'myweight_matrices' ,
			'Selected2': 'selected2' ,
			'CombineWith':'combine_with' ,
			'FactorAttribute1': 'factor_attribute1' ,
			'Matches': 'matches' ,
			'UseOnlyCorePos' : 'use_only_core_pos' ,
			'MaAllowedMismatch':'max_allowed_mismatch' ,
			'MinLogLikelihoodRatioScore': 'min_log_likelihood_ratio_score' ,
			'MinStingength':'min_string_length' ,
			'MinLgLikelihoodRatio': 'min_lg_likelihood_ratio' ,
			'GroupSelection1':'group_selection1' ,
			'MaxLgLikelihoodDeficit': 'max_lg_likelihood_deficit' ,
			'MinCoreSimilarity': 'min_core_similarity',
			'MinMatrixSimilarity': 'min_matrix_similarity',
			'SecondLgLikelihoodDeficit': 'second_lg_likelihood_deficit' ,
			'CountSigThreshold': 'count_sig_threshold',
			'Selected3': 'selected3' ,
			'Pseudocounts': 'pseudocounts' ,
			'GroupSelection2': 'group_selection2' ,
			'AtContent': 'at_content' ,
			'ExplicitAdist': 'explicit_A_dist',
			'ExplicitCdist': 'explicit_C_dist ,
			'ExplicitGdist': 'explicit_G_dist' ,
			'ExplicitTdist': 'explicit_T_dist' ,
			'HandleAmbigBases': 'handle_ambig_bases' ,
			'TESSJob':'tessJob' ,
        }
   });

   return JobParameters;
});
