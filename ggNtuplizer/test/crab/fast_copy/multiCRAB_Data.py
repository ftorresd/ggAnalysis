#!/usr/bin/env python

##############
# Multi CRAB #
##############

import time 

if __name__ == '__main__':
  from CRABAPI.RawCommand import crabCommand

def submit(config):
  res = crabCommand('submit', config = config)

from CRABClient.UserUtilities import config
config = config()

dataset = {
  # 2018 - ABC
  'SingleMuon_Run2018A-17Sep2018-v2_MINIAOD' : '/SingleMuon/Run2018A-17Sep2018-v2/MINIAOD', 
  'SingleMuon_Run2018B-17Sep2018-v1_MINIAOD' : '/SingleMuon/Run2018B-17Sep2018-v1/MINIAOD', 
  'SingleMuon_Run2018C-17Sep2018-v1_MINIAOD' : '/SingleMuon/Run2018C-17Sep2018-v1/MINIAOD', 
  
  # 2016
  'SingleMuon_Run2016H-17Jul2018-v1_MINIAOD' : '/SingleMuon/Run2016H-17Jul2018-v1/MINIAOD',
  'SingleMuon_Run2016G-17Jul2018-v1_MINIAOD' : '/SingleMuon/Run2016G-17Jul2018-v1/MINIAOD',
  'SingleMuon_Run2016F-17Jul2018-v1_MINIAOD' : '/SingleMuon/Run2016F-17Jul2018-v1/MINIAOD',
  'SingleMuon_Run2016E-17Jul2018-v1_MINIAOD' : '/SingleMuon/Run2016E-17Jul2018-v1/MINIAOD',
  'SingleMuon_Run2016D-17Jul2018-v1_MINIAOD' : '/SingleMuon/Run2016D-17Jul2018-v1/MINIAOD',
  'SingleMuon_Run2016C-17Jul2018-v1_MINIAOD' : '/SingleMuon/Run2016C-17Jul2018-v1/MINIAOD',
  'SingleMuon_Run2016B-17Jul2018_ver2-v1_MINIAOD' : '/SingleMuon/Run2016B-17Jul2018_ver2-v1/MINIAOD',
  # 'SingleMuon_Run2016B-17Jul2018_ver1-v1_MINIAOD' : '/SingleMuon/Run2016B-17Jul2018_ver1-v1/MINIAOD',

  # 2017
  'SingleMuon_Run2017F-31Mar2018-v1_MINIAOD' : '/SingleMuon/Run2017F-31Mar2018-v1/MINIAOD',
  'SingleMuon_Run2017E-31Mar2018-v1_MINIAOD' : '/SingleMuon/Run2017E-31Mar2018-v1/MINIAOD',
  'SingleMuon_Run2017D-31Mar2018-v1_MINIAOD' : '/SingleMuon/Run2017D-31Mar2018-v1/MINIAOD',
  'SingleMuon_Run2017C-31Mar2018-v1_MINIAOD' : '/SingleMuon/Run2017C-31Mar2018-v1/MINIAOD',
  'SingleMuon_Run2017B-31Mar2018-v1_MINIAOD' : '/SingleMuon/Run2017B-31Mar2018-v1/MINIAOD',
}




nfiles = -1 
#nfiles = 16 
unitsPerJob = 180

mask_2016 = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_ReReco_07Aug2017_Collisions16_JSON.txt'
mask_2017 = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt'
mask_2018 = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions18/13TeV/ReReco/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt'
mask = mask_2018

#name = 'HLTPhysics_ntuples_L1_V9_v02_UERJ_goodsrunBPH_RUN_ALL_UERJHLT_v24_V01'
#config.General.workArea = 'crab_'+name
config.General.transferLogs = False
config.JobType.allowUndistributedCMSSW = True
config.General.transferOutputs = False
config.JobType.pluginName = 'Analysis'
#config.JobType.psetName = 'hlt_L1_V9_GRun_Data_v02_UERJ_v18.py'
# config.JobType.numCores = 4
#config.JobType.maxMemoryMB = 5000
config.Data.inputDBS = 'global'
config.Data.splitting = 'Automatic'
# config.Data.splitting = 'FileBased'
config.Data.publication = False
config.Site.storageSite = 'T2_BR_UERJ'
config.Data.ignoreLocality = False


#config.Site.whitelist = ['T3_CH_CERN_CAF'] #Required for CAF submission
config.Site.blacklist = ['T2_US_UCSD', 'T2_US_Caltech'] 
# config.Site.whitelist = ['T2_BE_IIHE', 'T2_CH_CERN', 'T2_DE_DESY', 'T2_IN_TIFR', 'T2_US_Wisconsin']
#config.Site.whitelist = ['T3_US_FNALLPC']
#config.Site.ignoreGlobalBlacklist = True
#config.Site.ignoreGlobalBlacklist = False


def doSubmit(listOfSamples):
  for sample in listOfSamples:
    newName = sample+name
    config.General.workArea = 'crab_'+newName
    config.General.requestName = sample
    config.Data.inputDataset = dataset[sample]
    config.Data.unitsPerJob = unitsPerJob
    config.Data.totalUnits = nfiles
    config.Data.outputDatasetTag = sample
    config.Data.lumiMask = mask
    # config.Data.outLFNDirBase = '/store/user/ftorresd/ZtoUpsilonPhoton2016/' + newName # or '/store/group/<subdir>'
    config.Data.outLFNDirBase = '/store/user/ftorresd/HZUpsilonPhotonRun2/buffer_102X_slimmed_fast_copy_v03/' + newName 
    output_file_name = "ggtree_data.root"
    dest_directory = config.Data.outLFNDirBase
    config.JobType.scriptExe = "cmssw_executor.py"
    config.JobType.scriptArgs = ["output_file_name="+output_file_name, "dest_directory="+dest_directory]
    submit(config)



# config.JobType.psetName = '../../run_data2016_102X_slimmed.py'
# config.JobType.psetName = '../../run_data2017_102X_slimmed.py'
config.JobType.psetName = '../../run_data2018_102X_slimmed.py'
# config.JobType.psetName = '../../run_data2018D_102X_slimmed.py'

################################################################################################
# Submit CRAB jobs
################################################################################################

nfiles = -1
unitsPerJob = 180
name = '_ggNtuples_102X_slimmed_v01'

# 2016

# listOfSamples = ['SingleMuon_Run2016H-17Jul2018-v1_MINIAOD']
# doSubmit(listOfSamples)

# listOfSamples = ['SingleMuon_Run2016G-17Jul2018-v1_MINIAOD']
# doSubmit(listOfSamples)

# listOfSamples = ['SingleMuon_Run2016F-17Jul2018-v1_MINIAOD']
# doSubmit(listOfSamples)

# listOfSamples = ['SingleMuon_Run2016E-17Jul2018-v1_MINIAOD']
# doSubmit(listOfSamples)

# listOfSamples = ['SingleMuon_Run2016D-17Jul2018-v1_MINIAOD']
# doSubmit(listOfSamples)

# listOfSamples = ['SingleMuon_Run2016C-17Jul2018-v1_MINIAOD']
# doSubmit(listOfSamples)

# listOfSamples = ['SingleMuon_Run2016B-17Jul2018_ver2-v1_MINIAOD']
# doSubmit(listOfSamples)

#### Not in the Golden JSON!!!
#### listOfSamples = ['SingleMuon_Run2016B-17Jul2018_ver1-v1_MINIAOD']
#### doSubmit(listOfSamples)

# 2017

# listOfSamples = ['SingleMuon_Run2017F-31Mar2018-v1_MINIAOD']
# doSubmit(listOfSamples)

# listOfSamples = ['SingleMuon_Run2017E-31Mar2018-v1_MINIAOD']
# doSubmit(listOfSamples)

# listOfSamples = ['SingleMuon_Run2017D-31Mar2018-v1_MINIAOD']
# doSubmit(listOfSamples)

# listOfSamples = ['SingleMuon_Run2017C-31Mar2018-v1_MINIAOD']
# doSubmit(listOfSamples)

# listOfSamples = ['SingleMuon_Run2017B-31Mar2018-v1_MINIAOD']
# doSubmit(listOfSamples)



# 2018

listOfSamples = ['SingleMuon_Run2018A-17Sep2018-v2_MINIAOD']
doSubmit(listOfSamples)





