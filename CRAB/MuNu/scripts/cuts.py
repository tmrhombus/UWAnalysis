#!/usr/bin/env python
'''
for Wbb analysis, input a few values and function outputs cut strings
Author: T.M.Perry UW-Madison
'''

def cutmaker(isolationValue=0.12,antiIsoValue=0.2,lumi=13498.,bnr=0,btype='t',jnr=2):
 
 Control = True
 Z_Region   = False
 
 njetPt = '20' #20,24,25,26,30,40
 jetPt = '20'

 trigger = '(HLT_IsoMu24_eta2p1_v_fired)'
 muon_selection = '(nMuons==1&&abs(muonEta)<2.1&&muonPt>25)'
 dimuon_selection = '(nMuons==2&&abs(muonEta)<2.1&&muonPt>25)'
 vertex = '(abs(dz)<0.5&&abs(l1DXY)<0.02)'
 twoJets = '(nJetsPt'+njetPt+' >= 2 && highestJetPt >'+jetPt+' && secondJetPt>'+jetPt+' && abs(highestJetEta)<2.5 && abs(secondJetEta)<2.5)'
 threeJets = '('+twoJets+'&& nJetsPt'+njetPt+' >= 3 && thirdJetPt > '+jetPt+' && abs(thirdJetEta)<2.5)'
 fourJets = '('+threeJets+'&& nJetsPt'+njetPt+' >= 4 && mJ3J4 > 0)'
 mt = '(Mt>50)'

 Skim='('+trigger+'&&'+muon_selection+'&&'+vertex+'&&'+mt+')'
 Iso='(lPFIsoDB<'+str(isolationValue)+')'
 NonIso ='(lPFIsoDB>='+str(antiIsoValue)+')'
 Z='('+trigger+'&&'+dimuon_selection+'&&'+vertex+')'

 trigEff = 0.98
 #trigEff= '(EffWEIGHTpt*EffWEIGHTtrigeta)'
 weight = '('+'weightFactor*'+str(lumi)+'*'+str(trigEff)+')'

 if btype == 'tight' or 't':
  bcut = 0.898
 if btype == 'medium' or 'med' or 'm':
  bcut = 0.679
 if btype == 'loose' or 'l':
  bcut = 0.244
  
 OneBtag='((J1CSVbtag>'+str(bcut)+')||(J2CSVbtag>'+str(bcut)+'))'
 TwoBtag='((J1CSVbtag>'+str(bcut)+')&&(J2CSVbtag>'+str(bcut)+'))'

 if Control:
  theCut = Skim
 elif Z_Region:
  theCut = Z
 else:
  print("\n\n In cuts.py, choose Control or Z_Region True\n\n")

 if bnr == 1:
  if btype == 'tight' or 't':
   beffWeight = 'EffWEIGHTCSVT'
  if btype == 'medium' or 'med' or 'm':
   beffWeight = 'EffWEIGHTCSVM'
  if btype == 'loose' or 'l':
   beffWeight = 'EffWEIGHTCSVL'
  theCut = '('+theCut+'&&'+OneBtag+')'
  weight = '('+weight+'*'+beffWeight+')'

 if bnr == 2:
  if btype == 'tight' or 't':
   beffWeight = 'EffWEIGHTCSVT2'
  if btype == 'medium' or 'med' or 'm':
   beffWeight = 'EffWEIGHTCSVM2'
  if btype == 'loose' or 'l':
   beffWeight = 'EffWEIGHTCSVL2'
  theCut = '('+theCut+'&&'+TwoBtag+')'
  weight = '('+weight+'*'+beffWeight+')'

 if jnr == 2:
  theCut = '('+theCut+'&&'+twoJets+')'
 if jnr >= 3:
  theCut = '('+theCut+'&&'+threeJets+')'
 if jnr == 4:
  theCut = '('+theCut+'&&'+fourJets+')'

 # for splitting up the W sample
 genB = '(nbHadrons>0)'
 genC = '((ncCands+ncbarCands)>0)'
 evenC = '(((ncCands+ncbarCands)%2)==0)'
 
 Wl = '((!'+genB+'&&!'+genC+'))'
 Wc = '((!'+genB+'&&'+genC+'&&!'+evenC+'))'
 Wcc = '((!'+genB+'&&'+genC+'&&'+evenC+'))'
 Wbb = '('+genB+')'

 cutDataNonIso  = '('+NonIso+'&&'+theCut+')' #Data Non Iso
 cutDataIso     = '('+Iso+'&&'+theCut+')'    #Data Iso
 cutMcNonIso    = '('+weight+'*('+NonIso+'&&'+theCut+'))' #MC Non Iso
 cutMcIso       = '('+weight+'*('+Iso+   '&&'+theCut+'))' #MC Iso
 cutMcWlNonIso  = '('+weight+'*('+NonIso+'&&'+theCut+'&&'+Wl+'))'
 cutMcWlIso     = '('+weight+'*('+Iso+   '&&'+theCut+'&&'+Wl+'))'
 cutMcWcNonIso  = '('+weight+'*('+NonIso+'&&'+theCut+'&&'+Wc+'))'
 cutMcWcIso     = '('+weight+'*('+Iso+   '&&'+theCut+'&&'+Wc+'))'
 cutMcWccNonIso = '('+weight+'*('+NonIso+'&&'+theCut+'&&'+Wcc+'))'
 cutMcWccIso    = '('+weight+'*('+Iso+   '&&'+theCut+'&&'+Wcc+'))'
 cutMcWbbNonIso = '('+weight+'*('+NonIso+'&&'+theCut+'&&'+Wbb+'))'
 cutMcWbbIso    = '('+weight+'*('+Iso+   '&&'+theCut+'&&'+Wbb+'))'
 return cutMcNonIso, cutMcIso, cutDataNonIso, cutDataIso, cutMcWlNonIso, cutMcWlIso, cutMcWcNonIso, cutMcWcIso, cutMcWccNonIso, cutMcWccIso, cutMcWbbNonIso, cutMcWbbIso

