CREATE TABLE species (
   name VARCHAR(200) NOT NULL,
   PRIMARY KEY (name)
)TYPE=INNODB;

CREATE TABLE experiment (
   id INT NOT NULL AUTO_INCREMENT,
   dateof VARCHAR(30) NOT NULL,
   location VARCHAR(100),
   experimenter VARCHAR(50) NOT NULL,
   comparison VARCHAR(100) NOT NULL,
   species VARCHAR(200) NOT NULL,
   PRIMARY KEY (id),
   FOREIGN KEY (species) REFERENCES species(name),
   UNIQUE (experimenter, comparison, species, dateof)
)TYPE=INNODB;

CREATE TABLE genes (
   id INT NOT NULL AUTO_INCREMENT,
   name VARCHAR(100) NOT NULL,
   abbreviation VARCHAR(10) NOT NULL,
   species VARCHAR(200) NOT NULL,
   chromosome int,
   beginsite int,
   endsite int,
   PRIMARY KEY (id),
   FOREIGN KEY (species) REFERENCES species(name),
   UNIQUE (name, species)
)TYPE=INNODB;

CREATE TABLE gene_sequence (
   id INT NOT NULL, -- DONT AUTO INCREMENT (FOREIGN KEY TO GENES)
   sequence TEXT NOT NULL,
   PRIMARY KEY (id),
   FOREIGN KEY (id) REFERENCES genes(id)
)TYPE=INNODB;

CREATE TABLE job_parameters (
   gene_id INT NOT NULL,
   exp_id INT NOT NULL,
   regulation VARCHAR(10),
   time_len VARCHAR(20),
   email VARCHAR(50),
   TRANSFAC_strings int,
   my_site_strings VARCHAR(50),
   selected1 int,
   TRANSFAC_matrices int,
   IMD_matrices int,
   GBIL_gibbsmat_matrices int,
   JASPAR_matrices int,
   myweight_matrices VARCHAR(20),
   selected2 int,
   combine_with VARCHAR(10),
   factor_attribute1 VARCHAR(30),
   matches VARCHAR(20),
   use_only_core_pos int,
   max_allowed_mismatch int,
   min_log_likelihood_ratio_score int,
   min_string_length int,
   min_lg_likelihood_ratio int,
   group_selection1 VARCHAR(20),
   max_lg_likelihood_deficit int,
   min_core_similarity FLOAT,
   min_matrix_similarity FLOAT,
   second_lg_likelihood_deficit int,
   count_sig_threshold FLOAT,
   selected3 int,
   pseudocounts FLOAT,
   group_selection2 VARCHAR(20),
   at_content int,
   explicit_A_dist FLOAT,
   explicit_C_dist FLOAT,
   explicit_G_dist FLOAT,
   explicit_T_dist FLOAT,
   handle_ambig_bases VARCHAR(20),
   tessJob VARCHAR(50),
   PRIMARY KEY (gene_id, exp_id),
   FOREIGN KEY (gene_id) REFERENCES genes(id),
   FOREIGN KEY (exp_id) REFERENCES experiment(id)
)TYPE=INNODB;

CREATE TABLE regulatory_elements (
   id INT NOT NULL AUTO_INCREMENT,
   beginning INT NOT NULL,
   length INT NOT NULL,
   sense  INT NOT NULL,
   model VARCHAR(100) NOT NULL,
   reg_sequence VARCHAR(200) NOT NULL,
   la FLOAT NOT NULL,
   la_slash FLOAT NOT NULL,
   lq FLOAT NOT NULL,
   ld FLOAT NOT NULL,
   lpv FLOAT NOT NULL,
   sc FLOAT NOT NULL,
   sm FLOAT NOT NULL,
   spv FLOAT NOT NULL,
   ppv FLOAT NOT NULL,
   gene_id INT NOT NULL,
   experiment_id INT NOT NULL,
   PRIMARY KEY (id),
   FOREIGN KEY (gene_id) REFERENCES genes(id),
   FOREIGN KEY (experiment_id) REFERENCES experiment(id),
   UNIQUE (beginning, length, sense, model, gene_id, experiment_id)
)TYPE=INNODB;

CREATE TABLE transcription_factors (
   name VARCHAR(20) NOT NULL,
   reg_element int,
   PRIMARY KEY (name, reg_element),
   FOREIGN KEY (reg_element) REFERENCES regulatory_elements(id)
)TYPE=INNODB;

CREATE TABLE t_number (
   tnumber VARCHAR(20) NOT NULL,
   reg_element int,
   PRIMARY KEY (tnumber, reg_element),
   FOREIGN KEY (reg_element) REFERENCES regulatory_elements(id)
)TYPE=INNODB;
