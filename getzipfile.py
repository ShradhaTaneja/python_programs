from flask import Flask, send_file
import json
import urllib2
import os, time, zipfile


delete = False

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def get_zip():
    resource_url1 = 'https://api.github.com/repos/ShradhaTaneja/python_programs/releases/latest'
    response1 = json.loads(urllib2.urlopen(resource_url1).read())
    zip_url1 = str(response1['zipball_url'])
    zip_file1 = urllib2.urlopen(zip_url1).read()

    dest1 = "/home/shradha/projects/software/trial_**_" + zip_url1.split('/')[-3] + ".zip"

    with open(dest1, "w") as zf:
        zf.write(zip_file1)

    print "---> zip saved to " + dest1

    resource_url2 = 'https://api.github.com/repos/ShradhaTaneja/builder_project/releases/latest'
    response2 = json.loads(urllib2.urlopen(resource_url2).read())
    zip_url2 = str(response2['zipball_url'])
    zip_file2 = urllib2.urlopen(zip_url2).read()

    dest2 = "/home/shradha/projects/software/trial_**_" + zip_url2.split('/')[-3] + ".zip"

    with open(dest2, "w") as zf:
        zf.write(zip_file2)
    #----------------
    resource_url3 = 'https://api.github.com/repos/ShradhaTaneja/patchwork/releases/latest'
    response3 = json.loads(urllib2.urlopen(resource_url3).read())
    zip_url3 = str(response3['zipball_url'])
    zip_file3 = urllib2.urlopen(zip_url3).read()

    dest3 = "/home/shradha/projects/software/trial_**_" + zip_url3.split('/')[-3] + ".zip"

    with open(dest3, "w") as zf:
        zf.write(zip_file3)

    print "---> zip saved to " + dest3

    """
    zf = zipfile.ZipFile('/home/shradha/zipfile_write_compression.zip', mode='w')
    zf.write("software/" + dest2.split('/')[-1])
    zf.write("software/" + dest1.split('/')[-1])
    zf.close()

    return "done"
"""
    #print "---> zip saved to " + dest2
    print "\n ==== "
    os.system("pwd")

    """
    root = '/home/shradha/projects/software/'
    for next_dir, sub_dir, files in os.walk(root):
        for a_file in files:
            zf = zipfile.ZipFile('/home/shradha/ss_software.zip', mode = 'w')
            zf.write(root + a_file)
    """


    os.system("cp -r ~/projects/software/ ./")
    os.system("zip -r /home/shradha/software_update.zip software/")
    os.system("rm -rf ./software/")

    print "----> software zip ready"
    #return "done"
    delete = True
    return send_file('/home/shradha/software_update.zip')

if delete == True:
    print "delete projects/software/*"

if __name__ == '__main__':
    app.run(debug=True)
