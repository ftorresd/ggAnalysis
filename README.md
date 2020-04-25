#### Current production tag : 
#### Newest tag for testing : 
#### Note that the current head version can be run with CMSSW_10_2_10

##### To work with CMSSW_10_2_10 and head version, you do :

```bash=
cmsrel CMSSW_10_2_10 	
cd CMSSW_10_2_10/src 
cmsenv 
git cms-init 

git cms-merge-topic cms-egamma:EgammaPostRecoTools 
git cms-merge-topic cms-egamma:PhotonIDValueMapSpeedup1029 
git cms-merge-topic cms-egamma:slava77-btvDictFix_10210 
git cms-addpkg EgammaAnalysis/ElectronTools 
rm EgammaAnalysis/ElectronTools/data -rf 
git clone https://github.com/cms-data/EgammaAnalysis-ElectronTools.git EgammaAnalysis/ElectronTools/data 
scram b -j 8 
git cms-merge-topic cms-met:METFixEE2017_949_v2_backport_to_102X 
git clone https://github.com/cmkuo/HiggsAnalysis.git 
git clone -b 102X https://github.com/ftorresd/ggAnalysis.git 
scram b -j 8
```

The above code stores the decision in 64 integer. Each bit represents a decision
for ELECRON ID: 5 IDs (Veto, Loose, Medium, Tight and HEEP) so only 5 bits are imp for us (59 bits of this integer  we are not using so may be we can change that to 16 bit integer later)
Representing that integer in 5 bits: b4 b3 b2 b1 b0
b0: Veto; b1: Loose; b2: Medium; b3: Tight and b4: HEEP
To access the decision for 
(a) veto: eleIDbit[]>>0&1 ---> gives 0 or 1. if 0--> this eID is failed. if 1--> this eID is passed
(b) Loose: eleIDbit[]>>1&1
(c) Medium: eleIDbit[]>>2&1
(d) Tight: eleIDbit[]>>3&1
(e) HEEP: eleIDbit[]>>4&1

for photons it is done the same way: it has 3 IDs
so 3 bits represent the decision
Representing that integer in 3 bits:  b2 b1 b0
b0: Loose; b1: Medium; b2: Tight
To access the decision for 
(a) Loose: phoIDbit[]>>0&1 ---> gives 0 or 1. if 0--> this phoID is failed. if 1--> this phoID is passed
(b) Medium: phoIDbit[]>>1&1
(c) Tight: phoIDbit[]>>2&1

to access the MC status flag with GEN particles 
(a) fromHardProcessFinalState : mcStatusFlag[]>>0&1 ---> gives 0 (no) or 1 (yes). 
(b) isPromptFinalState        : mcStatusFlag[]>>1&1 ---> gives 0 (no) or 1 (yes). 
(c) fromHardProcessBeforeFSR  : mcStatusFlag[]>>2&1 ---> gives 0 (no) or 1 (yes). 

