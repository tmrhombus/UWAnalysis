#!/usr/bin/env python
'''
Parameters to be read by makeHistos.py and makePlotRatio.py
Author: T.M.Perry
'''

def arams():
 lumi = 19429.
 bNr = 2
 btype = 't'
 jNr = 2
 njetcut = '25' #20,25,26,30,40
 jetcut = '25'
 I = 0
 F = 20
 iso_value = 0.12
 antiIso_value = 0.2
 wSplitting = 'had'
 #wSplitting = 'par'

 drawQCD = True
 drawData = True

 jetVeto = True #use == instead of >=

 Control = True #one muon
 noMT = False # no mT cut
 Z_Region = False # two muons, no mT cut
 legacy = False #voids everything else and puts parametrs from 7Tev analysis

 drawW = False # line at W when plotting
 drawZ = False # line at Z when plotting

 #naming where output goes
 path = '../plots/'
 fitrange = '_'+str(I)+'_'+str(F)
 extraName = str(jNr)+'j'+njetcut+jetcut+'_'+str(bNr)+'b'+btype+'_newBTAG'

 jet1_2dr2 = '(((highestJetEta-secondJetEta)*(highestJetEta-secondJetEta))+((highestJetPhi-secondJetPhi)*(highestJetPhi-secondJetPhi)))'

 leafs = ['highestJetPt','highestJetEta','highestJetPhi','secondJetPt','secondJetEta','secondJetPhi']
 #leafs = ['secondJetPt','secondJetEta','secondJetPhi']
 #leafs = ['highestJetPt']
 #leafs = ['highestJetPt','highestJetEta','highestJetPhi']
 #leafs =['J1DR','J2DR']
 #leafs=['muonPt']
 #leafs=['nJetsPt20']
 #leafs=['muonPt','muonEta','muonPhi']
 #leafs = ['DiMuonMass']
 
 #leafs = ['J1SVMassb',jet1_2dr2]
 #leafs = ['J2SVMassb']
 #leafs = ['J1SVMassb','J2SVMassb']

 #leafs = ['dz']
 #leafs = ['muonCharge']
 #leafs=['J1CSVbtag','J2CSVbtag']
 #leafs=['J1JetParton','J2JetParton']
 #leafs = ['LHEProduct']

 #leafs=['Mt','WPt','ptJJ','ht']
 #leafs=['Mt']

 #leafs = ['mJ3J4','thirdJetEta','thirdJetPhi','thirdJetPt']

 #leafs = ['MET','vertices']
 #leafs = ['vertices']

 #leafs = ['highestJetPt','highestJetEta','highestJetPhi','secondJetPt','secondJetEta','secondJetPhi','J1DR','J2DR','muonPt','muonEta','muonPhi','Mt']#,'WPt','ptJJ','ht','MET','vertices']
 #leafs = ['secondJetPt','secondJetEta','secondJetPhi','J1DR','J2DR','muonPt','Mt','WPt','ptJJ','ht','MET','vertices']

 return lumi,bNr,btype,jNr,njetcut,jetcut,I,F,iso_value,antiIso_value,path,extraName,leafs,drawW,drawZ,drawQCD,drawData,wSplitting,jetVeto,Control,Z_Region,legacy,noMT
