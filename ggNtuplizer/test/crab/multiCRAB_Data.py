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
  'SingleMuon_Run2018A-17Sep2018-v2_MINIAOD' : '/SingleMuon/Run2018A-17Sep2018-v2/MINIAOD', 
  'SingleMuon_Run2018B-17Sep2018-v1_MINIAOD' : '/SingleMuon/Run2018B-17Sep2018-v1/MINIAOD', 
  'SingleMuon_Run2018C-17Sep2018-v1_MINIAOD' : '/SingleMuon/Run2018C-17Sep2018-v1/MINIAOD', 
}


nfiles = -1 
#nfiles = 16 
unitsPerJob = 180

mask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions18/13TeV/ReReco/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt'

#name = 'HLTPhysics_ntuples_L1_V9_v02_UERJ_goodsrunBPH_RUN_ALL_UERJHLT_v24_V01'
#config.General.workArea = 'crab_'+name
config.General.transferLogs = True
config.General.transferOutputs = True
config.JobType.pluginName = 'Analysis'
#config.JobType.psetName = 'hlt_L1_V9_GRun_Data_v02_UERJ_v18.py'
# config.JobType.numCores = 4
config.JobType.maxMemoryMB = 5000
config.Data.inputDBS = 'global'
config.Data.splitting = 'Automatic'
# config.Data.splitting = 'FileBased'
config.Data.publication = False
config.Site.storageSite = 'T2_BR_UERJ'
# config.Site.storageSite = 'T2_CH_CERN'
# config.Site.storageSite = 'T3_US_FNALLPC'

# config.Data.ignoreLocality = False


#config.Site.whitelist = ['T3_CH_CERN_CAF'] #Required for CAF submission
#config.Site.whitelist = ['T2_US_Nebraska'] 
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
    config.Data.outLFNDirBase = '/store/user/ftorresd/HZUpsilonPhotonRun2/buffer_102X_slimmed/' + newName # or '/store/group/<subdir>'
    submit(config)



config.JobType.psetName = '../run_data2018_102X_slimmed.py'
# config.JobType.inputFiles   = ['Summer16_23Sep2016V4_MC_L2Relative_AK8PFchs.txt', 'Summer16_23Sep2016V4_MC_L3Absolute_AK8PFchs.txt', 'Summer16_23Sep2016V4_MC.db']

# config.JobType.inputFiles   = [
#       'Summer16_23Sep2016AllV4_DATA.db',
#       'Summer16_23Sep2016EFV4_DATA_L2Relative_AK8PFchs.txt',
#       'Summer16_23Sep2016HV4_DATA_L2L3Residual_AK8PFchs.txt',
#       'Summer16_23Sep2016BCDV4_DATA_L2L3Residual_AK8PFchs.txt',
#       'Summer16_23Sep2016EFV4_DATA_L3Absolute_AK8PFchs.txt',
#       'Summer16_23Sep2016HV4_DATA_L2Relative_AK8PFchs.txt',
#       'Summer16_23Sep2016BCDV4_DATA_L2Relative_AK8PFchs.txt',
#       'Summer16_23Sep2016GV4_DATA_L2L3Residual_AK8PFchs.txt',
#       'Summer16_23Sep2016HV4_DATA_L3Absolute_AK8PFchs.txt', 
#       'Summer16_23Sep2016BCDV4_DATA_L3Absolute_AK8PFchs.txt',
#       'Summer16_23Sep2016GV4_DATA_L2Relative_AK8PFchs.txt', 
#       'Summer16_23Sep2016EFV4_DATA_L2L3Residual_AK8PFchs.txt',
#       'Summer16_23Sep2016GV4_DATA_L3Absolute_AK8PFchs.txt',
#       ]

config.JobType.outputFiles = ['ggtree_data.root'] 



# SingleMuon_Run2018A-17Sep2018-v2_MINIAOD
nfiles = -1
unitsPerJob = 180
name = '_ggNtuples_10x2X_slimmed'
listOfSamples = ['SingleMuon_Run2018A-17Sep2018-v2_MINIAOD']
doSubmit(listOfSamples)

