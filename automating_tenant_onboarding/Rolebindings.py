import yaml

class Rolebinding:
    def __init__(self,metadataname,principlename,principletype,role,resourcedic):
        self.metaname = metadataname
        self.principlename = principlename
        self.principletype = principletype
        self.role = role
        self.resourcedic = resourcedic
    
    def creator(self):
        d={"metadaname":self.metaname,"principlename":self.principlename,"principletype":self.principletype,"resources":self.resourcedic,"Role":self.role}
        return d
    
class resourcedic:
    def __init__(self,patterntype,value,resourcetype,clusterid) -> list:
        if (patterntype == "PREFIXED" or patterntype=="LITERAL"):
            self.patterntype= patterntype
        else:
            raise "patterntype is wrong"
        self.value = value
        if clusterid == None :
            if resourcetype in ["Topic", "Group"]:
                self.resourcetype = resourcetype
            else:
                raise "wrong cluster id"
        elif clusterid == "schemaregistry":
            self.resourcetype = "Subject"
        else:
            self.resourcetype = "Connect"

    def diccreator(self) -> list:
        d={"patternType":self.patterntype, "Resourcename":self.value, "Resourcetype":self.resourcetype }
        l = [d]
        return l


lrd=resourcedic("PREFIXED","DMN01-MDL","Topic",None)
controlcenterRole = Rolebinding("c3-role","GG_KAAS_c3_mygroup","Group","DeveloperREad",lrd.diccreator())

f = open("./mycontrolcenterRole.yaml",'w')
f.write(yaml.dump(controlcenterRole.creator()))
f.close()