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
import TheCuts as ct  #function which makes cut strings
import histoRange as hr #manages range, lables for plots
import TheParameters as p

#import scaleqcd as qs

sf_qcd = 2.03028050776
sf_drell = 1.
sf_st = 1.   
sf_st_t = 1.
sf_ttbar = 1.
sf_wjets = 1.
sf_vv = 1.

#get parameters (used in cutmaker)
lumi,bNr,btype,jNr,njetcut,jetcut,I,F,iso_value,antiIso_value,path,extraName,leafs,drawW,drawZ,drawQCD,drawData,jetVeto,Control,Z_Region,Legacy,noMT,TT_m,TT_me,ST,Signal,Tomislav,eventTreeLocation = p.arams() 

CutsMCn, CutsMCnW, CutsMCi,CutsDatan,CutsDatai,CutsMCnwl,CutsMCiwl,CutsMCnwc,CutsMCiwc,CutsMCnwcc,CutsMCiwcc,CutsMCnwbb,CutsMCiwbb,CutsMCnT,CutsMCiT = ct.cutmaker(
 iso_value,antiIso_value,lumi,bNr,btype,jNr,njetcut,jetcut,jetVeto,Control,Z_Region,Legacy,noMT,TT_m,TT_me,ST,Signal,Tomislav
)

data_filename  = '../data/v6/Data.root'
t_t_filename   = '../data/oldGT/T_t.root'
t_s_filename   = '../data/oldGT/T_s.root'
t_tw_filename  = '../data/oldGT/T_tW.root'
tb_t_filename  = '../data/oldGT/Tbar_t.root'
tb_s_filename  = '../data/oldGT/Tbar_s.root'
tb_tw_filename = '../data/oldGT/Tbar_tW.root'
ttb_filename   = '../data/oldGT/TTbar.root'
ww_filename    = '../data/oldGT/WW.root'
wz_filename    = '../data/oldGT/WZ.root'
zz_filename    = '../data/oldGT/ZZ.root'
wn_filename    = '../data/oldGT/WJets.root'
w1_filename    = '../data/oldGT/W1Jet.root'
w2_filename    = '../data/oldGT/W2Jet.root'
w3_filename    = '../data/oldGT/W3Jet.root'
w4_filename    = '../data/oldGT/W4Jet.root'
z_filename     = '../data/oldGT/Drell.root'

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

#Start the Plotting Program
leaf = leafs[0] 
extraName='Datacard_'+extraName
steps, xmin, xmax, xtitle, xunits, setLogY = hr.ranger(leaf)

outFile=gROOT.FindObject(path+extraName+'_'+leaf+'.root')
if outFile : outFile.Close()
outFile = TFile(path+extraName+'_'+leaf+'.root','RECREATE','Demo ROOT file')

log = open(path+extraName+'_'+leaf+'.log','w')

eventTreeLocations = ['muNuEventTree/eventTree',
                      'muNuEventTreeMuonUp/eventTree',
                      'muNuEventTreeMuonDown/eventTree',
                      'muNuEventTreeJetUp/eventTree',
                      'muNuEventTreeJetDown/eventTree'
                      'muNuEventTreeUCEUp/eventTree',
                      'muNuEventTreeUCEDown/eventTree'
                     ]
for eventTreeLocation in eventTreeLocations:
 
 print('\n\n'+eventTreeLocation)
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
 
 
 print('----------------------------')
 print('      --'+leaf+'--')
 print(extraName)
 print('----------------------------')
 
 if drawQCD:
  if eventTreeLocation ==  'muNuEventTree/eventTree' :
   ###
   datanh,datanhSize,datanhSizePart,datanhEntries = h.gram(data_tree,leaf,xmin,xmax,steps,CutsDatan,I,F)
   print('For QCD Shape')
   print('data nonIso')
   datanh.SetName('datanh')
   print('  '+str(datanhSize))
   print('  '+str(datanhSizePart))
 ####  Drell
  print('  z nonIso')
  znh,znhSize,znhSizePart,znhEntries = h.gram(z_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
  znh.SetName('znh')
  znh.Scale(sf_drell)
  print('    '+str(znhSize))
  print('    '+str(znhSizePart))
 ####  Dibosons
  print('  ww nonIso')
  wwnh,wwnhSize,wwnhSizePart,wwnhEntries = h.gram(ww_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
  wwnh.SetName('wwnh')
  wwnh.Scale(sf_vv)
  print('    '+str(wwnhSize))
  print('    '+str(wwnhSizePart))
  ###
  print('  wz nonIso')
  wznh,wznhSize,wznhSizePart,wznhEntries = h.gram(wz_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
  wznh.SetName('wznh')
  wznh.Scale(sf_vv)
  print('    '+str(wznhSize))
  print('    '+str(wznhSizePart))
  ###
  print('  ww nonIso')
  zznh,zznhSize,zznhSizePart,zznhEntries = h.gram(zz_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
  zznh.SetName('zznh')
  zznh.Scale(sf_vv)
  print('    '+str(zznhSize))
  print('    '+str(zznhSizePart))
 ####  Single Top
  print('  t t nonIso')
  t_tnh,t_tnhSize,t_tnhSizePart,t_tnhEntries = h.gram(t_t_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
  t_tnh.SetName('t_tnh')
  t_tnh.Scale(sf_st_t)
  print('    '+str(t_tnhSize))
  print('    '+str(t_tnhSizePart))
  ###
  print('  tb t nonIso')
  tb_tnh,tb_tnhSize,tb_tnhSizePart,tb_tnhEntries = h.gram(tb_t_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
  tb_tnh.SetName('tb_tnh')
  tb_tnh.Scale(sf_st)
  print('    '+str(tb_tnhSize))
  print('    '+str(tb_tnhSizePart))
  ###
  print('  t s nonIso')
  t_snh,t_snhSize,t_snhSizePart,t_snhEntries = h.gram(t_s_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
  t_snh.SetName('t_snh')
  t_snh.Scale(sf_st)
  print('    '+str(t_snhSize))
  print('    '+str(t_snhSizePart))
  ###
  print('  tb s nonIso')
  tb_snh,tb_snhSize,tb_snhSizePart,tb_snhEntries = h.gram(tb_s_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
  tb_snh.SetName('tb_snh')
  tb_snh.Scale(sf_st)
  print('    '+str(tb_snhSize))
  print('    '+str(tb_snhSizePart))
  ###
  print('  t tw nonIso')
  t_twnh,t_twnhSize,t_twnhSizePart,t_twnhEntries = h.gram(t_tw_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
  t_twnh.SetName('t_twnh')
  t_twnh.Scale(sf_st)
  print('    '+str(t_twnhSize))
  print('    '+str(t_twnhSizePart))
  ###
  print('  tb tw nonIso')
  tb_twnh,tb_twnhSize,tb_twnhSizePart,tb_twnhEntries = h.gram(tb_tw_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
  tb_twnh.SetName('tb_twnh')
  tb_twnh.Scale(sf_st)
  print('    '+str(tb_twnhSize))
  print('    '+str(tb_twnhSizePart))
 ####  TTbar
  print('  ttbar nonIso')
  ttbnh,ttbnhSize,ttbnhSizePart,ttbnhEntries = h.gram(ttb_tree,leaf,xmin,xmax,steps,CutsMCnT,I,F)
  ttbnh.SetName('ttbnh')
  ttbnh.Scale(sf_ttbar)
  print('    '+str(ttbnhSize))
  print('    '+str(ttbnhSizePart))
 ####  W
  print('  wn nonIso')
  wnnh,wnnhSize,wnnhSizePart,wnhEntries = h.gram(wn_tree,leaf,xmin,xmax,steps,CutsMCnW,I,F)
  wnnh.SetName('wnnh')
  wnnh.Scale(sf_wjets)
  print('    '+str(wnnhSize))
  print('    '+str(wnnhSizePart))
  print('  w1 nonIso')
  ###
  w1nh,w1nhSize,w1nhSizePart,w1nhEntries = h.gram(w1_tree,leaf,xmin,xmax,steps,CutsMCnW,I,F)
  w1nh.SetName('w1nh')
  w1nh.Scale(sf_wjets)
  print('    '+str(w1nhSize))
  print('    '+str(w1nhSizePart))
  print('  w2 nonIso')
  ###
  w2nh,w2nhSize,w2nhSizePart,w2nhEntries = h.gram(w2_tree,leaf,xmin,xmax,steps,CutsMCnW,I,F)
  w2nh.SetName('w2nh')
  w2nh.Scale(sf_wjets)
  print('    '+str(w2nhSize))
  print('    '+str(w2nhSizePart))
  print('  w3 nonIso')
  ###
  w3nh,w3nhSize,w3nhSizePart,w3nhEntries = h.gram(w3_tree,leaf,xmin,xmax,steps,CutsMCnW,I,F)
  w3nh.SetName('w3nh')
  w3nh.Scale(sf_wjets)
  print('    '+str(w3nhSize))
  print('    '+str(w3nhSizePart))
  print('  w4 nonIso')
  ###
  w4nh,w4nhSize,w4nhSizePart,w4nhEntries = h.gram(w4_tree,leaf,xmin,xmax,steps,CutsMCnW,I,F)
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
  qhEntries = qh.GetEntries()
  print('  '+str(qhSize))
  print('  '+str(qhSizePart))
 ####################################
 if drawData and  eventTreeLocation == 'muNuEventTree/eventTree':
  ### Data
  print('')
  print('Isolated Variables Now')
  print("data Iso") 
  dataih,dataihSize,dataihSizePart,dataihEntries = h.gram(data_tree,leaf,xmin,xmax,steps,CutsDatai,I,F)
  dataih.SetName('dataih')
  print('  '+str(dataihSize))
  print('  '+str(dataihSizePart))
  dimax = dataih.GetMaximum()
#### Drell
 print("z Iso")
 zih,zihSize,zihSizePart,zihEntries = h.gram(z_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 zih.SetName('zih')
 zih.Scale(sf_drell)
 print('  '+str(zihSize))
 print('  '+str(zihSizePart))
#### Diboson
 print("ww Iso")
 wwih,wwihSize,wwihSizePart,wwihEntries = h.gram(ww_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 wwih.SetName('wwih')
 wwih.Scale(sf_vv)
 print('  '+str(wwihSize))
 print('  '+str(wwihSizePart))
 ###
 print("wz Iso")
 wzih,wzihSize,wzihSizePart,wzihEntries = h.gram(wz_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 wzih.SetName('wzih')
 wzih.Scale(sf_vv)
 print('  '+str(wzihSize))
 print('  '+str(wzihSizePart))
 ###
 print("zz Iso")
 zzih,zzihSize,zzihSizePart,zzihEntries = h.gram(zz_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 zzih.SetName('zzih')
 zzih.Scale(sf_vv)
 print('  '+str(zzihSize))
 print('  '+str(zzihSizePart))
#### Single Top
 print('t t Iso')
 t_tih,t_tihSize,t_tihSizePart,t_tihEntries = h.gram(t_t_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 t_tih.SetName('t_tih')
 t_tih.Scale(sf_st_t)
 print('  '+str(t_tihSize))
 print('  '+str(t_tihSizePart))
 ###
 print('tb t Iso')
 tb_tih,tb_tihSize,tb_tihSizePart,tb_tihEntries = h.gram(tb_t_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 tb_tih.SetName('tb_tih')
 tb_tih.Scale(sf_st)
 print('  '+str(tb_tihSize))
 print('  '+str(tb_tihSizePart))
 ###
 print('t s Iso')
 t_sih,t_sihSize,t_sihSizePart,t_sihEntries = h.gram(t_s_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 t_sih.SetName('t_sih')
 t_sih.Scale(sf_st)
 print('  '+str(t_sihSize))
 print('  '+str(t_sihSizePart))
 ###
 print('tb s Iso')
 tb_sih,tb_sihSize,tb_sihSizePart,tb_sihEntries = h.gram(tb_s_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 tb_sih.SetName('tb_sih')
 tb_sih.Scale(sf_st)
 print('  '+str(tb_sihSize))
 print('  '+str(tb_sihSizePart))
 ###
 print('t tw Iso')
 t_twih,t_twihSize,t_twihSizePart,t_twihEntries = h.gram(t_tw_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 t_twih.SetName('t_twih')
 t_twih.Scale(sf_st)
 print('  '+str(t_twihSize))
 print('  '+str(t_twihSizePart))
 ###
 print('tb tw Iso')
 tb_twih,tb_twihSize,tb_twihSizePart,tb_twihEntries = h.gram(tb_tw_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 tb_twih.SetName('tb_twih')
 tb_twih.Scale(sf_st)
 print('  '+str(tb_twihSize))
 print('  '+str(tb_twihSizePart))
#### TTbar
 print('ttb Iso')
 ttbih,ttbihSize,ttbihSizePart,ttbihEntries = h.gram(ttb_tree,leaf,xmin,xmax,steps,CutsMCiT,I,F)
 ttbih.SetName('ttbih')
 ttbih.Scale(sf_ttbar)
 print('  '+str(ttbihSize))
 print('  '+str(ttbihSizePart))
#### W + Jets
 print('wl n Iso')
 wlnih,wlnihSize,wlnihSizePart,wlnihEntries = h.gram(wn_tree,leaf,xmin,xmax,steps,CutsMCiwl,I,F)
 wlnih.SetName('wlnih')
 wlnih.Scale(sf_wjets)
 print('  '+str(wlnihSize))
 print('  '+str(wlnihSizePart))
 ####
 print('wc n Iso')
 wcnih,wcnihSize,wcnihSizePart,wcnihEntries = h.gram(wn_tree,leaf,xmin,xmax,steps,CutsMCiwc,I,F)
 wcnih.SetName('wcnih')
 wcnih.Scale(sf_wjets)
 print('  '+str(wcnihSize))
 print('  '+str(wcnihSizePart))
 ####
 print('wcc n Iso')
 wccnih,wccnihSize,wccnihSizePart,wccnihEntries = h.gram(wn_tree,leaf,xmin,xmax,steps,CutsMCiwcc,I,F)
 wccnih.SetName('wccnih')
 wccnih.Scale(sf_wjets)
 print('  '+str(wccnihSize))
 print('  '+str(wccnihSizePart))
 ####
 print('wbb n Iso')
 wbbnih,wbbnihSize,wbbnihSizePart,wbbnihEntries = h.gram(wn_tree,leaf,xmin,xmax,steps,CutsMCiwbb,I,F)
 wbbnih.SetName('wbbnih')
 wbbnih.Scale(sf_wjets)
 print('  '+str(wbbnihSize))
 print('  '+str(wbbnihSizePart))
#####
 print('wl 1 Iso')
 wl1ih,wl1ihSize,wl1ihSizePart,wl1ihEntries = h.gram(w1_tree,leaf,xmin,xmax,steps,CutsMCiwl,I,F)
 wl1ih.SetName('wl1ih')
 wl1ih.Scale(sf_wjets)
 print('  '+str(wl1ihSize))
 print('  '+str(wl1ihSizePart))
 ####
 print('wc 1 Iso')
 wc1ih,wc1ihSize,wc1ihSizePart,wc1ihEntries = h.gram(w1_tree,leaf,xmin,xmax,steps,CutsMCiwc,I,F)
 wc1ih.SetName('wc1ih')
 wc1ih.Scale(sf_wjets)
 print('  '+str(wc1ihSize))
 print('  '+str(wc1ihSizePart))
 ####
 print('wcc 1 Iso')
 wcc1ih,wcc1ihSize,wcc1ihSizePart,wcc1ihEntries = h.gram(w1_tree,leaf,xmin,xmax,steps,CutsMCiwcc,I,F)
 wcc1ih.SetName('wcc1ih')
 wcc1ih.Scale(sf_wjets)
 print('  '+str(wcc1ihSize))
 print('  '+str(wcc1ihSizePart))
 ####
 print('wbb 1 Iso')
 wbb1ih,wbb1ihSize,wbb1ihSizePart,wbb1ihEntries = h.gram(w1_tree,leaf,xmin,xmax,steps,CutsMCiwbb,I,F)
 wbb1ih.SetName('wbb1ih')
 wbb1ih.Scale(sf_wjets)
 print('  '+str(wbb1ihSize))
 print('  '+str(wbb1ihSizePart))
#####
 print('wl 2 Iso')
 wl2ih,wl2ihSize,wl2ihSizePart,wl2ihEntries = h.gram(w2_tree,leaf,xmin,xmax,steps,CutsMCiwl,I,F)
 wl2ih.SetName('wl2ih')
 wl2ih.Scale(sf_wjets)
 print('  '+str(wl2ihSize))
 print('  '+str(wl2ihSizePart))
 ####
 print('wc 2 Iso')
 wc2ih,wc2ihSize,wc2ihSizePart,wc2ihEntries = h.gram(w2_tree,leaf,xmin,xmax,steps,CutsMCiwc,I,F)
 wc2ih.SetName('wc2ih')
 wc2ih.Scale(sf_wjets)
 print('  '+str(wc2ihSize))
 print('  '+str(wc2ihSizePart))
 ####
 print('wcc 2 Iso')
 wcc2ih,wcc2ihSize,wcc2ihSizePart,wcc2ihEntries = h.gram(w2_tree,leaf,xmin,xmax,steps,CutsMCiwcc,I,F)
 wcc2ih.SetName('wcc2ih')
 wcc2ih.Scale(sf_wjets)
 print('  '+str(wcc2ihSize))
 print('  '+str(wcc2ihSizePart))
 ####
 print('wbb 2 Iso')
 wbb2ih,wbb2ihSize,wbb2ihSizePart,wbb2ihEntries = h.gram(w2_tree,leaf,xmin,xmax,steps,CutsMCiwbb,I,F)
 wbb2ih.SetName('wbb2ih')
 wbb2ih.Scale(sf_wjets)
 print('  '+str(wbb2ihSize))
 print('  '+str(wbb2ihSizePart))
#####
 print('wl 3 Iso')
 wl3ih,wl3ihSize,wl3ihSizePart,wl3ihEntries = h.gram(w3_tree,leaf,xmin,xmax,steps,CutsMCiwl,I,F)
 wl3ih.SetName('wl3ih')
 wl3ih.Scale(sf_wjets)
 print('  '+str(wl3ihSize))
 print('  '+str(wl3ihSizePart))
 ####
 print('wc 3 Iso')
 wc3ih,wc3ihSize,wc3ihSizePart,wc3ihEntries = h.gram(w3_tree,leaf,xmin,xmax,steps,CutsMCiwc,I,F)
 wc3ih.SetName('wc3ih')
 wc3ih.Scale(sf_wjets)
 print('  '+str(wc3ihSize))
 print('  '+str(wc3ihSizePart))
 ####
 print('wcc 3 Iso')
 wcc3ih,wcc3ihSize,wcc3ihSizePart,wcc3ihEntries = h.gram(w3_tree,leaf,xmin,xmax,steps,CutsMCiwcc,I,F)
 wcc3ih.SetName('wcc3ih')
 wcc3ih.Scale(sf_wjets)
 print('  '+str(wcc3ihSize))
 print('  '+str(wcc3ihSizePart))
 ####
 print('wbb 3 Iso')
 wbb3ih,wbb3ihSize,wbb3ihSizePart,wbb3ihEntries = h.gram(w3_tree,leaf,xmin,xmax,steps,CutsMCiwbb,I,F)
 wbb3ih.SetName('wbb3ih')
 wbb3ih.Scale(sf_wjets)
 print('  '+str(wbb3ihSize))
 print('  '+str(wbb3ihSizePart))
#####
 print('wl 4 Iso')
 wl4ih,wl4ihSize,wl4ihSizePart,wl4ihEntries = h.gram(w4_tree,leaf,xmin,xmax,steps,CutsMCiwl,I,F)
 wl4ih.SetName('wl4ih')
 wl4ih.Scale(sf_wjets)
 print('  '+str(wl4ihSize))
 print('  '+str(wl4ihSizePart))
 ####
 print('wc 4 Iso')
 wc4ih,wc4ihSize,wc4ihSizePart,wc4ihEntries = h.gram(w4_tree,leaf,xmin,xmax,steps,CutsMCiwc,I,F)
 wc4ih.SetName('wc4ih')
 wc4ih.Scale(sf_wjets)
 print('  '+str(wc4ihSize))
 print('  '+str(wc4ihSizePart))
 ####
 print('wcc 4 Iso')
 wcc4ih,wcc4ihSize,wcc4ihSizePart,wcc4ihEntries = h.gram(w4_tree,leaf,xmin,xmax,steps,CutsMCiwcc,I,F)
 wcc4ih.SetName('wcc4ih')
 wcc4ih.Scale(sf_wjets)
 print('  '+str(wcc4ihSize))
 print('  '+str(wcc4ihSizePart))
 ####
 print('wbb 4 Iso')
 wbb4ih,wbb4ihSize,wbb4ihSizePart,wbb4ihEntries = h.gram(w4_tree,leaf,xmin,xmax,steps,CutsMCiwbb,I,F)
 wbb4ih.SetName('wbb4ih')
 wbb4ih.Scale(sf_wjets)
 print('  '+str(wbb4ihSize))
 print('  '+str(wbb4ihSizePart))
 
 if eventTreeLocation == 'muNuEventTree/eventTree' :
  qihNo     = qh.Clone()
  qihNo.SetName("qhNo")
  zihNo     = zih.Clone()
  zihNo.SetName("zihNo")
  vvihNo    = wwih.Clone()
  vvihNo.SetName("vvihNo")
  vvihNo.Add(wzih)
  vvihNo.Add(zzih)
  tihNo     = t_tih.Clone()
  tihNo.SetName("tihNo")
  tihNo.Add(t_sih)
  tbihNo    = tb_tih.Clone()
  tbihNo.SetName("tbihNo")
  tbihNo.Add(tb_sih)
  t_twihNo  = t_twih.Clone()
  t_twihNo.SetName("t_twihNo")
  t_twihNo.Add(tb_twih)
  ttbihNo   = ttbih.Clone()
  ttbihNo.SetName("ttbihNo")
  wlihNo    = wlnih.Clone()
  wlihNo.SetName("wlihNo")
  wlihNo.Add(wl1ih)
  wlihNo.Add(wl2ih)
  wlihNo.Add(wl3ih)
  wlihNo.Add(wl4ih)
  wcihNo    = wcnih.Clone()
  wcihNo.SetName("wcihNo")
  wcihNo.Add(wc1ih)
  wcihNo.Add(wc2ih)
  wcihNo.Add(wc3ih)
  wcihNo.Add(wc4ih)
  wccihNo   = wccnih.Clone()
  wccihNo.SetName("wccihNo")
  wccihNo.Add(wcc1ih)
  wccihNo.Add(wcc2ih)
  wccihNo.Add(wcc3ih)
  wccihNo.Add(wcc4ih)
  wbbihNo   = wbbnih.Clone()
  wbbihNo.SetName("wbbihNo")
  wbbihNo.Add(wbb1ih)
  wbbihNo.Add(wbb2ih)
  wbbihNo.Add(wbb3ih)
  wbbihNo.Add(wbb4ih)

 if eventTreeLocation == 'muNuEventTreeMuonUp/eventTree' :
  qihUp     = qh.Clone()
  qihUp.SetName("qhUp")
  zihUp     = zih.Clone()
  zihUp.SetName("zihUp")
  vvihUp    = wwih.Clone()
  vvihUp.SetName("vvihUp")
  vvihUp.Add(wzih)
  vvihUp.Add(zzih)
  tihUp     = t_tih.Clone()
  tihUp.SetName("tihUp")
  tihUp.Add(t_sih)
  tbihUp    = tb_tih.Clone()
  tbihUp.SetName("tbihUp")
  tbihUp.Add(tb_sih)
  t_twihUp  = t_twih.Clone()
  t_twihUp.SetName("t_twihUp")
  t_twihUp.Add(tb_twih)
  ttbihUp   = ttbih.Clone()
  ttbihUp.SetName("ttbihUp")
  wlihUp    = wlnih.Clone()
  wlihUp.SetName("wlihUp")
  wlihUp.Add(wl1ih)
  wlihUp.Add(wl2ih)
  wlihUp.Add(wl3ih)
  wlihUp.Add(wl4ih)
  wcihUp    = wcnih.Clone()
  wcihUp.SetName("wcihUp")
  wcihUp.Add(wc1ih)
  wcihUp.Add(wc2ih)
  wcihUp.Add(wc3ih)
  wcihUp.Add(wc4ih)
  wccihUp   = wccnih.Clone()
  wccihUp.SetName("wccihUp")
  wccihUp.Add(wcc1ih)
  wccihUp.Add(wcc2ih)
  wccihUp.Add(wcc3ih)
  wccihUp.Add(wcc4ih)
  wbbihUp   = wbbnih.Clone()
  wbbihUp.SetName("wbbihUp")
  wbbihUp.Add(wbb1ih)
  wbbihUp.Add(wbb2ih)
  wbbihUp.Add(wbb3ih)
  wbbihUp.Add(wbb4ih)

 if eventTreeLocation == 'muNuEventTreeMuonDown/eventTree' : 
  qihDn     = qh.Clone()
  qihDn.SetName("qhDn")
  zihDn     = zih.Clone()
  zihDn.SetName("zihDn")
  vvihDn    = wwih.Clone()
  vvihDn.SetName("vvihDn")
  vvihDn.Add(wzih)
  vvihDn.Add(zzih)
  tihDn     = t_tih.Clone()
  tihDn.SetName("tihDn")
  tihDn.Add(t_sih)
  tbihDn    = tb_tih.Clone()
  tbihDn.SetName("tbihDn")
  tbihDn.Add(tb_sih)
  t_twihDn  = t_twih.Clone()
  t_twihDn.SetName("t_twihDn")
  t_twihDn.Add(tb_twih)
  ttbihDn   = ttbih.Clone()
  ttbihDn.SetName("ttbihDn")
  wlihDn    = wlnih.Clone()
  wlihDn.SetName("wlihDn")
  wlihDn.Add(wl1ih)
  wlihDn.Add(wl2ih)
  wlihDn.Add(wl3ih)
  wlihDn.Add(wl4ih)
  wcihDn    = wcnih.Clone()
  wcihDn.SetName("wcihDn")
  wcihDn.Add(wc1ih)
  wcihDn.Add(wc2ih)
  wcihDn.Add(wc3ih)
  wcihDn.Add(wc4ih)
  wccihDn   = wccnih.Clone()
  wccihDn.SetName("wccihDn")
  wccihDn.Add(wcc1ih)
  wccihDn.Add(wcc2ih)
  wccihDn.Add(wcc3ih)
  wccihDn.Add(wcc4ih)
  wbbihDn   = wbbnih.Clone()
  wbbihDn.SetName("wbbihDn")
  wbbihDn.Add(wbb1ih)
  wbbihDn.Add(wbb2ih)
  wbbihDn.Add(wbb3ih)
  wbbihDn.Add(wbb4ih)

 if eventTreeLocation == 'muNuEventTreeJetUp/eventTree' : 
  qihJUp     = qh.Clone()
  qihJUp.SetName("qhJUp")
  zihJUp     = zih.Clone()
  zihJUp.SetName("zihJUp")
  vvihJUp    = wwih.Clone()
  vvihJUp.SetName("vvihJUp")
  vvihJUp.Add(wzih)
  vvihJUp.Add(zzih)
  tihJUp     = t_tih.Clone()
  tihJUp.SetName("tihJUp")
  tihJUp.Add(t_sih)
  tbihJUp    = tb_tih.Clone()
  tbihJUp.SetName("tbihJUp")
  tbihJUp.Add(tb_sih)
  t_twihJUp  = t_twih.Clone()
  t_twihJUp.SetName("t_twihJUp")
  t_twihJUp.Add(tb_twih)
  ttbihJUp   = ttbih.Clone()
  ttbihJUp.SetName("ttbihJUp")
  wlihJUp    = wlnih.Clone()
  wlihJUp.SetName("wlihJUp")
  wlihJUp.Add(wl1ih)
  wlihJUp.Add(wl2ih)
  wlihJUp.Add(wl3ih)
  wlihJUp.Add(wl4ih)
  wcihJUp    = wcnih.Clone()
  wcihJUp.SetName("wcihJUp")
  wcihJUp.Add(wc1ih)
  wcihJUp.Add(wc2ih)
  wcihJUp.Add(wc3ih)
  wcihJUp.Add(wc4ih)
  wccihJUp   = wccnih.Clone()
  wccihJUp.SetName("wccihJUp")
  wccihJUp.Add(wcc1ih)
  wccihJUp.Add(wcc2ih)
  wccihJUp.Add(wcc3ih)
  wccihJUp.Add(wcc4ih)
  wbbihJUp   = wbbnih.Clone()
  wbbihJUp.SetName("wbbihJUp")
  wbbihJUp.Add(wbb1ih)
  wbbihJUp.Add(wbb2ih)
  wbbihJUp.Add(wbb3ih)
  wbbihJUp.Add(wbb4ih)

 if eventTreeLocation == 'muNuEventTreeJetDown/eventTree' : 
  qihJDn     = qh.Clone()
  qihJDn.SetName("qhJDn")
  zihJDn     = zih.Clone()
  zihJDn.SetName("zihJDn")
  vvihJDn    = wwih.Clone()
  vvihJDn.SetName("vvihJDn")
  vvihJDn.Add(wzih)
  vvihJDn.Add(zzih)
  tihJDn     = t_tih.Clone()
  tihJDn.SetName("tihJDn")
  tihJDn.Add(t_sih)
  tbihJDn    = tb_tih.Clone()
  tbihJDn.SetName("tbihJDn")
  tbihJDn.Add(tb_sih)
  t_twihJDn  = t_twih.Clone()
  t_twihJDn.SetName("t_twihJDn")
  t_twihJDn.Add(tb_twih)
  ttbihJDn   = ttbih.Clone()
  ttbihJDn.SetName("ttbihJDn")
  wlihJDn    = wlnih.Clone()
  wlihJDn.SetName("wlihJDn")
  wlihJDn.Add(wl1ih)
  wlihJDn.Add(wl2ih)
  wlihJDn.Add(wl3ih)
  wlihJDn.Add(wl4ih)
  wcihJDn    = wcnih.Clone()
  wcihJDn.SetName("wcihJDn")
  wcihJDn.Add(wc1ih)
  wcihJDn.Add(wc2ih)
  wcihJDn.Add(wc3ih)
  wcihJDn.Add(wc4ih)
  wccihJDn   = wccnih.Clone()
  wccihJDn.SetName("wccihJDn")
  wccihJDn.Add(wcc1ih)
  wccihJDn.Add(wcc2ih)
  wccihJDn.Add(wcc3ih)
  wccihJDn.Add(wcc4ih)
  wbbihJDn   = wbbnih.Clone()
  wbbihJDn.SetName("wbbihJDn")
  wbbihJDn.Add(wbb1ih)
  wbbihJDn.Add(wbb2ih)
  wbbihJDn.Add(wbb3ih)
  wbbihJDn.Add(wbb4ih)

 if eventTreeLocation == 'muNuEventTreeUCEUp/eventTree':
  qihUUp     = qh.Clone()
  qihUUp.SetName("qhUUp")
  zihUUp     = zih.Clone()
  zihUUp.SetName("zihUUp")
  vvihUUp    = wwih.Clone()
  vvihUUp.SetName("vvihUUp")
  vvihUUp.Add(wzih)
  vvihUUp.Add(zzih)
  tihUUp     = t_tih.Clone()
  tihUUp.SetName("tihUUp")
  tihUUp.Add(t_sih)
  tbihUUp    = tb_tih.Clone()
  tbihUUp.SetName("tbihUUp")
  tbihUUp.Add(tb_sih)
  t_twihUUp  = t_twih.Clone()
  t_twihUUp.SetName("t_twihUUp")
  t_twihUUp.Add(tb_twih)
  ttbihUUp   = ttbih.Clone()
  ttbihUUp.SetName("ttbihUUp")
  wlihUUp    = wlnih.Clone()
  wlihUUp.SetName("wlihUUp")
  wlihUUp.Add(wl1ih)
  wlihUUp.Add(wl2ih)
  wlihUUp.Add(wl3ih)
  wlihUUp.Add(wl4ih)
  wcihUUp    = wcnih.Clone()
  wcihUUp.SetName("wcihUUp")
  wcihUUp.Add(wc1ih)
  wcihUUp.Add(wc2ih)
  wcihUUp.Add(wc3ih)
  wcihUUp.Add(wc4ih)
  wccihUUp   = wccnih.Clone()
  wccihUUp.SetName("wccihUUp")
  wccihUUp.Add(wcc1ih)
  wccihUUp.Add(wcc2ih)
  wccihUUp.Add(wcc3ih)
  wccihUUp.Add(wcc4ih)
  wbbihUUp   = wbbnih.Clone()
  wbbihUUp.SetName("wbbihUUp")
  wbbihUUp.Add(wbb1ih)
  wbbihUUp.Add(wbb2ih)
  wbbihUUp.Add(wbb3ih)
  wbbihUUp.Add(wbb4ih)

 if eventTreeLocation == 'muNuEventTreeUCEDown/eventTree' :
  qihUDn     = qh.Clone()
  qihUDn.SetName("qhUDn")
  zihUDn     = zih.Clone()
  zihUDn.SetName("zihUDn")
  vvihUDn    = wwih.Clone()
  vvihUDn.SetName("vvihUDn")
  vvihUDn.Add(wzih)
  vvihUDn.Add(zzih)
  tihUDn     = t_tih.Clone()
  tihUDn.SetName("tihUDn")
  tihUDn.Add(t_sih)
  tbihUDn    = tb_tih.Clone()
  tbihUDn.SetName("tbihUDn")
  tbihUDn.Add(tb_sih)
  t_twihUDn  = t_twih.Clone()
  t_twihUDn.SetName("t_twihUDn")
  t_twihUDn.Add(tb_twih)
  ttbihUDn   = ttbih.Clone()
  ttbihUDn.SetName("ttbihUDn")
  wlihUDn    = wlnih.Clone()
  wlihUDn.SetName("wlihUDn")
  wlihUDn.Add(wl1ih)
  wlihUDn.Add(wl2ih)
  wlihUDn.Add(wl3ih)
  wlihUDn.Add(wl4ih)
  wcihUDn    = wcnih.Clone()
  wcihUDn.SetName("wcihUDn")
  wcihUDn.Add(wc1ih)
  wcihUDn.Add(wc2ih)
  wcihUDn.Add(wc3ih)
  wcihUDn.Add(wc4ih)
  wccihUDn   = wccnih.Clone()
  wccihUDn.SetName("wccihUDn")
  wccihUDn.Add(wcc1ih)
  wccihUDn.Add(wcc2ih)
  wccihUDn.Add(wcc3ih)
  wccihUDn.Add(wcc4ih)
  wbbihUDn   = wbbnih.Clone()
  wbbihUDn.SetName("wbbihUDn")
  wbbihUDn.Add(wbb1ih)
  wbbihUDn.Add(wbb2ih)
  wbbihUDn.Add(wbb3ih)
  wbbihUDn.Add(wbb4ih)

 log.write('\n\n\n'+eventTreeLocation+'\n')
 log.write('------------------------------------------------\n')
 log.write('Non Isolated\n')
 log.write('---------------------------\n')
 log.write(' Cuts MC:      \n'+str(CutsMCn)+'\n\n')
 log.write(' Cuts MC Top:  \n'+str(CutsMCnT)+'\n\n')
 log.write(' Cuts Data:    \n'+str(CutsDatan)+'\n\n')
 log.write('Isolated\n')
 log.write('---------------------------\n')
 log.write(' Cuts MC:  \n'+str(CutsMCi)+'\n\n')
 log.write(' Cuts MC Top:  \n'+str(CutsMCiT)+'\n\n')
 log.write(' Cuts Data: \n'+str(CutsDatai)+'\n\n')
 log.write(' Cuts Wbb: \n'+str(CutsMCiwbb)+'\n\n')
 log.write(' Cuts Wcc: \n'+str(CutsMCiwcc)+'\n\n')
 log.write(' Cuts Wc: \n'+str(CutsMCiwc)+'\n\n')
 log.write(' Cuts Wl: \n'+str(CutsMCiwl)+'\n\n')
 if drawQCD:
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
 else:
  log.write('no qcd drawn\n\n')
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
 if drawData:
  log.write('Data Size:          '+str(dataihSizePart)+'\n')
 else:
  log.write('no Data drawn\n')
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
 if drawData:
  log.write('Data Size:          '+str(dataihSize)+'\n')
 log.write('---------------------------------------------\n')
 log.write('---------------------------\n')
 log.write('Isolated Number of Entries\n')
 log.write('---------------------------\n')
 log.write('W:\n')
 log.write('  Wn+light:--------'+str(wlnihEntries)+'\n')
 log.write('  W1+light:--------'+str(wl1ihEntries)+'\n')
 log.write('  W2+light:--------'+str(wl2ihEntries)+'\n')
 log.write('  W3+light:--------'+str(wl3ihEntries)+'\n')
 log.write('  W4+light:--------'+str(wl4ihEntries)+'\n\n')
 log.write('  Wn+c:------------'+str(wcnihEntries)+'\n')
 log.write('  W1+c:------------'+str(wc1ihEntries)+'\n')
 log.write('  W2+c:------------'+str(wc2ihEntries)+'\n')
 log.write('  W3+c:------------'+str(wc3ihEntries)+'\n')
 log.write('  W4+c:------------'+str(wc4ihEntries)+'\n\n')
 log.write('  Wn+cc:-----------'+str(wccnihEntries)+'\n')
 log.write('  W1+cc:-----------'+str(wcc1ihEntries)+'\n')
 log.write('  W2+cc:-----------'+str(wcc2ihEntries)+'\n')
 log.write('  W3+cc:-----------'+str(wcc3ihEntries)+'\n')
 log.write('  W4+cc:-----------'+str(wcc4ihEntries)+'\n\n')
 log.write('  Wn+bb:-----------'+str(wbbnihEntries)+'\n')
 log.write('  W1+bb:-----------'+str(wbb1ihEntries)+'\n')
 log.write('  W2+bb:-----------'+str(wbb2ihEntries)+'\n')
 log.write('  W3+bb:-----------'+str(wbb3ihEntries)+'\n')
 log.write('  W4+bb:-----------'+str(wbb4ihEntries)+'\n')
 log.write('tt Entries:--------'+str(ttbihEntries)+'\n')
 log.write('t_t Entries:-------'+str(t_tihEntries)+'\n')
 log.write('tb_t Entries:------'+str(tb_tihEntries)+'\n')
 log.write('t_s Entries:-------'+str(t_sihEntries)+'\n')
 log.write('tb_s Entries:------'+str(tb_sihEntries)+'\n')
 log.write('t_tw Entries:------'+str(t_twihEntries)+'\n')
 log.write('tb_tw Entries:-----'+str(tb_twihEntries)+'\n')
 log.write('WW Entries:--------'+str(wwihEntries)+'\n')
 log.write('WZ Entries:--------'+str(wzihEntries)+'\n')
 log.write('ZZ Entries:--------'+str(zzihEntries)+'\n')
 log.write('Drell-Yan Entries:-'+str(zihEntries)+'\n')
 if drawData:
  log.write('Data Entries:          '+str(dataihEntries)+'\n')
 log.write('---------------------------------------------\n')
 log.write('---------------------------------------------\n')
 log.write('DataCard Numbers\n')
 log.write('---------------------------\n')
 if drawData:
 log.write('Data Size:      '+str(dataihSize)+'\n')
 log.write('Wbb Size:       '+str(wbbnihSize+wbb1ihSize+wbb2ihSize+wbb3ihSize+wbb4ihSize)+'\n')
 log.write('Wcc Size:       '+str(wccnihSize+wcc1ihSize+wcc2ihSize+wcc3ihSize+wcc4ihSize)+'\n')
 log.write('TTbar Size:     '+str(ttbihSize)+'\n')
 log.write('T Size:         '+str(t_tihSize+t_sihSize)+'\n')
 log.write('Tbar Size:      '+str(tb_tihSize+tb_sihSize)+'\n')
 log.write('T_tW Size:      '+str(t_twihSize+tb_twihSize)+'\n')
 log.write('Drell-Yan Size: '+str(zihSize)+'\n')
 log.write('VV Size:        '+str(wwihSize+wzihSize+zzihSize)+'\n')
 log.write('QCD Size:       '+str(qhSize)+'\n')

 
 znh.Delete()    #Drell
 t_tnh.Delete()  #Single Top
 tb_tnh.Delete()
 t_snh.Delete()
 tb_snh.Delete()
 t_twnh.Delete()
 tb_twnh.Delete()
 wwnh.Delete()   #Diboson
 wznh.Delete()
 zznh.Delete()
 ttbnh.Delete()  #TTbar
 wnnh.Delete()   #W
 w1nh.Delete()
 w2nh.Delete()
 w3nh.Delete()
 w4nh.Delete()
 qh.Delete()
 zih.Delete()
 wwih.Delete()
 wzih.Delete()
 zzih.Delete()
 t_tih.Delete()
 tb_tih.Delete()
 t_sih.Delete()
 tb_sih.Delete()
 t_twih.Delete()
 tb_twih.Delete()
 ttbih.Delete()
 wlnih.Delete()
 wl1ih.Delete()
 wl2ih.Delete()
 wl3ih.Delete()
 wl4ih.Delete()
 wcnih.Delete()
 wc1ih.Delete()
 wc2ih.Delete()
 wc3ih.Delete()
 wc4ih.Delete()
 wccnih.Delete()
 wcc1ih.Delete()
 wcc2ih.Delete()
 wcc3ih.Delete()
 wcc4ih.Delete()
 wbbnih.Delete()
 wbb1ih.Delete()
 wbb2ih.Delete()
 wbb3ih.Delete()
 wbb4ih.Delete()
 
datanh.Delete()
print(".log written")
log.close()

outFile.Write()
print('')
print('Your File is here: '+path+extraName+'_'+leaf+'.root')
print('')
 
