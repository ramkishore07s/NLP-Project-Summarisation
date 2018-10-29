'''
arg1: [test/train/dev/test-small]
arg2: <Folder of system summaries>
      * File names should be of the format summary.<id>.txt
      * Encoding should be unicode
'''

import sys
from pyrouge import Rouge155

SUB_FOLDER = sys.argv[1]
SYSTEM_FOLDER = sys.argv[2]

r = Rouge155()

r.system_dir = SYSTEM_FOLDER
r.model_dir = 'Dataset/Summaries/' + SUB_FOLDER
r.system_filename_pattern = 'summary.(\d+).txt'
r.model_filename_pattern = 'summary.#ID#.txt'

output = r.convert_and_evaluate()
output_dict = r.output_to_dict(output)

print(output_dict)