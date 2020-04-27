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
  # 'HLTPhysics' : '/HLTPhysics/Run2016H-v1/RAW',
  # 'HLTPhysics0' : '/HLTPhysics0/Run2016H-v1/RAW',
  # 'HLTPhysics1' : '/HLTPhysics1/Run2016H-v1/RAW',
  # 'HLTPhysics2' : '/HLTPhysics2/Run2016H-v1/RAW',
  # 'HLTPhysics3' : '/HLTPhysics3/Run2016H-v1/RAW',
  # 'MuonEG' : '/MuonEG/Run2016H-v1/RAW',
  # 'ParkingZeroBias0' : '/ParkingZeroBias0/Run2016H-v1/RAW',
  # 'ParkingZeroBias1' : '/ParkingZeroBias1/Run2016H-v1/RAW',
  # 'ParkingZeroBias2' : '/ParkingZeroBias2/Run2016H-v1/RAW',
  # 'ParkingZeroBias3' : '/ParkingZeroBias3/Run2016H-v1/RAW',
  # 'ParkingZeroBias4' : '/ParkingZeroBias4/Run2016H-v1/RAW',
  # 'ParkingZeroBias5' : '/ParkingZeroBias5/Run2016H-v1/RAW',
  # 'ParkingZeroBias6' : '/ParkingZeroBias6/Run2016H-v1/RAW',
  # 'ParkingZeroBias7' : '/ParkingZeroBias7/Run2016H-v1/RAW',
  # 'HLTPhysics' : '/HLTPhysics/Run2016H-v1/RAW',
  # 'MuonEG_Run2017D-PromptReco-v1_AOD' : '/MuonEG/Run2017D-PromptReco-v1/AOD',
  # 'SingleMuon_Run2017D-PromptReco-v1_AOD' : '/SingleMuon/Run2017D-PromptReco-v1/AOD',
  'ZToUpsilon1SGamma_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV' : '/ZToUpsilon1SGamma-TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM',
  'ZToUpsilon2SGamma_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV' : '/ZToUpsilon2SGamma-TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM',
  'ZToUpsilon3SGamma_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV' : '/ZToUpsilon3SGamma-TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM',
  'ZToJPsiGamma_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV' : '/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',  
  'HToJPsiGamma_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV' : '/HToJPsiG_ToMuMuG_allProdMode_M125_TuneCUETP8M1_13TeV_Pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
  'HToUpsilon1SGamma_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV' : '/HToUpsilon1SG_ToMuMuG_allProdMode_M125_TuneCUETP8M1_13TeV_Pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/MINIAODSIM',
  'HToUpsilon2SGamma_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV' : '/HToUpsilon2SG_ToMuMuG_allProdMode_M125_TuneCUETP8M1_13TeV_Pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/MINIAODSIM',
  'HToUpsilon3SGamma_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV' : '/HToUpsilon3SG_ToMuMuG_allProdMode_M125_TuneCUETP8M1_13TeV_Pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM',
  # 'HiggsDalitz_v14' : '/GluGluHToMuMuG_M125_mll-0To50_Dalitz_13TeV_madgraph_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',
  # 'HiggsDalitz_v14_ext' : '/GluGluHToMuMuG_M125_mll-0To50_Dalitz_13TeV_madgraph_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14_ext1-v1/MINIAODSIM',
  'HiggsDalitz_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV' : '/GluGluHToZG_M-125_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM',
  'ZGTo2MuG_MMuMu-2To15' : '/ZGTo2MuG_MMuMu-2To15_TuneCUETP8M1_13TeV-madgraph-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
  'HDalitzNLO' : '/GluGluHToMuMuG_M125_MLL-0To60_Dalitz_012j_13TeV_amcatnloFXFX_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',


  # Z to Upsilon(1S) + Photon - NLO
  'ZToUpsilon1SGamma_NLO' : '/ZToUpsilon1SGamma_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',

  # Z to Upsilon(2S) + Photon - NLO
  'ZToUpsilon2SGamma_NLO' : '/ZToUpsilon2SGamma_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',

  # Z to Upsilon(3S) + Photon - NLO
  'ZToUpsilon3SGamma_NLO' : '/ZToUpsilon3SGamma_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',

  # Higgs to Upsilon(1S) + Photon - NLO
  'ZH_HToUps1SG_NLO' : '/ZH_HToUps1SG_M125_NNPDF30_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM',
  'WpH_HToUps1SG_NLO' : '/WpH_HToUps1SG_M125_NNPDF30_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM',
  'WmH_HToUps1SG_NLO' : '/WmH_HToUps1SG_M125_NNPDF30_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM',
  'ttH_HToUps1SG_NLO' : '/ttH_HToUps1SG_M125_NNPDF30_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM',
  'VBFH_HToUps1SG_NLO' : '/VBFH_HToUps1SG_M125_NNPDF30_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM',
  'ggH_HToUps1SG_NLO' : '/ggH_HToUps1SG_M125_NNPDF30_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM',

  # Higgs to Upsilon(2S) + Photon - NLO
  'ZH_HToUps2SG_NLO' : '/ZH_HToUps2SG_M125_NNPDF30_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM',
  'WpH_HToUps2SG_NLO' : '/WpH_HToUps2SG_M125_NNPDF30_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM',
  'WmH_HToUps2SG_NLO' : '/WmH_HToUps2SG_M125_NNPDF30_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM',
  'ttH_HToUps2SG_NLO' : '/ttH_HToUps2SG_M125_NNPDF30_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM',
  'VBFH_HToUps2SG_NLO' : '/VBFH_HToUps2SG_M125_NNPDF30_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM',
  'ggH_HToUps2SG_NLO' : '/ggH_HToUps2SG_M125_NNPDF30_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM',

  # Higgs to Upsilon(3S) + Photon - NLO
  'ZH_HToUps3SG_NLO' : '/ZH_HToUps3SG_M125_NNPDF30_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM',
  'WpH_HToUps3SG_NLO' : '/WpH_HToUps3SG_M125_NNPDF30_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM',
  'WmH_HToUps3SG_NLO' : '/WmH_HToUps3SG_M125_NNPDF30_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM',
  'ttH_HToUps3SG_NLO' : '/ttH_HToUps3SG_M125_NNPDF30_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM',
  'VBFH_HToUps3SG_NLO' : '/VBFH_HToUps3SG_M125_NNPDF30_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM',
  'ggH_HToUps3SG_NLO' : '/ggH_HToUps3SG_M125_NNPDF30_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM',

  # Z to Upsilon(1S) + Photon - LO - no Gen Filter
  'ZToUpsilon1SGamma_LO_noGenFilter' : '/ZToUpsilon1SGamma_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',

  # Z to Upsilon(2S) + Photon - LO - no Gen Filter
  'ZToUpsilon2SGamma_LO_noGenFilter' : '/ZToUpsilon2SGamma_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',

  # Z to Upsilon(3S) + Photon - LO - no Gen Filter
  'ZToUpsilon3SGamma_LO_noGenFilter' : '/ZToUpsilon3SGamma_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',

}



nfiles = -1 
#nfiles = 16 
filesPerJob = 1
# mask = '/afs/cern.ch/user/f/ftorresd/trigger2017/EXOTutorial/myHLTTest/CMSSW_8_0_26_patch1/src/myHLT/goodsrun_BPH.json'
# mask = '/afs/cern.ch/user/f/ftorresd/trigger2017/HLT_DATA/CMSSW_9_0_2/src/HLTrigger/HLTanalyzers/test/goodsrun_BPH.json' #HLTPhysics - BPH
# mask = '/afs/cern.ch/user/n/ndaci/public/STEAM/Scripts/columns_2016H/columns_1p35e34.txt' #HLTPhysics - Nadir
# mask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/13TeV/PromptReco/Cert_294927-303825_13TeV_PromptReco_Collisions17_JSON.txt'
mask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/Final/Cert_271036-284044_13TeV_PromptReco_Collisions16_JSON.txt'
# mask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/DCSOnly/json_DCSONLY.txt'
#name = 'HLTPhysics_ntuples_L1_V9_v02_UERJ_goodsrunBPH_RUN_ALL_UERJHLT_v24_V01'
#config.General.workArea = 'crab_'+name
config.General.transferLogs = True
config.General.transferOutputs = True
config.JobType.pluginName = 'Analysis'
#config.JobType.psetName = 'hlt_L1_V9_GRun_Data_v02_UERJ_v18.py'
# config.JobType.numCores = 4
# config.JobType.maxMemoryMB = 5000
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
# config.Data.splitting = 'FileBased'
config.Data.publication = False
# config.Site.storageSite = 'T2_CH_CERN'
config.Site.storageSite = 'T2_CH_CERN'
# config.Data.ignoreLocality = True 


#config.Site.whitelist = ['T3_CH_CERN_CAF'] #Required for CAF submission
#config.Site.whitelist = ['T2_US_Nebraska'] 
# config.Site.whitelist = ['T2_US_*']
#config.Site.whitelist = ['T3_US_FNALLPC']
#config.Site.ignoreGlobalBlacklist = True
#config.Site.ignoreGlobalBlacklist = False

#listOfSamples = ['HLTPhysics','HLTPhysics0','HLTPhysics1','HLTPhysics2','HLTPhysics3']
#listOfSamples = ['MuonEG']
#listOfSamples = ['SingleMuon']
#listOfSamples = ['HLTPhysics']


def doSubmit(listOfSamples):
  for sample in listOfSamples:
    newName = sample+name
    config.General.workArea = 'crab_'+newName
    config.General.requestName = sample
    config.Data.inputDataset = dataset[sample]
    config.Data.unitsPerJob = filesPerJob
    config.Data.totalUnits = nfiles
    config.Data.outputDatasetTag = sample
    config.Data.lumiMask = mask
    # config.Data.outLFNDirBase = '/store/user/ftorresd/HZtoUpsilonPlusPhotonSamples2016/' + newName # or '/store/group/<subdir>'
    config.Data.outLFNDirBase = '/store/user/ftorresd/HZtoUpsilonPlusPhotonSamples2016/MC/' + newName # or '/store/group/<subdir>'
    submit(config)



config.JobType.psetName = 'run_mc_80X.py'
config.JobType.inputFiles   = ['Summer16_23Sep2016V4_MC_L2Relative_AK8PFchs.txt', 'Summer16_23Sep2016V4_MC_L3Absolute_AK8PFchs.txt', 'Summer16_23Sep2016V4_MC.db']
config.JobType.outputFiles = ['ggtree_mc.root'] 


################################################################################################
# Submit CRAB jobs
################################################################################################

# # Z Samples

# # ZToJPsiGamma_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV
# mask = ''
# nfiles = -1 
# filesPerJob = 1
# name = '_ggNtuples_V08_00_26_07_ZtoJPsi_cleanedMu_withOniaHLT_v01'
# listOfSamples = ['ZToJPsiGamma_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV']
# doSubmit(listOfSamples)

# # ZToUpsilon1SGamma_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2_MINIAODSIM
# mask = ''
# nfiles = -1 
# filesPerJob = 1
# name = '_ggNtuples_V08_00_26_07_ZtoUpsilon1S_cleanedMu_withOniaHLT_v01'
# listOfSamples = ['ZToUpsilon1SGamma_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV']
# doSubmit(listOfSamples)


# # ZToUpsilon2SGamma_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2_MINIAODSIM
# mask = ''
# nfiles = -1 
# filesPerJob = 1
# name = '_ggNtuples_V08_00_26_07_ZtoUpsilon2S_cleanedMu_withOniaHLT_v01'
# listOfSamples = ['ZToUpsilon2SGamma_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV']
# doSubmit(listOfSamples)


# # ZToUpsilon3SGamma_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2_MINIAODSIM
# mask = ''
# nfiles = -1 
# filesPerJob = 1
# name = '_ggNtuples_V08_00_26_07_ZtoUpsilon3S_cleanedMu_withOniaHLT_v01'
# listOfSamples = ['ZToUpsilon3SGamma_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV']
# doSubmit(listOfSamples)


# # H Samples

# # HToJPsiGamma_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV
# mask = ''
# nfiles = -1 
# filesPerJob = 1
# name = '_ggNtuples_V08_00_26_07_HtoJPsi_cleanedMu_withOniaHLT_v01'
# listOfSamples = ['HToJPsiGamma_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV']
# doSubmit(listOfSamples)

# # HToUpsilon1SGamma_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV
# mask = ''
# nfiles = -1 
# filesPerJob = 1
# name = '_ggNtuples_V08_00_26_07_HtoUpsilon1S_cleanedMu_withOniaHLT_v01'
# listOfSamples = ['HToUpsilon1SGamma_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV']
# doSubmit(listOfSamples) 


# # HToUpsilon2SGamma_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV
# mask = ''
# nfiles = -1 
# filesPerJob = 1
# name = '_ggNtuples_V08_00_26_07_HtoUpsilon2S_cleanedMu_withOniaHLT_v01'
# listOfSamples = ['HToUpsilon2SGamma_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV']
# doSubmit(listOfSamples)


# # HToUpsilon3SGamma_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV
# mask = ''
# nfiles = -1 
# filesPerJob = 1
# name = '_ggNtuples_V08_00_26_07_HtoUpsilon3S_cleanedMu_withOniaHLT_v01'
# listOfSamples = ['HToUpsilon3SGamma_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV']
# doSubmit(listOfSamples)

# # ZGTo2MuG_MMuMu-2To15
# mask = ''
# nfiles = -1 
# filesPerJob = 1
# name = '_ggNtuples_V08_00_26_07_ZGTo2MuG_MMuMu-2To15_cleanedMu_withOniaHLT_v01'
# listOfSamples = ['ZGTo2MuG_MMuMu-2To15']
# doSubmit(listOfSamples) 

# # H Dalitz

# # HiggsDalitz_v14
# mask = ''
# nfiles = -1 
# filesPerJob = 1
# name = '_ggNtuples_V08_00_26_07_HiggsDalitz_v14_cleanedMu_withOniaHLT_v01'
# listOfSamples = ['HiggsDalitz_v14']
# doSubmit(listOfSamples)

# # HiggsDalitz_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV
# mask = ''
# nfiles = -1 
# filesPerJob = 1
# name = '_ggNtuples_V08_00_26_07_HiggsDalitz_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_cleanedMu_withOniaHLT_v01'
# listOfSamples = ['HiggsDalitz_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV']
# doSubmit(listOfSamples) 

# # HDalitzNLO
# mask = ''
# nfiles = -1 
# filesPerJob = 1
# name = '_ggNtuples_V08_00_26_07_HDalitzNLO_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_cleanedMu_withOniaHLT_v01'
# listOfSamples = ['HDalitzNLO']
# doSubmit(listOfSamples) 


# config.Data.allowNonValidInputDataset = True


# # ZToUpsilon1SGamma_NLO
# mask = ''
# nfiles = -1 
# filesPerJob = 1
# name = '_ggNtuples_V08_00_26_07_Moriond17_80X_2016_TrancheIV_cleanedMu_withOniaHLT_v02'
# listOfSamples = ['ZToUpsilon1SGamma_NLO']
# doSubmit(listOfSamples) 

# # ZToUpsilon2SGamma_NLO
# mask = ''
# nfiles = -1 
# filesPerJob = 1
# name = '_ggNtuples_V08_00_26_07_Moriond17_80X_2016_TrancheIV_cleanedMu_withOniaHLT_v02'
# listOfSamples = ['ZToUpsilon2SGamma_NLO']
# doSubmit(listOfSamples) 

# # ZToUpsilon3SGamma_NLO
# mask = ''
# nfiles = -1 
# filesPerJob = 1
# name = '_ggNtuples_V08_00_26_07_Moriond17_80X_2016_TrancheIV_cleanedMu_withOniaHLT_v02'
# listOfSamples = ['ZToUpsilon3SGamma_NLO']
# doSubmit(listOfSamples) 






# # ZH_HToUps1SG_NLO
# mask = ''
# nfiles = -1 
# filesPerJob = 1
# name = '_ggNtuples_V08_00_26_07_Moriond17_80X_2016_TrancheIV_cleanedMu_withOniaHLT_v02'
# listOfSamples = ['ZH_HToUps1SG_NLO']
# doSubmit(listOfSamples) 


# # WpH_HToUps1SG_NLO
# mask = ''
# nfiles = -1 
# filesPerJob = 1
# name = '_ggNtuples_V08_00_26_07_Moriond17_80X_2016_TrancheIV_cleanedMu_withOniaHLT_v02'
# listOfSamples = ['WpH_HToUps1SG_NLO']
# doSubmit(listOfSamples) 


# # WmH_HToUps1SG_NLO
# mask = ''
# nfiles = -1 
# filesPerJob = 1
# name = '_ggNtuples_V08_00_26_07_Moriond17_80X_2016_TrancheIV_cleanedMu_withOniaHLT_v02'
# listOfSamples = ['WmH_HToUps1SG_NLO']
# doSubmit(listOfSamples) 


# # ttH_HToUps1SG_NLO
# mask = ''
# nfiles = -1 
# filesPerJob = 1
# name = '_ggNtuples_V08_00_26_07_Moriond17_80X_2016_TrancheIV_cleanedMu_withOniaHLT_v02'
# listOfSamples = ['ttH_HToUps1SG_NLO']
# doSubmit(listOfSamples) 

# # VBFH_HToUps1SG_NLO
# mask = ''
# nfiles = -1 
# filesPerJob = 1
# name = '_ggNtuples_V08_00_26_07_Moriond17_80X_2016_TrancheIV_cleanedMu_withOniaHLT_v02'
# listOfSamples = ['VBFH_HToUps1SG_NLO']
# doSubmit(listOfSamples) 

# # ggH_HToUps1SG_NLO
# mask = ''
# nfiles = -1 
# filesPerJob = 1
# name = '_ggNtuples_V08_00_26_07_Moriond17_80X_2016_TrancheIV_cleanedMu_withOniaHLT_v02'
# listOfSamples = ['ggH_HToUps1SG_NLO']
# doSubmit(listOfSamples) 

# # ZH_HToUps2SG_NLO
# mask = ''
# nfiles = -1 
# filesPerJob = 1
# name = '_ggNtuples_V08_00_26_07_Moriond17_80X_2016_TrancheIV_cleanedMu_withOniaHLT_v02'
# listOfSamples = ['ZH_HToUps2SG_NLO']
# doSubmit(listOfSamples) 

# # WpH_HToUps2SG_NLO
# mask = ''
# nfiles = -1 
# filesPerJob = 1
# name = '_ggNtuples_V08_00_26_07_Moriond17_80X_2016_TrancheIV_cleanedMu_withOniaHLT_v02'
# listOfSamples = ['WpH_HToUps2SG_NLO']
# doSubmit(listOfSamples) 

# # WmH_HToUps2SG_NLO
# mask = ''
# nfiles = -1 
# filesPerJob = 1
# name = '_ggNtuples_V08_00_26_07_Moriond17_80X_2016_TrancheIV_cleanedMu_withOniaHLT_v02'
# listOfSamples = ['WmH_HToUps2SG_NLO']
# doSubmit(listOfSamples) 

# # ttH_HToUps2SG_NLO
# mask = ''
# nfiles = -1 
# filesPerJob = 1
# name = '_ggNtuples_V08_00_26_07_Moriond17_80X_2016_TrancheIV_cleanedMu_withOniaHLT_v02'
# listOfSamples = ['ttH_HToUps2SG_NLO']
# doSubmit(listOfSamples) 

# # VBFH_HToUps2SG_NLO
# mask = ''
# nfiles = -1 
# filesPerJob = 1
# name = '_ggNtuples_V08_00_26_07_Moriond17_80X_2016_TrancheIV_cleanedMu_withOniaHLT_v02'
# listOfSamples = ['VBFH_HToUps2SG_NLO']
# doSubmit(listOfSamples) 

# # ggH_HToUps2SG_NLO
# mask = ''
# nfiles = -1 
# filesPerJob = 1
# name = '_ggNtuples_V08_00_26_07_Moriond17_80X_2016_TrancheIV_cleanedMu_withOniaHLT_v02'
# listOfSamples = ['ggH_HToUps2SG_NLO']
# doSubmit(listOfSamples) 

# # ZH_HToUps3SG_NLO
# mask = ''
# nfiles = -1 
# filesPerJob = 1
# name = '_ggNtuples_V08_00_26_07_Moriond17_80X_2016_TrancheIV_cleanedMu_withOniaHLT_v02'
# listOfSamples = ['ZH_HToUps3SG_NLO']
# doSubmit(listOfSamples) 

# # WpH_HToUps3SG_NLO
# mask = ''
# nfiles = -1 
# filesPerJob = 1
# name = '_ggNtuples_V08_00_26_07_Moriond17_80X_2016_TrancheIV_cleanedMu_withOniaHLT_v02'
# listOfSamples = ['WpH_HToUps3SG_NLO']
# doSubmit(listOfSamples) 

# # WmH_HToUps3SG_NLO
# mask = ''
# nfiles = -1 
# filesPerJob = 1
# name = '_ggNtuples_V08_00_26_07_Moriond17_80X_2016_TrancheIV_cleanedMu_withOniaHLT_v02'
# listOfSamples = ['WmH_HToUps3SG_NLO']
# doSubmit(listOfSamples) 

# # ttH_HToUps3SG_NLO
# mask = ''
# nfiles = -1 
# filesPerJob = 1
# name = '_ggNtuples_V08_00_26_07_Moriond17_80X_2016_TrancheIV_cleanedMu_withOniaHLT_v02'
# listOfSamples = ['ttH_HToUps3SG_NLO']
# doSubmit(listOfSamples) 

# # VBFH_HToUps3SG_NLO
# mask = ''
# nfiles = -1 
# filesPerJob = 1
# name = '_ggNtuples_V08_00_26_07_Moriond17_80X_2016_TrancheIV_cleanedMu_withOniaHLT_v02'
# listOfSamples = ['VBFH_HToUps3SG_NLO']
# doSubmit(listOfSamples) 

# # ggH_HToUps3SG_NLO
# mask = ''
# nfiles = -1 
# filesPerJob = 1
# name = '_ggNtuples_V08_00_26_07_Moriond17_80X_2016_TrancheIV_cleanedMu_withOniaHLT_v02'
# listOfSamples = ['ggH_HToUps3SG_NLO']
# doSubmit(listOfSamples) 


#########################################################
## Z - LO - No gen filters
#########################################################


# ZToUpsilon1SGamma_LO_noGenFilter
mask = ''
nfiles = -1 
filesPerJob = 1
name = '_ggNtuples_V08_00_26_07_Moriond17_80X_2016_TrancheIV_cleanedMu_withOniaHLT_v05'
listOfSamples = ['ZToUpsilon1SGamma_LO_noGenFilter']
doSubmit(listOfSamples) 

# ZToUpsilon2SGamma_LO_noGenFilter
mask = ''
nfiles = -1 
filesPerJob = 1
name = '_ggNtuples_V08_00_26_07_Moriond17_80X_2016_TrancheIV_cleanedMu_withOniaHLT_v05'
listOfSamples = ['ZToUpsilon2SGamma_LO_noGenFilter']
doSubmit(listOfSamples) 

# ZToUpsilon3SGamma_LO_noGenFilter
mask = ''
nfiles = -1 
filesPerJob = 1
name = '_ggNtuples_V08_00_26_07_Moriond17_80X_2016_TrancheIV_cleanedMu_withOniaHLT_v05'
listOfSamples = ['ZToUpsilon3SGamma_LO_noGenFilter']
doSubmit(listOfSamples) 


