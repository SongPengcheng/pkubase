import GstoreConnector

username = "endpoint"
password = "123"
databasename = "pkubase"
sparql = "select ?x ?y where\
                 {\
                     <周杰伦> ?x ?y. \
                 }"
gc =  GstoreConnector.GstoreConnector("pkubase.gstore-pku.com", 80)
print(gc.query(username, password, databasename, sparql))