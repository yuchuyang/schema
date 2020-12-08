
import xmlschema

my_schema = xmlschema.XMLSchema11('config.xsd')
my_schema.validate('hybrid_rt.xml')
