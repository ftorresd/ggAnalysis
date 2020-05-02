#!/usr/bin/env python

import os
import subprocess
import sys

exitCode = 0
exitMessage = ""
errorType = ""

job_id = sys.argv[1]
output_file_name = sys.argv[2].replace("output_file_name=", "")
dest_directory = sys.argv[3].replace("dest_directory=", "")


print "================= Arguments passed ===================="
print "--> Arguments passed:"
print sys.argv
print "=======================================================\n\n\n"

# Dump PSet.py
print "================= Dump PSet.py starting ===================="
import PSet
print PSet.process.dumpPython()
print "================= Dump PSet.py finished ====================\n\n\n"


# Run CMSSW
print "================= CMSRUN starting ===================="
cmssw_returncode = subprocess.call("cmsRun -j FrameworkJobReport.xml -p PSet.py > cmssw_ouput_fast_copy.txt 2>&1", shell=True)
print "================= CMSRUN output ===================="
with open('cmssw_ouput_fast_copy.txt', 'r') as f:
    print(f.read())
print "CMSSW return code: " + str(cmssw_returncode)
print "================= CMSRUN finished ====================\n\n\n"

if (cmssw_returncode != 0):
  os.system(r"rm -rf " + output_file_name)

# Copy output 
copy_returncode = 0
if not(job_id.startswith("0")):
  output_file_name_new = output_file_name.replace(".root", "_"+str(job_id)+".root")
  print "================= XRDCP starting ===================="
  copy_returncode = subprocess.call(r"xrdcp -p -f "+ output_file_name +r" xroot://xrootd.hepgrid.uerj.br//cms"+ dest_directory + r"/" + output_file_name_new + " > copy_ouput_fast_copy.txt 2>&1", shell=True)
  print "================= XRDCP output ===================="
  with open('copy_ouput_fast_copy.txt', 'r') as f:
    print(f.read())
  print "XRDCP return code: " + str(copy_returncode)
  print "================= XRDCP finished ====================\n\n\n"



print "================= ERROR SETTING starting ===================="
if (cmssw_returncode != 0):
  exitCode = cmssw_returncode
  exitMessage = "CMSSW_ERROR"
  errorType = "CMSSW_ERROR"

if (cmssw_returncode == 0) and (copy_returncode != 0):
  exitCode = copy_returncode
  exitMessage = "COPY_ERROR"
  errorType = "COPY_ERROR"
print "================= ERROR SETTING finished ====================\n\n\n"


# Push the error code to FrameworkJobReport.xml
print "================= PREPARING FrameworkJobReport.xml starting ===================="
if (exitCode != 0):
  FrameworkJobReport_editor = r"""
if [ -e FrameworkJobReport.xml ]
then
    cat << EOF > FrameworkJobReport.xml.tmp
<FrameworkJobReport>
<FrameworkError ExitStatus="__EXIT_CODE__" Type="__ERROR_TYPE__" >
__EXIT_MESSAGE__
</FrameworkError>
EOF
    tail -n+2 FrameworkJobReport.xml >> FrameworkJobReport.xml.tmp
    mv FrameworkJobReport.xml.tmp FrameworkJobReport.xml
else
    cat << EOF > FrameworkJobReport.xml
<FrameworkJobReport>
<FrameworkError ExitStatus="__EXIT_CODE__" Type="__ERROR_TYPE__" >
__EXIT_MESSAGE__
</FrameworkError>
</FrameworkJobReport>
EOF
fi
  """
  FrameworkJobReport_editor.replace("__EXIT_CODE__", str(exitCode))
  FrameworkJobReport_editor.replace("__ERROR_TYPE__", errorType)
  FrameworkJobReport_editor.replace("__EXIT_MESSAGE__", exitMessage)
  with open('FrameworkJobReport_editor.sh', 'w') as f:
    print(f.write(FrameworkJobReport_editor))
  os.system("chmod +x FrameworkJobReport_editor.sh")
  os.system("./FrameworkJobReport_editor.sh")
  with open('FrameworkJobReport.xml', 'r') as f:
    print(f.read())
print "================= PREPARING FrameworkJobReport.xml finished ===================="

# Finish execution
sys.exit(exitCode)



