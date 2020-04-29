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
 'DYJetsToLL_M-50_RunIIAutumn18MiniAOD_MINIAODSIM' : '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
  }



nfiles = -1 
#nfiles = 16 
filesPerJob = 1
mask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/Final/Cert_271036-284044_13TeV_PromptReco_Collisions16_JSON.txt'
config.General.transferLogs = True
config.JobType.allowUndistributedCMSSW = True
config.General.transferOutputs = True
config.JobType.pluginName = 'Analysis'
#config.JobType.psetName = 'hlt_L1_V9_GRun_Data_v02_UERJ_v18.py'
# config.JobType.numCores = 4
# config.JobType.maxMemoryMB = 5000
config.Data.inputDBS = 'global'
config.Data.splitting = 'Automatic'
config.Data.publication = False
config.Site.storageSite = 'T2_BR_UERJ'
# config.Data.ignoreLocality = True 


#config.Site.whitelist = ['T3_CH_CERN_CAF'] #Required for CAF submission
#config.Site.whitelist = ['T2_US_Nebraska'] 
# config.Site.whitelist = ['T2_US_*']
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
    # config.Data.outLFNDirBase = '/store/user/ftorresd/HZtoUpsilonPlusPhotonSamples2016/' + newName # or '/store/group/<subdir>'
    config.Data.outLFNDirBase = '/store/user/ftorresd/HZUpsilonPhotonRun2/buffer_102X_slimmed/' + newName # or '/store/group/<subdir>'
    submit(config)


config.JobType.psetName = '../run_data2018_102X_slimmed.py'

config.JobType.outputFiles = ['ggtree_mc.root'] 

################################################################################################
# Submit CRAB jobs
################################################################################################


# DYJetsToLL_M-50_RunIIAutumn18MiniAOD_MINIAODSIM
mask = ''
nfiles = -1 
unitsPerJob = 180
name = '_ggNtuples_10x2X_slimmed_v01'
listOfSamples = ['DYJetsToLL_M-50_RunIIAutumn18MiniAOD_MINIAODSIM']
doSubmit(listOfSamples)


