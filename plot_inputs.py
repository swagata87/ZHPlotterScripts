#!/bin/env python

from DukePlotALot import *
from plotlib import HistStorage,getColorList,getDictValue,HistStorageContainer
import matplotlib.pyplot as plt
from configobj import ConfigObj
try:
    from collections import OrderedDict
except ImportError:
    from ordered import OrderedDict

from rootpy.plotting.views import ScaleView
from rootpy.io import File

def get_binning_from_hist(file_name, hist_name, plot_range, debug=False, min_binning = 1):
    res_file = File(file_name, "read")
    res_hist = res_file.Get(hist_name)
    binning = [plot_range[0]]
    value = plot_range[0]
    while(binning[-1] < plot_range[1]):
        value = res_hist.Eval(binning[-1])
        value *= binning[-1]
        if value < min_binning:
            if debug:
                print('appending %f, last value: %f'%(min_binning,binning[-1]))
            binning.append(binning[-1]+min_binning)
        else:
            if debug:
                print('appending %f, last value: %f'%(round(value),binning[-1]))
            binning.append(binning[-1]+round(value))
    if binning[-1] > plot_range[1]:
        binning[-1] = plot_range[1]
    res_file.Close()
    if debug:
        print(binning)
    return binning

# 
basedir="/home/home1/institut_3a/mukherjee/PhysicsAnalysis/CMSSW_7_4_0/src/TAPAS/PxlAnalyzer/JobTry/BACKGROUND/merged/"
#lumi = 40.8 + 16.3 + 25.028
lumi = 1000
lumisc = float(lumi)/float(1)

xs= ConfigObj("/home/home1/institut_3a/mukherjee/TAPAS/DibosonPlots/xs_13TeV.cfg")
#####bghists=HistStorage(xs,lumi,xstype=None,path=basedir)
bghists=HistStorage(xs,lumi,path=basedir)  

bglist=OrderedDict()

#bglist["DY"]=[
# 'ZToEE_NNPDF30_13TeV_M_50_120_PH-skimid1741',
# 'ZToEE_NNPDF30_13TeV_M_120_200_PH-skimid1736',
# 'ZToEE_NNPDF30_13TeV_M_200_400_PH-skimid1896',
# 'ZToEE_NNPDF30_13TeV_M_400_800_PH-skimid1730',
# 'ZToEE_NNPDF30_13TeV_M_800_1400_PH-skimid1740',
# 'ZToEE_NNPDF30_13TeV_M_1400_2300_PH-skimid1794',
# 'ZToEE_NNPDF30_13TeV_M_3500_4500_PH-skimid1770',
# 'ZToEE_NNPDF30_13TeV_M_6000_Inf_PH-skimid1726',
# 'ZToMuMu_NNPDF30_13TeV_M_50_120_PH-skimid1752',
# 'ZToMuMu_NNPDF30_13TeV_M_200_400_PH-skimid1727',
# 'ZToMuMu_NNPDF30_13TeV_M_400_800_PH-skimid1728',
# 'ZToMuMu_NNPDF30_13TeV_M_800_1400_PH-skimid1837',
# 'ZToMuMu_NNPDF30_13TeV_M_3500_4500_PH-skimid1737',
# 'ZToMuMu_NNPDF30_13TeV_M_4500_6000_PH-skimid1902',
# 'ZToMuMu_NNPDF30_13TeV_M_6000_Inf_PH-skimid1772',
#]
bglist["W"]=[
 'WJetsToLNu_HT-100To200_13TeVMLM_MG-skimid2641',
 'WJetsToLNu_HT-600To800_13TeVMLM_MG-skimid2550',
 'WJetsToLNu_HT-800To1200_13TeVMLM_MG-skimid2621',
 'WJetsToLNu_HT-1200To2500_13TeVMLM_MG-skimid2396',
 'WJetsToLNu_HT-2500ToInf_13TeVMLM_MG-skimid2588',
]
bglist["single Top"]=[
 'ST_t-channel_antitop_4f_leptonDecays_13TeV_PH-skimid2639',
 'ST_t-channel_top_4f_leptonDecays_13TeV_PH-skimid2569',
 'ST_tW_antitop_5f_inclusiveDecays_13TeV_PH-skimid2260',
 'ST_tW_top_5f_inclusiveDecays_13TeV_PH-skimid2554',
]
#bglist["QCD jet"]=[
# 'QCD_Pt-20to30_MuEnrichedPt5_13TeV_P8-skimid1868',
# 'QCD_Pt-80to120_MuEnrichedPt5_13TeV_P8-skimid1805',
# 'QCD_Pt-120to170_MuEnrichedPt5_13TeV_P8-skimid1882',
# 'QCD_Pt-1000toInf_MuEnrichedPt5_13TeV_P8-skimid1930',
#]
bglist["Diboson"]=[
 'WWTo2L2Nu_13TeV_PH-skimid2231',
 'WWTo4Q_13TeV_PH-skimid2602',
 'WWToLNuQQ_13TeV_PH-skimid2209',
 'WZTo3LNu_13TeV_PH-skimid2317',
 'ZZTo2L2Nu_13TeV_PH-skimid2211',
 'ZZTo4L_13TeV_PH-skimid2618',
]
bglist["TTbar"]=[
 ###'TT_13TeV_MCRUN2_74_V9_ext3-v1_PH-skimid2633',
 'TT_Mtt-1000toInf_13TeV_MCRUN2_74_V9_ext1-v2_PH-skimid2247',
]

colorList={}
colorList["W"]="lightblue"
colorList["Diboson"]="darkblue"
colorList["single Top"]="green"
#colorList["QCD jet"]="darkblue"
colorList["TTbar"]="red"
#colorList["WW"]="green"
#colorList["DY"]="pink"
colorList['ZH800']="magenta"
colorList['ZH1200']="darkmagenta"
colorList['ZH1600']="pink"


bghists.additionalWeight = {
# 'ZToEE_NNPDF30_13TeV_M_50_120_PH-skimid1741':lumisc,
# 'ZToEE_NNPDF30_13TeV_M_120_200_PH-skimid1736':lumisc,
  'WWTo2L2Nu_13TeV_PH-skimid2231':lumisc,
  'WWTo4Q_13TeV_PH-skimid2602':lumisc,
  'W WToLNuQQ_13TeV_PH-skimid2209':lumisc,
  'WZTo3LNu_13TeV_PH-skimid2317':lumisc,
  'ZZTo2L2Nu_13TeV_PH-skimid2211':lumisc,
  'ZZTo4L_13TeV_PH-skimid2618':lumisc,
  'TT_13TeV_MCRUN2_74_V9_ext3-v1_PH-skimid2633':lumisc,
  'WJetsToLNu_HT-100To200_13TeVMLM_MG-skimid2641':lumisc,
  'WJetsToLNu_HT-600To800_13TeVMLM_MG-skimid2550':lumisc,
  'WJetsToLNu_HT-800To1200_13TeVMLM_MG-skimid2621':lumisc,
  'WJetsToLNu_HT-1200To2500_13TeVMLM_MG-skimid2396':lumisc,
  'WJetsToLNu_HT-2500ToInf_13TeVMLM_MG-skimid2588':lumisc,
  'ST_t-channel_antitop_4f_leptonDecays_13TeV_PH-skimid2639':lumisc,
  'ST_t-channel_top_4f_leptonDecays_13TeV_PH-skimid2569':lumisc,
  'ST_tW_antitop_5f_inclusiveDecays_13TeV_PH-skimid2260':lumisc,
  'ST_tW_top_5f_inclusiveDecays_13TeV_PH-skimid2554':lumisc,
  'TT_Mtt-1000toInf_13TeV_MCRUN2_74_V9_ext1-v2_PH-skimid2247':lumisc,
# 'TT_13TeV_MCRUN2_74_V9_ext3-v1_PH-skimid1978':lumisc,
# 'TT_Mtt-1000toInf_13TeV_MCRUN2_74_V9_ext1-v2_PH-skimid1749':lumisc,
}

bghists.addFileList(bglist)
#bghists.addFileList("bla1") 

#dat_hist=HistStorage(xs,lumi,path="/home/home1/institut_3a/mukherjee/PhysicsAnalysis/CMSSW_7_4_0/src/TAPAS/PxlAnalyzer/JobTry/",isData=True)
#dat_hist.addFile("bla")
# dat_hist.addFile("Data_Run2015B-PromptReco_251162_252126_SingleMuon-skimid81")
# dat_hist.addFile("Data_Run2015C-PromptReco_253888_254914_SingleMuon-skimid48")
# dat_hist.addFile("../../DATA_25/merged/Data_Run2015C-PromptReco_253888_254914_SingleMuon-skimid48")

basedir="/home/home1/institut_3a/mukherjee/PhysicsAnalysis/CMSSW_7_4_0/src/TAPAS/PxlAnalyzer/JobTry/SIGNAL/merged/"
###sghist=HistStorage(xs,lumi,path=basedir,xstype=None)
sghist=HistStorage(xs,lumi,path=basedir)
sglist=OrderedDict()

sglist['ZH800']=[
 'ZprimeToZhToZlephtata_narrow_M-800_13TeV_MG-skimid1962',
]
sglist['ZH1200']=[
 'ZprimeToZhToZlephtata_narrow_M-1200_13TeV_MG-skimid1944',
]
sglist['ZH1600']=[
 'ZprimeToZhToZlephtata_narrow_M-1600_13TeV_MG-skimid1963',
]

sghist.additionalWeight = {
    'ZprimeToZhToZlephtata_narrow_M-800_13TeV_MG-skimid1962':lumisc,
    'ZprimeToZhToZlephtata_narrow_M-1200_13TeV_MG-skimid1944':lumisc,
    'ZprimeToZhToZlephtata_narrow_M-1600_13TeV_MG-skimid1963':lumisc,
}    
##sghist.additionalWeight.update({'ZprimeToZhToZlephtata_narrow_M-1200_13TeV_MG-skimid1944':lumisc})
#sghist.additionalWeight = {'RPVresonantToEMu_M-500_LLE_LQD-001_13TeV_CA-skimid1827':lumisc}
#sghist.additionalWeight.update({'RPVresonantToEMu_M-1000_LLE_LQD-001_13TeV_CA-skimid1891':lumisc})

sghist.addFileList(sglist)
histContainer=HistStorageContainer(bg=bghists,sg=sghist)

bghists.initStyle(style="bg",colors=colorList)
sghist.initStyle(style="sg",colors=colorList)
