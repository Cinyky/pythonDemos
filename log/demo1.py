log = open("logfile.txt","w")

url = "http://www.baidu.com"
print >> log,('Downloading file from URL %s' %url)

print >> log,"File successfully downloaded"


