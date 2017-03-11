
import sys,os
import traceback
import pandas as pd
from jinja2 import Template

WORK_DIR = os.path.dirname(os.path.abspath(__file__))
html_template_path = os.path.join(WORK_DIR,"template.html")
data_path = os.path.join(WORK_DIR,"data.csv")

with open(html_template_path,'r') as f:
    mytemplate = f.read()
template = Template(mytemplate)

data_list = list(pd.read_csv(data_path).T.to_dict().values())
content = dict(
    column_str='row_jid,use_jid,comment_jid', 
    column_len=3,
    data_list=data_list,
)
with open(os.path.join(WORK_DIR,'report.html'),'w') as f:
    f.write(template.render(**content))
    