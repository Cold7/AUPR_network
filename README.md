# AUPR_network
usage: Script to compute the Area Under Precision-Recall curve based in a reference and a GENIE3 inferred network.
 [-h] -r REFERENCE -i INFERRED [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -r REFERENCE, --reference REFERENCE
                        Route to the reference network (GML format)
  -i INFERRED, --inferred INFERRED
                        Route to the inferred network (GML format and a edge attribute called score)
  -o OUTPUT, --output OUTPUT
                        Output path to save results
