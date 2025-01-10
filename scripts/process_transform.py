from saxonche import *

##
## script to process xsl transforms
## Uses SaxonC library https://pypi.org/project/saxonche/, for XSL > v1.0 support 
##

INPUT_XML='../CEI/CED/ELECTRIC/tariffBooks/CED_E_SC1-All/XML/v0.99.7-dev/CEI_CED_E_T002_SC1-All_tariff_books_2024-12-18T1615-5.xml'
TRANSFORM_XSL='./transform_rate_plan_data_transfers.xsl'


with PySaxonProcessor(license=False) as proc:
  """
  From documentation example https://pypi.org/project/saxonche/
  """

  print(proc.version)
  xsltproc = proc.new_xslt30_processor()
  executable = xsltproc.compile_stylesheet(stylesheet_file=TRANSFORM_XSL)
  executable.set_result_as_raw_value(True)
  executable.set_initial_match_selection(file_name=INPUT_XML)
 
  result = executable.apply_templates_returning_string()
  print(result)
    