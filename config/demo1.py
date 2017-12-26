from ConfigParser import ConfigParser

CONFIGFILE = "python.txt"

config = ConfigParser()

config.read(CONFIGFILE)

print config.get('messages','greeting')

print config.getfloat('numbers','pi')*10**3