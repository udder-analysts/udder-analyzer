
import re
from functions import *

#Accepts group of 3 open files for single gene, parses and inserts into DB
def parse_gene_files(hits, param, sequence):
   print 'NOW PARSING FILES'
   
   #Parse Job Parameters.
   selectedCount = 1;
   selectGroups = 1;
   params = {}
   for line in param:
      line = line.rstrip().replace('"', '').replace("'", '')
      m = re.match("Explicit A,C,G,T Distribution\s*,\s*(.*?)\s*,\s*(.*?)\s*,\s*(.*?)\s*,\s*(.*?)\s*$", line)
      if(m) :
         params['adistr'] = m.group(1)
         params['cdistr'] = m.group(2)
         params['gdistr'] = m.group(3)
         params['tdistr'] = m.group(4)
      else :
         m = re.match("\s*(.+?)\s*,\s*(.*?)\s*$", line)
         if (m) :
            key = m.group(1).lower()
            key, selectedCount, selectGroups = interpretKey(key, selectedCount, selectGroups)
            params[key] = m.group(2)
   #Done reading Job Parameters
   
   if params.has_key('experiment') :
      #Break up into experimenter and date
      m = re.match("([\w\s]*)-([\w\s]*)", params['experiment'])
      if m :
         params['experimenter'] = m.group(1)
         params['dateofexp'] = m.group(2)
      else:
         print "Error deciphering experimenter/date"
   else :
      print "Error deciphering experimenter/date"


   #Add species
   insertIntoSpecies(params['species'], '')

   #Get exp ID
   expID = getExperimentID(params['experimenter'], params['comparison'], params['species'], params['dateofexp'])
   if expID < 0: 
      insertIntoExperiment(params['dateofexp'], '', params['experimenter'], params['comparison'], params['species'])
      expID = getExperimentID(params['experimenter'], params['comparison'], params['species'], params['dateofexp'])

      #Make sure expID valid or quit.
      if expID < 0 :
         dbgprint("Invalid experiment")
         return False
   
   #Get Gene ID
   geneID = getGeneID(params['gene name'], params['species'])
   if geneID < 0 :
      insertIntoGenes(params['gene name'], params['gene abbreviation'], params['species'], params['chromosome'], params['begin site'], params['end site'])
      geneID = getGeneID(params['gene name'], params['species'])
      
      #Make sure geneID valid or quit
      if geneID < 0 :
         dbgprint("Invalid Gene")
         return False
 
      #Only parse Sequence if gene needs to be added.
      seq = "";
      for line in sequence:
         if line.lower().find("index") == -1 : #Skip first line
            m = re.match(".*?,.*?,\s*([ACGTNacgtn]+)\s*$", line) #Next line should have ACGT sequence
            if(m) :
               seq = m.group(1) #insert into table
      if seq != "" :
         insertIntoGeneSeq(str(geneID), seq)
      else :
         dbgprint ("Failed to add sequence for gene " + str(geneID) )

   #Add JobParam Data to DB
   insertIntoJobParameters( str(geneID), str(expID), params['regulation'], params['timelen'], params['email'], \
      params['transfacstr'], params['mysitestr'], params['selected1'], params['transfacmat'], \
      params['imdmat'], params['cbilgibbsmat'], params['jasparmat'], params['myweightmat'], params['selected2'], params['combine with'], params['factorattr'], \
      params['matches'], params['usecorepos'], params['strmismatch'], params['minlglikeratscore'], params['minstrlen'], params['minlglikeratio'], params['groupsel1'], \
      params['maxlgdeficit'], params['mincoresim'], params['minmatsim'], params['seclgdeficit'], params['countsigthresh'], params['selected3'], params['pseudocounts'], \
      params['groupsel2'], params['atcontent'], params['adistr'], params['cdistr'], params['gdistr'], params['tdistr'], params['ambigbases'], params['tessjob'] \
   )

   #Parse Hits 1
   for line in hits:
      val = line.count(",");  
      if val == 14 :
         if line.find("Factor") < 0 : #sanity check, skip first line
            fields = line.split(",")
            
            if fields[1].startswith("M") or fields[1].startswith("I") :
               fields[1] = fields[1].split(" (")[0]
            else : #Model starts with R
               fields[1] = fields[1].replace(" ", "").replace("()", "/")
               
            #Convert SNS to bool: 1 for Normal 0 for Reverse
            if fields[3].startswith("N") or fields[3].startswith("n"):
               fields[3] = "1";
            else :
               fields[3] = "0";
            
            #Add Reg Element, get ID regID
            insertIntoRegulatoryElements( fields[2], fields[4], fields[3], fields[1], fields[5], fields[6], fields[7], fields[8], fields[9], fields[10], fields[11], fields[12], fields[13], fields[14], str(geneID), str(expID))
            regID = getRegElementID(fields[2], fields[4], fields[3], fields[1], str(geneID), str(expID))
            if regID < 0 :
               dbgprint("Could not get reg Element ID")
            
            if fields[1].startswith("I") :
               #Ignore Factor "_00000 ", remainder is TFactor
               tfactor = fields[0].replace("_00000 ", "")
               #Add factor (tfactor, regID)
            elif fields[1].startswith("M") or fields[1].startswith("R") :
               numsfacs = fields[0].split()
               for numfac in numsfacs :
                  if numfac.startswith("T") :
                     #Add TNumber
                     insertIntoTnumber(numfac, str(regID))
                  else :
                     #Add TFactor
                     insertIntoTranscriptionFactors(numfac, str(regID))
      else:
         dbgprint("Invalid Line in Hits 1 for gene " + str(geneID) + ". Skipping Line")
   commit()  

 

def dbgprint(outstring) :
   print outstring

def interpretKey (key, selectedCount, selectGroups): 
   output = "";

   if re.match("selected\?", key) : 
      output = "selected" + str(selectedCount)
      selectedCount = selectedCount + 1;
   elif re.match("group selection", key) : 
      output = "groupsel" + str(selectGroups)
      selectGroups = selectGroups + 1
   elif re.match("tess job", key) :
      output = "tessjob";
   elif re.match("length of time to store", key) : 
      output = "timelen";
   elif re.match("search transfac strings", key) : 
      output = "transfacstr";
   elif re.match("search my site strings", key) : 
      output = "mysitestr";
   elif re.match("your email address", key) : 
      output = "email";
   elif re.match("search transfac matrices", key) : 
      output = "transfacmat";
   elif re.match("search imd matrices", key) : 
      output = "imdmat";
   elif re.match("search cbil-gibbsmat matrices", key) : 
      output = "cbilgibbsmat";
   elif re.match("search jaspar matrices", key) : 
      output = "jasparmat";
   elif re.match("search my weight matrices", key) : 
      output = "myweightmat";
   elif re.match("factor attribute 1", key) : 
      output = "factorattr";
   elif re.match("use only core positions", key) : 
      output = "usecorepos";
   elif re.match("maximum allowable string mismatch", key) : 
      output = "strmismatch";
   elif re.match("minimum log-likelihood ratio score", key) : 
      output = "minlglikeratscore";
   elif re.match("minimum string length", key) : 
      output = "minstrlen";
   elif re.match("minimum lg likelihood ratio \(ta\)", key) : 
      output = "minlglikeratio";
   elif re.match("maximum lg-likelihood deficit", key) : 
      output = "maxlgdeficit";
   elif re.match("minimum core similarity", key) : 
      output = "mincoresim";
   elif re.match("minimum matrix similarity", key) : 
      output = "minmatsim";
   elif re.match("secondary lg-likelihood deficit", key) : 
      output = "seclgdeficit";
   elif re.match("count significance threshold", key) : 
      output = "countsigthresh";
   elif re.match("use a-t content", key) : 
      output = "atcontent";
   elif re.match("handle ambiguous bases using", key) : 
      output = "ambigbases";
   else :
      output = key;
   return output, selectedCount, selectGroups
   
if __name__ == '__main__':
   paramFname = "Small/bACTB promoter TESS Job Parameters.csv"
   sequenceFname = "Small/bACTB promoter TESS Sequences.csv"
   hitsFname = "Small/bACTB promoter TESS Hits 1.csv"
   parse_gene_files(hitsFname, paramFname, sequenceFname)
   exit()
