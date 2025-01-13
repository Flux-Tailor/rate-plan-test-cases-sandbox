#!ve/bin/python
##
## script to process xsl transforms
## Uses SaxonC library https://pypi.org/project/saxonche/, for XSL > v1.0 support 
##

import os
import sys
import argparse
from saxonche import *

# INPUT_XML='../CEI/CED/ELECTRIC/tariffBooks/CED_E_SC1-All/XML/v0.99.7-dev/CEI_CED_E_T002_SC1-All_tariff_books_2024-12-18T1615-5.xml'
# TRANSFORM_XSL='./transform_rate_plan_data_transfers.xsl'

def apply_template(input_xml, transform_xsl):
    """
    From documentation example https://pypi.org/project/saxonche/
    """

    with PySaxonProcessor(license=False) as proc:
        # print(proc.version)
        xsltproc = proc.new_xslt30_processor()
        executable = xsltproc.compile_stylesheet(stylesheet_file=TRANSFORM_XSL)
        executable.set_result_as_raw_value(True)
        executable.set_initial_match_selection(file_name=INPUT_XML)
       
        result = executable.apply_templates_returning_string()
        return result


if __name__ == "__main__":
    """Main function command line script. ./mirror_delta_share.py -h for Usage"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=argparse.FileType('r', encoding='latin-1'),
                        required=True, help="The full path to the xml input file"),
    parser.add_argument("--transform", type=argparse.FileType('r', encoding='latin-1'), 
                        required=True, help="The full path to the xsl transformation file")
    args = parser.parse_args()

    output = apply_template(args.input, args.transform)

    print(output)
