#!/usr/bin/env python
'''
Makes a root file containing histograms for later plotting
Author: T.M.Perry UW
'''
import ROOT
from ROOT import TGraph,THStack,TLegend,TCanvas,TFile,TH1F, TPad
from ROOT import TLatex
from ROOT import gROOT,gStyle
from ROOT import *

import aHisto as h #function to make histograms
import cuts as ct  #function which makes cut strings
import histoRange as hr #manages range, lables for plots
import parameters as p

#import scaleqcd as qs

qcdFromData = False 
qcdFromMC = False
qcdFromDsubMC=True

qcdRescale = False
tRescale = False
ttRescale = False
vRescale = False
dRescale = False
sf_qcd = 1.
sf_drell = 1. # 3503.71 / 3.02386400000000000e+07
sf_st = 1. # 22.2    / 9.91118000000000000e+05
sf_ttbar = 1. # 225.    / 6.88773100000000000e+06
sf_wjets = 1. # 37509.  / 5.31329400000000000e+07
sf_vv = 1.

#get parameters (used in cutmaker)
lumi,bNr,btype,jNr,I,F,iso_value,antiIso_value,path,extraName,leafs,drawW,drawZ,drawQCD = p.arams() 

#isolationValue,antiIsoValue,lumi,massTrans,bnr,btype,jnr
CutsMCn,CutsMCi,CutsDatan,CutsDatai,CutsMCnwl,CutsMCiwl,CutsMCnwc,CutsMCiwc,CutsMCnwcc,CutsMCiwcc,CutsMCnwbb,CutsMCiwbb = ct.cutmaker(
 iso_value,antiIso_value,lumi,bNr,btype,jNr
 )

data_filename  = '../data/wMuNuData.root'
t_t_filename   = '../data/T_t.root'
t_s_filename   = '../data/T_s.root'
t_tw_filename  = '../data/T_tW.root'
tb_t_filename  = '../data/Tbar_t.root'
tb_s_filename  = '../data/Tbar_s.root'
tb_tw_filename = '../data/Tbar_tW.root'
ttb_filename   = '../data/TTbar.root'
ww_filename    = '../data/WW.root'
wz_filename    = '../data/WZ.root'
zz_filename    = '../data/ZZ.root'
wn_filename    = '../data/WJets.root'
w1_filename    = '../data/W1Jet.root'
w2_filename    = '../data/W2Jet.root'
w3_filename    = '../data/W3Jet.root'
w4_filename    = '../data/W4Jet.root'
z_filename     = '../data/Drell.root'

data_file  = TFile( data_filename )
t_t_file   = TFile( t_t_filename  )
t_s_file   = TFile( t_s_filename  )
t_tw_file  = TFile( t_tw_filename )
tb_t_file  = TFile( tb_t_filename )
tb_s_file  = TFile( tb_s_filename )
tb_tw_file = TFile( tb_tw_filename)
ttb_file   = TFile( ttb_filename  )
ww_file    = TFile( ww_filename   )
wz_file    = TFile( wz_filename   )
zz_file    = TFile( zz_filename   )
wn_file    = TFile( wn_filename   )
w1_file    = TFile( w1_filename   )
w2_file    = TFile( w2_filename   )
w3_file    = TFile( w3_filename   )
w4_file    = TFile( w4_filename   )
z_file     = TFile( z_filename    )

eventTreeLocation = 'muNuEventTree/eventTree'

data_tree  =  data_file.Get(eventTreeLocation) 
t_t_tree   =  t_t_file.Get(eventTreeLocation)
t_s_tree   =  t_s_file.Get(eventTreeLocation)
t_tw_tree  =  t_tw_file.Get(eventTreeLocation)
tb_t_tree  =  tb_t_file.Get(eventTreeLocation)
tb_s_tree  =  tb_s_file.Get(eventTreeLocation)
tb_tw_tree =  tb_tw_file.Get(eventTreeLocation)
ttb_tree   =  ttb_file.Get(eventTreeLocation)
ww_tree    =  ww_file.Get(eventTreeLocation)
wz_tree    =  wz_file.Get(eventTreeLocation)
zz_tree    =  zz_file.Get(eventTreeLocation)
wn_tree    =  wn_file.Get(eventTreeLocation)
w1_tree    =  w1_file.Get(eventTreeLocation)
w2_tree    =  w2_file.Get(eventTreeLocation)
w3_tree    =  w3_file.Get(eventTreeLocation)
w4_tree    =  w4_file.Get(eventTreeLocation)
z_tree     =  z_file.Get(eventTreeLocation)

#Start the Plotting Program
for leaf in leafs:

 steps, xmin, xmax, xtitle, xunits, setLogY = hr.ranger(leaf)
 
 outFile=gROOT.FindObject(path+leaf+extraName+'.root')
 if outFile : outFile.Close()
 outFile = TFile(path+leaf+extraName+'.root','RECREATE','Demo ROOT file')
 
 log = open(path+leaf+extraName+'.log','w')
 
 print('----------------------------')
 print('      --'+leaf+'--')
 print(extraName)
 print('----------------------------')
 
 ###
 datanh,datanhSize,datanhSizePart = h.gram(data_tree,leaf,xmin,xmax,steps,CutsDatan,I,F)
 print('For QCD Shape')
 print('data nonIso')
 datanh.SetName('datanh')
 print('  '+str(datanhSize))
 print('  '+str(datanhSizePart))
####  Drell
 print('  z nonIso')
 znh,znhSize,znhSizePart = h.gram(z_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
 znh.SetName('znh')
 znh.Scale(sf_drell)
 print('    '+str(znhSize))
 print('    '+str(znhSizePart))
####  Dibosons
 print('  ww nonIso')
 wwnh,wwnhSize,wwnhSizePart = h.gram(ww_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
 wwnh.SetName('wwnh')
 wwnh.Scale(sf_vv)
 print('    '+str(wwnhSize))
 print('    '+str(wwnhSizePart))
 ###
 print('  wz nonIso')
 wznh,wznhSize,wznhSizePart = h.gram(wz_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
 wznh.SetName('wznh')
 wznh.Scale(sf_vv)
 print('    '+str(wznhSize))
 print('    '+str(wznhSizePart))
 ###
 print('  ww nonIso')
 zznh,zznhSize,zznhSizePart = h.gram(zz_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
 zznh.SetName('zznh')
 zznh.Scale(sf_vv)
 print('    '+str(zznhSize))
 print('    '+str(zznhSizePart))
####  Single Top
 print('  t t nonIso')
 t_tnh,t_tnhSize,t_tnhSizePart = h.gram(t_t_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
 t_tnh.SetName('t_tnh')
 t_tnh.Scale(sf_st)
 print('    '+str(t_tnhSize))
 print('    '+str(t_tnhSizePart))
 ###
 print('  tb t nonIso')
 tb_tnh,tb_tnhSize,tb_tnhSizePart = h.gram(tb_t_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
 tb_tnh.SetName('tb_tnh')
 tb_tnh.Scale(sf_st)
 print('    '+str(tb_tnhSize))
 print('    '+str(tb_tnhSizePart))
 ###
 print('  t s nonIso')
 t_snh,t_snhSize,t_snhSizePart = h.gram(t_s_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
 t_snh.SetName('t_snh')
 t_snh.Scale(sf_st)
 print('    '+str(t_snhSize))
 print('    '+str(t_snhSizePart))
 ###
 print('  tb s nonIso')
 tb_snh,tb_snhSize,tb_snhSizePart = h.gram(tb_s_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
 tb_snh.SetName('tb_snh')
 tb_snh.Scale(sf_st)
 print('    '+str(tb_snhSize))
 print('    '+str(tb_snhSizePart))
 ###
 print('  t tw nonIso')
 t_twnh,t_twnhSize,t_twnhSizePart = h.gram(t_tw_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
 t_twnh.SetName('t_twnh')
 t_twnh.Scale(sf_st)
 print('    '+str(t_twnhSize))
 print('    '+str(t_twnhSizePart))
 ###
 print('  tb tw nonIso')
 tb_twnh,tb_twnhSize,tb_twnhSizePart = h.gram(tb_tw_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
 tb_twnh.SetName('tb_twnh')
 tb_twnh.Scale(sf_st)
 print('    '+str(tb_twnhSize))
 print('    '+str(tb_twnhSizePart))
####  TTbar
 print('  ttbar nonIso')
 ttbnh,ttbnhSize,ttbnhSizePart = h.gram(ttb_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
 ttbnh.SetName('ttbnh')
 ttbnh.Scale(sf_ttbar)
 print('    '+str(ttbnhSize))
 print('    '+str(ttbnhSizePart))
####  W
 print('  wn nonIso')
 wnnh,wnnhSize,wnnhSizePart = h.gram(wn_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
 wnnh.SetName('wnnh')
 wnnh.Scale(sf_wjets)
 print('    '+str(wnnhSize))
 print('    '+str(wnnhSizePart))
 print('  w1 nonIso')
 ###
 w1nh,w1nhSize,w1nhSizePart = h.gram(w1_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
 w1nh.SetName('w1nh')
 w1nh.Scale(sf_wjets)
 print('    '+str(w1nhSize))
 print('    '+str(w1nhSizePart))
 print('  w2 nonIso')
 ###
 w2nh,w2nhSize,w2nhSizePart = h.gram(w2_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
 w2nh.SetName('w2nh')
 w2nh.Scale(sf_wjets)
 print('    '+str(w2nhSize))
 print('    '+str(w2nhSizePart))
 print('  w3 nonIso')
 ###
 w3nh,w3nhSize,w3nhSizePart = h.gram(w3_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
 w3nh.SetName('w3nh')
 w3nh.Scale(sf_wjets)
 print('    '+str(w3nhSize))
 print('    '+str(w3nhSizePart))
 print('  w4 nonIso')
 ###
 w4nh,w4nhSize,w4nhSizePart = h.gram(w4_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
 w4nh.SetName('w4nh')
 w4nh.Scale(sf_wjets)
 print('    '+str(w4nhSize))
 print('    '+str(w4nhSizePart))
#
 print('subtracting non-iso MC from Data ')
 qh = datanh.Clone()
 qh.SetName('qh')
 qh.Add(znh,-1)    #Drell
 qh.Add(t_tnh,-1)  #Single Top
 qh.Add(tb_tnh,-1)
 qh.Add(t_snh,-1)
 qh.Add(tb_snh,-1)
 qh.Add(t_twnh,-1)
 qh.Add(tb_twnh,-1)
 qh.Add(wwnh,-1)   #Diboson
 qh.Add(wznh,-1)
 qh.Add(zznh,-1)
 qh.Add(ttbnh,-1)  #TTbar
 qh.Add(wnnh,-1)   #W
 qh.Add(w1nh,-1)
 qh.Add(w2nh,-1)
 qh.Add(w3nh,-1)
 qh.Add(w4nh,-1)

 print('qcd')
 qh.SetTitle('')
 bminq = qh.GetXaxis().FindBin(xmin)
 bmaxq = qh.GetXaxis().FindBin(xmax)
 bIq = qh.GetXaxis().FindBin(I)
 bFq = qh.GetXaxis().FindBin(F)
 qhSizePart = qh.Integral(bIq,bFq)
 qh.Scale(sf_qcd)
 qhSize = qh.Integral(bminq,bmaxq)
 print('  '+str(qhSize))
 print('  '+str(qhSizePart))
 ####################################
 ### Data
 print('')
 print('Isolated Variables Now')
 print("data Iso") 
 dataih,dataihSize,dataihSizePart = h.gram(data_tree,leaf,xmin,xmax,steps,CutsDatai,I,F)
 dataih.SetName('dataih')
 print('  '+str(dataihSize))
 print('  '+str(dataihSizePart))
 dimax = dataih.GetMaximum()
#### Drell
 print("z Iso")
 zih,zihSize,zihSizePart = h.gram(z_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 zih.SetName('zih')
 zih.Scale(sf_drell)
 print('  '+str(zihSize))
 print('  '+str(zihSizePart))
#### Diboson
 print("ww Iso")
 wwih,wwihSize,wwihSizePart = h.gram(ww_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 wwih.SetName('wwih')
 wwih.Scale(sf_vv)
 print('  '+str(wwihSize))
 print('  '+str(wwihSizePart))
 ###
 print("wz Iso")
 wzih,wzihSize,wzihSizePart = h.gram(wz_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 wzih.SetName('wzih')
 wzih.Scale(sf_vv)
 print('  '+str(wzihSize))
 print('  '+str(wzihSizePart))
 ###
 print("zz Iso")
 zzih,zzihSize,zzihSizePart = h.gram(zz_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 zzih.SetName('zzih')
 zzih.Scale(sf_vv)
 print('  '+str(zzihSize))
 print('  '+str(zzihSizePart))
#### Single Top
 print('t t Iso')
 t_tih,t_tihSize,t_tihSizePart = h.gram(t_t_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 t_tih.SetName('t_tih')
 t_tih.Scale(sf_st)
 print('  '+str(t_tihSize))
 print('  '+str(t_tihSizePart))
 ###
 print('tb t Iso')
 tb_tih,tb_tihSize,tb_tihSizePart = h.gram(tb_t_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 tb_tih.SetName('tb_tih')
 tb_tih.Scale(sf_st)
 print('  '+str(tb_tihSize))
 print('  '+str(tb_tihSizePart))
 ###
 print('t s Iso')
 t_sih,t_sihSize,t_sihSizePart = h.gram(t_s_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 t_sih.SetName('t_sih')
 t_sih.Scale(sf_st)
 print('  '+str(t_sihSize))
 print('  '+str(t_sihSizePart))
 ###
 print('tb s Iso')
 tb_sih,tb_sihSize,tb_sihSizePart = h.gram(tb_s_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 tb_sih.SetName('tb_sih')
 tb_sih.Scale(sf_st)
 print('  '+str(tb_sihSize))
 print('  '+str(tb_sihSizePart))
 ###
 print('t tw Iso')
 t_twih,t_twihSize,t_twihSizePart = h.gram(t_tw_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 t_twih.SetName('t_twih')
 t_twih.Scale(sf_st)
 print('  '+str(t_twihSize))
 print('  '+str(t_twihSizePart))
 ###
 print('tb tw Iso')
 tb_twih,tb_twihSize,tb_twihSizePart = h.gram(tb_tw_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 tb_twih.SetName('tb_twih')
 tb_twih.Scale(sf_st)
 print('  '+str(tb_twihSize))
 print('  '+str(tb_twihSizePart))
#### TTbar
 print('ttb Iso')
 ttbih,ttbihSize,ttbihSizePart = h.gram(ttb_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 ttbih.SetName('ttbih')
 ttbih.Scale(sf_ttbar)
 print('  '+str(ttbihSize))
 print('  '+str(ttbihSizePart))
#### W + Jets
 print('wl n Iso')
 wlnih,wlnihSize,wlnihSizePart = h.gram(wn_tree,leaf,xmin,xmax,steps,CutsMCiwl,I,F)
 wlnih.SetName('wlnih')
 wlnih.Scale(sf_wjets)
 print('  '+str(wlnihSize))
 print('  '+str(wlnihSizePart))
 ####
 print('wc n Iso')
 wcnih,wcnihSize,wcnihSizePart = h.gram(wn_tree,leaf,xmin,xmax,steps,CutsMCiwc,I,F)
 wcnih.SetName('wcnih')
 wcnih.Scale(sf_wjets)
 print('  '+str(wcnihSize))
 print('  '+str(wcnihSizePart))
 ####
 print('wcc n Iso')
 wccnih,wccnihSize,wccnihSizePart = h.gram(wn_tree,leaf,xmin,xmax,steps,CutsMCiwcc,I,F)
 wccnih.SetName('wccnih')
 wccnih.Scale(sf_wjets)
 print('  '+str(wccnihSize))
 print('  '+str(wccnihSizePart))
 ####
 print('wbb n Iso')
 wbbnih,wbbnihSize,wbbnihSizePart = h.gram(wn_tree,leaf,xmin,xmax,steps,CutsMCiwbb,I,F)
 wbbnih.SetName('wbbnih')
 wbbnih.Scale(sf_wjets)
 print('  '+str(wbbnihSize))
 print('  '+str(wbbnihSizePart))
#####
 print('wl 1 Iso')
 wl1ih,wl1ihSize,wl1ihSizePart = h.gram(w1_tree,leaf,xmin,xmax,steps,CutsMCiwl,I,F)
 wl1ih.SetName('wl1ih')
 wl1ih.Scale(sf_wjets)
 print('  '+str(wl1ihSize))
 print('  '+str(wl1ihSizePart))
 ####
 print('wc 1 Iso')
 wc1ih,wc1ihSize,wc1ihSizePart = h.gram(w1_tree,leaf,xmin,xmax,steps,CutsMCiwc,I,F)
 wc1ih.SetName('wc1ih')
 wc1ih.Scale(sf_wjets)
 print('  '+str(wc1ihSize))
 print('  '+str(wc1ihSizePart))
 ####
 print('wcc 1 Iso')
 wcc1ih,wcc1ihSize,wcc1ihSizePart = h.gram(w1_tree,leaf,xmin,xmax,steps,CutsMCiwcc,I,F)
 wcc1ih.SetName('wcc1ih')
 wcc1ih.Scale(sf_wjets)
 print('  '+str(wcc1ihSize))
 print('  '+str(wcc1ihSizePart))
 ####
 print('wbb 1 Iso')
 wbb1ih,wbb1ihSize,wbb1ihSizePart = h.gram(w1_tree,leaf,xmin,xmax,steps,CutsMCiwbb,I,F)
 wbb1ih.SetName('wbb1ih')
 wbb1ih.Scale(sf_wjets)
 print('  '+str(wbb1ihSize))
 print('  '+str(wbb1ihSizePart))
#####
 print('wl 2 Iso')
 wl2ih,wl2ihSize,wl2ihSizePart = h.gram(w2_tree,leaf,xmin,xmax,steps,CutsMCiwl,I,F)
 wl2ih.SetName('wl2ih')
 wl2ih.Scale(sf_wjets)
 print('  '+str(wl2ihSize))
 print('  '+str(wl2ihSizePart))
 ####
 print('wc 2 Iso')
 wc2ih,wc2ihSize,wc2ihSizePart = h.gram(w2_tree,leaf,xmin,xmax,steps,CutsMCiwc,I,F)
 wc2ih.SetName('wc2ih')
 wc2ih.Scale(sf_wjets)
 print('  '+str(wc2ihSize))
 print('  '+str(wc2ihSizePart))
 ####
 print('wcc 2 Iso')
 wcc2ih,wcc2ihSize,wcc2ihSizePart = h.gram(w2_tree,leaf,xmin,xmax,steps,CutsMCiwcc,I,F)
 wcc2ih.SetName('wcc2ih')
 wcc2ih.Scale(sf_wjets)
 print('  '+str(wcc2ihSize))
 print('  '+str(wcc2ihSizePart))
 ####
 print('wbb 2 Iso')
 wbb2ih,wbb2ihSize,wbb2ihSizePart = h.gram(w2_tree,leaf,xmin,xmax,steps,CutsMCiwbb,I,F)
 wbb2ih.SetName('wbb2ih')
 wbb2ih.Scale(sf_wjets)
 print('  '+str(wbb2ihSize))
 print('  '+str(wbb2ihSizePart))
#####
 print('wl 3 Iso')
 wl3ih,wl3ihSize,wl3ihSizePart = h.gram(w3_tree,leaf,xmin,xmax,steps,CutsMCiwl,I,F)
 wl3ih.SetName('wl3ih')
 wl3ih.Scale(sf_wjets)
 print('  '+str(wl3ihSize))
 print('  '+str(wl3ihSizePart))
 ####
 print('wc 3 Iso')
 wc3ih,wc3ihSize,wc3ihSizePart = h.gram(w3_tree,leaf,xmin,xmax,steps,CutsMCiwc,I,F)
 wc3ih.SetName('wc3ih')
 wc3ih.Scale(sf_wjets)
 print('  '+str(wc3ihSize))
 print('  '+str(wc3ihSizePart))
 ####
 print('wcc 3 Iso')
 wcc3ih,wcc3ihSize,wcc3ihSizePart = h.gram(w3_tree,leaf,xmin,xmax,steps,CutsMCiwcc,I,F)
 wcc3ih.SetName('wcc3ih')
 wcc3ih.Scale(sf_wjets)
 print('  '+str(wcc3ihSize))
 print('  '+str(wcc3ihSizePart))
 ####
 print('wbb 3 Iso')
 wbb3ih,wbb3ihSize,wbb3ihSizePart = h.gram(w3_tree,leaf,xmin,xmax,steps,CutsMCiwbb,I,F)
 wbb3ih.SetName('wbb3ih')
 wbb3ih.Scale(sf_wjets)
 print('  '+str(wbb3ihSize))
 print('  '+str(wbb3ihSizePart))
#####
 print('wl 4 Iso')
 wl4ih,wl4ihSize,wl4ihSizePart = h.gram(w4_tree,leaf,xmin,xmax,steps,CutsMCiwl,I,F)
 wl4ih.SetName('wl4ih')
 wl4ih.Scale(sf_wjets)
 print('  '+str(wl4ihSize))
 print('  '+str(wl4ihSizePart))
 ####
 print('wc 4 Iso')
 wc4ih,wc4ihSize,wc4ihSizePart = h.gram(w4_tree,leaf,xmin,xmax,steps,CutsMCiwc,I,F)
 wc4ih.SetName('wc4ih')
 wc4ih.Scale(sf_wjets)
 print('  '+str(wc4ihSize))
 print('  '+str(wc4ihSizePart))
 ####
 print('wcc 4 Iso')
 wcc4ih,wcc4ihSize,wcc4ihSizePart = h.gram(w4_tree,leaf,xmin,xmax,steps,CutsMCiwcc,I,F)
 wcc4ih.SetName('wcc4ih')
 wcc4ih.Scale(sf_wjets)
 print('  '+str(wcc4ihSize))
 print('  '+str(wcc4ihSizePart))
 ####
 print('wbb 4 Iso')
 wbb4ih,wbb4ihSize,wbb4ihSizePart = h.gram(w4_tree,leaf,xmin,xmax,steps,CutsMCiwbb,I,F)
 wbb4ih.SetName('wbb4ih')
 wbb4ih.Scale(sf_wjets)
 print('  '+str(wbb4ihSize))
 print('  '+str(wbb4ihSizePart))
 
 outFile.Write()
 print('')
 print('Your File is here: '+path+leaf+extraName+'.root')
 print('')
 
 log.write('------------------------------------------------\n')
 log.write('QCD from Data:    '+str(qcdFromData)+'\n')
 log.write('Non Isolated\n')
 log.write('---------------------------\n')
 log.write(' Cuts MC:  '+str(CutsMCn)+'\n\n')
 log.write(' Cuts Data: '+str(CutsDatan)+'\n\n')
 log.write('Isolated\n')
 log.write('---------------------------\n')
 log.write(' Cuts MC:  '+str(CutsMCi)+'\n\n')
 log.write(' Cuts Data: '+str(CutsDatai)+'\n\n')
 log.write(' Cuts Wbb: '+str(CutsMCiwbb)+'\n\n')
 log.write(' Cuts Wcc: '+str(CutsMCiwcc)+'\n\n')
 log.write(' Cuts Wc: '+str(CutsMCiwc)+'\n\n')
 log.write(' Cuts Wl: '+str(CutsMCiwl)+'\n\n')
 log.write('Anti-Isolated Sizes\n')
 log.write('---------------------------\n')
 log.write(' Wn Size:--------'+str(wnnhSize)+'\n')
 log.write(' W1 Size:--------'+str(w1nhSize)+'\n')
 log.write(' W2 Size:--------'+str(w2nhSize)+'\n')
 log.write(' W3 Size:--------'+str(w3nhSize)+'\n')
 log.write(' W4 Size:--------'+str(w4nhSize)+'\n')
 log.write(' tt Size:--------'+str(ttbnhSize)+'\n')
 log.write(' t_t Size:-------'+str(t_tnhSize)+'\n')
 log.write(' tb_t Size:------'+str(tb_tnhSize)+'\n')
 log.write(' t_s Size:-------'+str(t_snhSize)+'\n')
 log.write(' tb_s Size:------'+str(tb_snhSize)+'\n')
 log.write(' t_tw Size:------'+str(t_twnhSize)+'\n')
 log.write(' tb_tw Size:-----'+str(tb_twnhSize)+'\n')
 log.write(' WW Size:--------'+str(wwnhSize)+'\n')
 log.write(' WZ Size:--------'+str(wznhSize)+'\n')
 log.write(' ZZ Size:--------'+str(zznhSize)+'\n')
 log.write(' Drell-Yan Size:-'+str(znhSize)+'\n')
 log.write(' QCD Size:-------'+str(qhSize)+'\n')
 log.write(' Data Size:      '+str(datanhSize)+'\n')
 log.write('---------------------------\n')
 log.write('Anti-Isolated Sizes from '+str(I)+' to '+str(F)+'\n')
 log.write('---------------------------\n')
 log.write(' Wn Size:--------'+str(wnnhSizePart)+'\n')
 log.write(' W1 Size:--------'+str(w1nhSizePart)+'\n')
 log.write(' W2 Size:--------'+str(w2nhSizePart)+'\n')
 log.write(' W3 Size:--------'+str(w3nhSizePart)+'\n')
 log.write(' W4 Size:--------'+str(w4nhSizePart)+'\n')
 log.write(' tt Size:--------'+str(ttbnhSizePart)+'\n')
 log.write(' t_t Size:-------'+str(t_tnhSizePart)+'\n')
 log.write(' tb_t Size:------'+str(tb_tnhSizePart)+'\n')
 log.write(' t_s Size:-------'+str(t_snhSizePart)+'\n')
 log.write(' tb_s Size:------'+str(tb_snhSizePart)+'\n')
 log.write(' t_tw Size:------'+str(t_twnhSizePart)+'\n')
 log.write(' tb_tw Size:-----'+str(tb_twnhSizePart)+'\n')
 log.write(' WW Size:--------'+str(wwnhSizePart)+'\n')
 log.write(' WZ Size:--------'+str(wznhSizePart)+'\n')
 log.write(' ZZ Size:--------'+str(zznhSizePart)+'\n')
 log.write(' Drell-Yan Size:-'+str(znhSizePart)+'\n')
 log.write(' QCD Size:-------'+str(qhSizePart)+'\n')
 log.write(' Data Size:      '+str(datanhSizePart)+'\n')
 log.write('---------------------------------------------\n')
 log.write('QCD Scale:   '+str(sf_qcd)+'\n')
 log.write('Drell Scale: '+str(sf_drell)+'\n')
 log.write('t Scale:     '+str(sf_st)+'\n')
 log.write('tt Scale:    '+str(sf_ttbar)+'\n')
 log.write('W+x Scale:   '+str(sf_wjets)+'\n')
 log.write('---------------------------------------------\n\n')
 log.write('Isolated Sizes from '+str(I)+' to '+str(F)+'\n')
 log.write('---------------------------\n')
 log.write('W:\n')
 log.write('  W+light:--------'+str(wlnihSizePart)+'\n')
 log.write('  W+light:--------'+str(wl1ihSizePart)+'\n')
 log.write('  W+light:--------'+str(wl2ihSizePart)+'\n')
 log.write('  W+light:--------'+str(wl3ihSizePart)+'\n')
 log.write('  W+light:--------'+str(wl4ihSizePart)+'\n\n')
 log.write('  W+c:------------'+str(wcnihSizePart)+'\n')
 log.write('  W+c:------------'+str(wc1ihSizePart)+'\n')
 log.write('  W+c:------------'+str(wc2ihSizePart)+'\n')
 log.write('  W+c:------------'+str(wc3ihSizePart)+'\n')
 log.write('  W+c:------------'+str(wc4ihSizePart)+'\n\n')
 log.write('  W+cc:-----------'+str(wccnihSizePart)+'\n')
 log.write('  W+cc:-----------'+str(wcc1ihSizePart)+'\n')
 log.write('  W+cc:-----------'+str(wcc2ihSizePart)+'\n')
 log.write('  W+cc:-----------'+str(wcc3ihSizePart)+'\n')
 log.write('  W+cc:-----------'+str(wcc4ihSizePart)+'\n\n')
 log.write('  W+bb:-----------'+str(wbbnihSizePart)+'\n')
 log.write('  W+bb:-----------'+str(wbb1ihSizePart)+'\n')
 log.write('  W+bb:-----------'+str(wbb2ihSizePart)+'\n')
 log.write('  W+bb:-----------'+str(wbb3ihSizePart)+'\n')
 log.write('  W+bb:-----------'+str(wbb4ihSizePart)+'\n')
 log.write('tt Size:--------'+str(ttbihSizePart)+'\n')
 log.write('t_t Size:-------'+str(t_tihSizePart)+'\n')
 log.write('tb_t Size:------'+str(tb_tihSizePart)+'\n')
 log.write('t_s Size:-------'+str(t_sihSizePart)+'\n')
 log.write('tb_s Size:------'+str(tb_sihSizePart)+'\n')
 log.write('t_tw Size:------'+str(t_twihSizePart)+'\n')
 log.write('tb_tw Size:-----'+str(tb_twihSizePart)+'\n')
 log.write('WW Size:--------'+str(wwihSizePart)+'\n')
 log.write('WZ Size:--------'+str(wzihSizePart)+'\n')
 log.write('ZZ Size:--------'+str(zzihSizePart)+'\n')
 log.write('Drell-Yan Size:-'+str(zihSizePart)+'\n')
 log.write('Data Size:          '+str(dataihSizePart)+'\n')
 log.write('---------------------------------------------\n')
 log.write('Isolated Sizes\n')
 log.write('---------------------------\n')
 log.write('W:\n')
 log.write('  Wn+light:--------'+str(wlnihSize)+'\n')
 log.write('  W1+light:--------'+str(wl1ihSize)+'\n')
 log.write('  W2+light:--------'+str(wl2ihSize)+'\n')
 log.write('  W3+light:--------'+str(wl3ihSize)+'\n')
 log.write('  W4+light:--------'+str(wl4ihSize)+'\n\n')
 log.write('  Wn+c:------------'+str(wcnihSize)+'\n')
 log.write('  W1+c:------------'+str(wc1ihSize)+'\n')
 log.write('  W2+c:------------'+str(wc2ihSize)+'\n')
 log.write('  W3+c:------------'+str(wc3ihSize)+'\n')
 log.write('  W4+c:------------'+str(wc4ihSize)+'\n\n')
 log.write('  Wn+cc:-----------'+str(wccnihSize)+'\n')
 log.write('  W1+cc:-----------'+str(wcc1ihSize)+'\n')
 log.write('  W2+cc:-----------'+str(wcc2ihSize)+'\n')
 log.write('  W3+cc:-----------'+str(wcc3ihSize)+'\n')
 log.write('  W4+cc:-----------'+str(wcc4ihSize)+'\n\n')
 log.write('  Wn+bb:-----------'+str(wbbnihSize)+'\n')
 log.write('  W1+bb:-----------'+str(wbb1ihSize)+'\n')
 log.write('  W2+bb:-----------'+str(wbb2ihSize)+'\n')
 log.write('  W3+bb:-----------'+str(wbb3ihSize)+'\n')
 log.write('  W4+bb:-----------'+str(wbb4ihSize)+'\n')
 log.write('tt Size:--------'+str(ttbihSize)+'\n')
 log.write('t_t Size:-------'+str(t_tihSize)+'\n')
 log.write('tb_t Size:------'+str(tb_tihSize)+'\n')
 log.write('t_s Size:-------'+str(t_sihSize)+'\n')
 log.write('tb_s Size:------'+str(tb_sihSize)+'\n')
 log.write('t_tw Size:------'+str(t_twihSize)+'\n')
 log.write('tb_tw Size:-----'+str(tb_twihSize)+'\n')
 log.write('WW Size:--------'+str(wwihSize)+'\n')
 log.write('WZ Size:--------'+str(wzihSize)+'\n')
 log.write('ZZ Size:--------'+str(zzihSize)+'\n')
 log.write('Drell-Yan Size:-'+str(zihSize)+'\n')
 log.write('Data Size:          '+str(dataihSize)+'\n')
 log.write('---------------------------\n')
 log.write('---------------------------------------------\n')
 
 print(".log written")
 log.close()
 
