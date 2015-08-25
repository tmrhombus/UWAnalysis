#CutNtuple.py
#Author: Aaron Levine, UW Madison
#Produces reduced ntuples, to speed up the analysis

from sys import argv, stdout, stderr
import ROOT
import math
#Returns the number of lines in the files
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

counter = 0

#define the file
dir='/afs/hep.wisc.edu/cms/tperry/Wbb_CMSSW_5_3_14_patch1/src/UWAnalysis/CRAB/MuNu/synch/2014ocbr24/'
fname = "list.txt"
numfiles = file_len(fname)
with open(fname) as f:
 for x in f:
  print "Reading " +dir+x
  if counter % 5 == 0: 
   print "Processed " + str(counter) + " out of " + str(numfiles) + " files"
  #get file of current ntuples from input directory
  x = x.rstrip()
  new_fname = "C1_"+x
  print "Writing "+new_fname
  ntuple_file = ROOT.TFile(dir+x)
  #ntuple_file_spot = 'New_Tree'
  ntuple_file_spot = 'muNuEventTree/eventTree'
  tree = ntuple_file.Get(ntuple_file_spot)
  tree.SetName("tree")
  print tree.GetEntries()

  noFJ = "( !(J3_pt>25 && abs(J3_eta)>2.4 && J3_idLooseJet) && !(J4_pt>25 && abs(J4_eta)>2.4 && J4_idLooseJet) && !(J5_pt>25 && abs(J5_eta)>2.4) && !(J6_pt>25 && abs(J6_eta)>2.4) && !(J7_pt>25 && abs(J7_eta)>2.4) && !(J8_pt>25 && abs(J8_eta)>2.4) )"
  no3J = "( !(J3_pt>25 && J3_idLooseJet) && !(J4_pt>25 && J4_idLooseJet))"
  #muonIso = "(muNuRelPFIsoDB_A_vec[0]<0.12)"
  muonIso = "(muNuRelPFIsoDB_A_vec[0]<0.12 && !muNuRelPFIsoDB_A_vec[1])"

  cut_str = "(( %s && HLT_IsoMu24_eta2p1_v_fired)&&((abs(muon_eta)<2.1 && muon_pt>30) && (nrMuLoose==1 && nrEle==0) && (J1_pt>25 && abs(J1_eta)<2.4 && J1_idLooseJet) && (J2_pt>25 && abs(J2_eta)<2.4 && J2_idLooseJet) && %s && %s ))"%(muonIso,no3J,noFJ)

  #cut_str = "((((muNuRelPFIsoDB_A_vec[0]<0.12)||(muNuRelPFIsoDB_A_vec[1]<0.12)) && HLT_IsoMu24_eta2p1_v_fired)&&((abs(muon_eta)<2.1 && muon_pt>30) && (nrMuLoose==1 && nrEle==0) && (J1_pt>25 && abs(J1_eta)<2.4 && J1_idLooseJet) && (J2_pt>25 && abs(J2_eta)<2.4 && J2_idLooseJet) && %s && %s ))"%(no3J,noFJ)
  #cut_str = "(((muNuRelPFIsoDB_A_vec[0]<0.12||muNuRelPFIsoDB_A_vec[1]<0.12) && HLT_IsoMu24_eta2p1_v_fired)&&((abs(muon_eta)<2.1 && muon_pt>30) && (nrMuLoose==1 && nrEle==0) && (J1_pt>25 && abs(J1_eta)<2.4 && J1_idLooseJet) && (J2_pt>25 && abs(J2_eta)<2.4 && J2_idLooseJet) && %s && %s && (mt_new>45)))"%(no3J,noFJ)
  #cut_str = "(((muNuRelPFIsoDB_A_vec[0]<0.12||muNuRelPFIsoDB_A_vec[1]<0.12) && HLT_IsoMu24_eta2p1_v_fired)&&((abs(muon_eta)<2.1 && muon_pt>30) && (nrMuLoose==1 && nrEle==0) && (J1_pt>25 && abs(J1_eta)<2.4 && J1_idLooseJet) && (J2_pt>25 && abs(J2_eta)<2.4 && J2_idLooseJet) && %s && %s && (J1_CSVbtag>0.898) && (J2_CSVbtag>0.898) && (mt_new>45)))"%(no3J,noFJ)

  Smalltree_file = ROOT.TFile(new_fname,"RECREATE")
  Smalltree_file.cd()
  new_ttree = ROOT.TTree("new_ttree","new_ttree")
  new_ttree = tree.CopyTree(cut_str)
  new_ttree.SetName("New_Tree")
  print new_ttree.GetEntries()
  tree.Delete()
  #new_ttree.Write("eventTree")
  Smalltree_file.Write()
  Smalltree_file.Close()
  
  counter = counter+1


