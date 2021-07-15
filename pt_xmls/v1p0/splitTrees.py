import xml.etree.ElementTree as ET
tree = ET.parse('f_logPtTarg_invPtWgt_BDTG_AWB_Sq_mode15.weights.xml')
root = tree.getroot()
weights= root.find('Weights')

for itree in range(0,len(weights)):
    iweight = weights[itree]
    mydata = ET.tostring(iweight)
    myfile = open("{}.xml".format(itree), "w")
    myfile.write("""<?xml version="1.0"?>\n""")
    myfile.write(mydata)
    myfile.close()
