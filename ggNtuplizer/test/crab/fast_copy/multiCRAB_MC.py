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
 'DYJetsToLL_M-50_RunIISummer16MiniAODv3_MINIAODSIM' : '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/MINIAODSIM',
 'DYJetsToLL_M-50_RunIIFall17MiniAODv2_MINIAODSIM' : '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
  }



nfiles = -1 
#nfiles = 16 
filesPerJob = 1
mask = ''
config.General.transferLogs = False
config.JobType.allowUndistributedCMSSW = True
config.General.transferOutputs = False
config.JobType.pluginName = 'Analysis'
#config.JobType.psetName = 'hlt_L1_V9_GRun_Data_v02_UERJ_v18.py'
# config.JobType.numCores = 4
# config.JobType.maxMemoryMB = 5000
config.Data.inputDBS = 'global'
config.Data.splitting = 'Automatic'
config.Data.publication = False
config.Site.storageSite = 'T2_BR_UERJ'
config.Data.ignoreLocality = False 


config.Site.blacklist = ['T2_US_UCSD', 'T2_US_Caltech'] 
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
    config.Data.outLFNDirBase = '/store/user/ftorresd/HZUpsilonPhotonRun2/buffer_102X_slimmed_fast_copy_v03/' + newName 
    output_file_name = "ggtree_mc.root"
    dest_directory = config.Data.outLFNDirBase
    config.JobType.scriptExe = "cmssw_executor.py"
    config.JobType.scriptArgs = ["output_file_name="+output_file_name, "dest_directory="+dest_directory]
    submit(config)


# config.JobType.psetName = '../../run_mc2016_102X_slimmed.py'
# config.JobType.psetName = '../../run_mc2017_102X_slimmed.py'
config.JobType.psetName = '../../run_mc2018_102X_slimmed.py'

# config.JobType.outputFiles = ['ggtree_mc.root'] 

################################################################################################
# Submit CRAB jobs
################################################################################################


mask = ''
nfiles = -1 
unitsPerJob = 180
name = '_ggNtuples_102X_slimmed_v01'



listOfSamples = ['DYJetsToLL_M-50_RunIIAutumn18MiniAOD_MINIAODSIM']
doSubmit(listOfSamples)


# listOfSamples = ['DYJetsToLL_M-50_RunIIFall17MiniAODv2_MINIAODSIM']
# doSubmit(listOfSamples)


# config.Data.splitting = 'FileBased' # only for this DY sample
# config.Data.runRange = '' # only for this DY sample
# config.Data.lumiMask  = '' # only for this DY sample
# unitsPerJob = 1
# listOfSamples = ['DYJetsToLL_M-50_RunIISummer16MiniAODv3_MINIAODSIM']
# doSubmit(listOfSamples)




