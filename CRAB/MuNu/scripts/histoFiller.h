#ifndef histoFiller_h
#define histoFiller_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <iostream>

// classes stored in the TTree
#include <vector>

// for reading SFs
//#include "table.h" // I copied it to xxx/scripts/table.h
//#include "RecoTools/interface/table.h"
//#include "UWAnalysis/RecoTools/interface/table.h"
//#include "$CMSSW_BASE/src/UWAnalysis/RecoTools/interface/table.h"
//#include <table.h> 

class histoFiller {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

   // For Cuts
   Bool_t oneGoodMuon;
   Bool_t twoGoodMuons;
   Bool_t oneQCDMuon;
   Bool_t twoQCDMuons;
   Bool_t oneGoodElectron;
   Bool_t twoGoodElectrons;
   Bool_t oneQCDElectron;
   Bool_t twoQCDElectrons;
   Bool_t twoGoodLeptons;
   Bool_t twoQCDLeptons;
   Bool_t min2goodJs;
   Bool_t exactly2goodJs;
   Bool_t min2goodBJs;
   Bool_t exactly2goodBJs;
   Bool_t aGoodBJaFwdJ;
   Bool_t twoCs;
   Bool_t someCs;
   Bool_t someBs;
   Bool_t isWl;
   Bool_t isWc;
   Bool_t isWcc;
   Bool_t isWbb;

   //// For SFs
   //Float_t goodMu_pt; 
   //Float_t goodMu_eta; 
   //Float_t qcdMu_pt; 
   //Float_t qcdMu_eta; 
   //Float_t goodEle_pt; 
   //Float_t goodEle_eta; 
   //Float_t qcdEle_pt; 
   //Float_t qcdEle_eta; 

   //  table* SFtableMu_Id;  // tried as pointer and reference
   //  table* SFtableMu_Iso;
   //  table* SFtableMu_Trg;
   //  table* SFtableEle_IdIso;
   //  table* SFtableEle_Trg;

   Float_t SF_topBJ;
   Float_t SF_top2BJs;
   Float_t SF_top2BJs_errUp;
   Float_t SF_top2BJs_errDn;
   Float_t SF_CSVreweight;
   Float_t SF_IDIsoHLT;
   Float_t SF_IDIsoHLT_errUp;
   Float_t SF_IDIsoHLT_errDn;
   Float_t SF_IDIso; // tried Float_t, float, double
   Float_t SF_IDIso_errUp;
   Float_t SF_IDIso_errDn;
   Float_t weight;
   Float_t weight_CSVerrUp;
   Float_t weight_CSVerrDn;
   Float_t weight_EMuerrUp;
   Float_t weight_EMuerrDn;

   // histogram variables
   Float_t mt;
   Float_t lep_pt;
   Float_t lep_eta;
   Float_t lep_phi;
   Float_t dphiJJ;
   Float_t dRgoodJ1J2;

   // Declaration of leaf types
   UInt_t          EVENT;
   UInt_t          RUN;
   UInt_t          LUMI;
   Float_t         GBWeight;
   Float_t         J1_eta_gen_NoNu;
   Float_t         J1_phi_gen_NoNu;
   Float_t         J1_pt_gen_NoNu;
   Float_t         J2_eta_gen_NoNu;
   Float_t         J2_phi_gen_NoNu;
   Float_t         J2_pt_gen_NoNu;
   Float_t         J3_eta_gen_NoNu;
   Float_t         J3_phi_gen_NoNu;
   Float_t         J3_pt_gen_NoNu;
   Float_t         J4_eta_gen_NoNu;
   Float_t         J4_phi_gen_NoNu;
   Float_t         J4_pt_gen_NoNu;
   vector<double>  *SF_goodEle_IDIsoHLT;
   vector<double>  *SF_goodEle_IDIsoHLT_errDn;
   vector<double>  *SF_goodEle_IDIsoHLT_errUp;
   vector<double>  *SF_goodMu_IDIsoHLT;
   vector<double>  *SF_goodMu_IDIsoHLT_errDn;
   vector<double>  *SF_goodMu_IDIsoHLT_errUp;
   Float_t         SF_lumiWeightPU;
   Float_t         SF_qcdEle_IDIso;
   Float_t         SF_qcdEle_IDIsoHLT;
   Float_t         SF_qcdEle_IDIsoHLT_errDn;
   Float_t         SF_qcdEle_IDIsoHLT_errUp;
   Float_t         SF_qcdEle_IDIso_errDn;
   Float_t         SF_qcdEle_IDIso_errUp;
   Float_t         SF_qcdMu_IDIso;
   Float_t         SF_qcdMu_IDIsoHLT;
   Float_t         SF_qcdMu_IDIsoHLT_errDn;
   Float_t         SF_qcdMu_IDIsoHLT_errUp;
   Float_t         SF_qcdMu_IDIso_errDn;
   Float_t         SF_qcdMu_IDIso_errUp;
   Float_t         bCandidate1Eta;
   Float_t         bCandidate1Phi;
   Float_t         bCandidate1Pt;
   Float_t         bCandidate2Eta;
   Float_t         bCandidate2Phi;
   Float_t         bCandidate2Pt;
   Float_t         bCandidateBC1MASS;
   Float_t         bCandidateBC1nTracks;
   Float_t         bCandidateBC2MASS;
   Float_t         bCandidateBC2nTracks;
   Float_t         bCandidateBCDeltaR;
   Float_t         bCandidateBCEnergySum;
   Float_t         bCandidateBCGenEnergySum;
   Float_t         bCandidateBDeltaPHI;
   Float_t         bCandidateDeltaPhi;
   Float_t         bCandidateDeltaR;
   Float_t         bCandidateJet1BC1ETA;
   Float_t         bCandidateJet1BC1PHI;
   Float_t         bCandidateJet1BC1PT;
   Float_t         bCandidateJet1BC2ETA;
   Float_t         bCandidateJet1BC2PHI;
   Float_t         bCandidateJet1BC2PT;
   Float_t         bCandidateJet2BC1ETA;
   Float_t         bCandidateJet2BC1PHI;
   Float_t         bCandidateJet2BC1PT;
   Float_t         bCandidateJet2BC2ETA;
   Float_t         bCandidateJet2BC2PHI;
   Float_t         bCandidateJet2BC2PT;
   Float_t         bCandidateJet3BC1ETA;
   Float_t         bCandidateJet3BC1PHI;
   Float_t         bCandidateJet3BC1PT;
   Float_t         bCandidateJet3BC2ETA;
   Float_t         bCandidateJet3BC2PHI;
   Float_t         bCandidateJet3BC2PT;
   Float_t         bCandidateJet4BC1ETA;
   Float_t         bCandidateJet4BC1PHI;
   Float_t         bCandidateJet4BC1PT;
   Float_t         bCandidateJet4BC2ETA;
   Float_t         bCandidateJet4BC2PHI;
   Float_t         bCandidateJet4BC2PT;
   Float_t         bCandidatenBC;
   Float_t         bCandidatenJetAssociatedToBC;
   Float_t         bCandidatenJetAssociatedToBC1;
   Float_t         bCandidatenJetAssociatedToBC2;
   vector<double>  *bHadronsEta;
   vector<double>  *bHadronsPhi;
   vector<double>  *bHadronsPt;
   Float_t         fwdJ1_CSV;
   Float_t         fwdJ1_CSVreweight;
   Float_t         fwdJ1_SF_CSVM;
   Float_t         fwdJ1_SF_CSVM_errDn;
   Float_t         fwdJ1_SF_CSVM_errUp;
   Float_t         fwdJ1_SF_CSVT;
   Float_t         fwdJ1_SF_CSVT_errDn;
   Float_t         fwdJ1_SF_CSVT_errUp;
   Float_t         fwdJ1_eta;
   Float_t         fwdJ1_partonFlavour;
   Float_t         fwdJ1_phi;
   Float_t         fwdJ1_pt;
   Float_t         fwdJ2_CSV;
   Float_t         fwdJ2_CSVreweight;
   Float_t         fwdJ2_SF_CSVM;
   Float_t         fwdJ2_SF_CSVM_errDn;
   Float_t         fwdJ2_SF_CSVM_errUp;
   Float_t         fwdJ2_SF_CSVT;
   Float_t         fwdJ2_SF_CSVT_errDn;
   Float_t         fwdJ2_SF_CSVT_errUp;
   Float_t         fwdJ2_eta;
   Float_t         fwdJ2_partonFlavour;
   Float_t         fwdJ2_phi;
   Float_t         fwdJ2_pt;
   Int_t           genBs;
   Int_t           genCs;
   Int_t           genDs;
   Int_t           genSs;
   Int_t           genTbars;
   Int_t           genTs;
   Int_t           genUs;
   Int_t           genWs;
   vector<double>  *goodEle_charge_vec;
   vector<double>  *goodEle_eta_vec;
   vector<double>  *goodEle_phi_vec;
   vector<double>  *goodEle_pt_vec;
   Float_t         goodJ1_CSV;
   Float_t         goodJ1_CSVreweight;
   Float_t         goodJ1_SF_CSVM;
   Float_t         goodJ1_SF_CSVM_errDn;
   Float_t         goodJ1_SF_CSVM_errUp;
   Float_t         goodJ1_SF_CSVT;
   Float_t         goodJ1_SF_CSVT_errDn;
   Float_t         goodJ1_SF_CSVT_errUp;
   Float_t         goodJ1_eta;
   Float_t         goodJ1_partonFlavour;
   Float_t         goodJ1_phi;
   Float_t         goodJ1_pt;
   Float_t         goodJ2_CSV;
   Float_t         goodJ2_CSVreweight;
   Float_t         goodJ2_SF_CSVM;
   Float_t         goodJ2_SF_CSVM_errDn;
   Float_t         goodJ2_SF_CSVM_errUp;
   Float_t         goodJ2_SF_CSVT;
   Float_t         goodJ2_SF_CSVT_errDn;
   Float_t         goodJ2_SF_CSVT_errUp;
   Float_t         goodJ2_eta;
   Float_t         goodJ2_partonFlavour;
   Float_t         goodJ2_phi;
   Float_t         goodJ2_pt;
   Float_t         goodJ3_CSV;
   Float_t         goodJ3_CSVreweight;
   Float_t         goodJ3_SF_CSVM;
   Float_t         goodJ3_SF_CSVM_errDn;
   Float_t         goodJ3_SF_CSVM_errUp;
   Float_t         goodJ3_SF_CSVT;
   Float_t         goodJ3_SF_CSVT_errDn;
   Float_t         goodJ3_SF_CSVT_errUp;
   Float_t         goodJ3_eta;
   Float_t         goodJ3_partonFlavour;
   Float_t         goodJ3_phi;
   Float_t         goodJ3_pt;
   Float_t         goodJ4_CSV;
   Float_t         goodJ4_CSVreweight;
   Float_t         goodJ4_SF_CSVM;
   Float_t         goodJ4_SF_CSVM_errDn;
   Float_t         goodJ4_SF_CSVM_errUp;
   Float_t         goodJ4_SF_CSVT;
   Float_t         goodJ4_SF_CSVT_errDn;
   Float_t         goodJ4_SF_CSVT_errUp;
   Float_t         goodJ4_eta;
   Float_t         goodJ4_partonFlavour;
   Float_t         goodJ4_phi;
   Float_t         goodJ4_pt;
   vector<double>  *goodMu_charge_vec;
   vector<double>  *goodMu_eta_vec;
   vector<double>  *goodMu_phi_vec;
   vector<double>  *goodMu_pt_vec;
   Float_t         met_eesDn_phi;
   Float_t         met_eesDn_pt;
   Float_t         met_eesUp_phi;
   Float_t         met_eesUp_pt;
   Float_t         met_jesDn_phi;
   Float_t         met_jesDn_pt;
   Float_t         met_jesUp_phi;
   Float_t         met_jesUp_pt;
   Float_t         met_eta;
   Float_t         met_pt;
   Float_t         met_uesDn_phi;
   Float_t         met_uesDn_pt;
   Float_t         met_uesUp_phi;
   Float_t         met_uesUp_pt;
   Float_t         mt_goodElectron;
   Float_t         mt_goodElectron_eesDn;
   Float_t         mt_goodElectron_eesUp;
   Float_t         mt_goodElectron_jesDn;
   Float_t         mt_goodElectron_jesUp;
   Float_t         mt_goodElectron_uesDn;
   Float_t         mt_goodElectron_uesUp;
   Float_t         mt_goodMuon;
   Float_t         mt_goodMuon_eesDn;
   Float_t         mt_goodMuon_eesUp;
   Float_t         mt_goodMuon_jesDn;
   Float_t         mt_goodMuon_jesUp;
   Float_t         mt_goodMuon_uesDn;
   Float_t         mt_goodMuon_uesUp;
   Float_t         mt_qcdElectron;
   Float_t         mt_qcdElectron_eesDn;
   Float_t         mt_qcdElectron_eesUp;
   Float_t         mt_qcdElectron_jesDn;
   Float_t         mt_qcdElectron_jesUp;
   Float_t         mt_qcdElectron_uesDn;
   Float_t         mt_qcdElectron_uesUp;
   Float_t         mt_qcdMuon;
   Float_t         mt_qcdMuon_eesDn;
   Float_t         mt_qcdMuon_eesUp;
   Float_t         mt_qcdMuon_jesDn;
   Float_t         mt_qcdMuon_jesUp;
   Float_t         mt_qcdMuon_uesDn;
   Float_t         mt_qcdMuon_uesUp;
   Int_t           LHEProduct;
   Int_t           nbHadrons;
   Int_t           nrAllEle;
   Int_t           nrAllJets;
   Int_t           nrAllMu;
   Int_t           nrCleanJets;
   Int_t           nrFwdJets;
   Int_t           nrGoodEle;
   Int_t           nrGoodJets;
   Int_t           nrGoodMu;
   Int_t           nrQCDEle;
   Int_t           nrQCDMu;
   Int_t           nrVetoEle;
   Int_t           nrVetoMu;
   Float_t         puBXminus;
   Float_t         puTruth;
   Float_t         puBX0;
   Float_t         puBXplus;
   Float_t         qcdEle_charge;
   Float_t         qcdEle_eta;
   Float_t         qcdEle_phi;
   Float_t         qcdEle_pt;
   Float_t         qcdMu_charge;
   Float_t         qcdMu_eta;
   Float_t         qcdMu_phi;
   Float_t         qcdMu_pt;
   Float_t         weightTop;
   Float_t         topPt;
   Float_t         antitopPt;
   Int_t           HLT_IsoMu24_eta2p1_v_wasRun;
   Int_t           HLT_IsoMu24_eta2p1_v_fired;
   Int_t           HLT_IsoMu24_eta2p1_v_prescale;
   Int_t           HLT_IsoMu24_eta2p1_v_error;
   Int_t           HLT_Mu40_eta2p1_v_wasRun;
   Int_t           HLT_Mu40_eta2p1_v_fired;
   Int_t           HLT_Mu40_eta2p1_v_prescale;
   Int_t           HLT_Mu40_eta2p1_v_error;
   Int_t           HLT_Ele27_WP80_wasRun;
   Int_t           HLT_Ele27_WP80_fired;
   Int_t           HLT_Ele27_WP80_prescale;
   Int_t           HLT_Ele27_WP80_error;
   Int_t           HLT_Any;
   Int_t           vertices;
   Float_t         vetoEle_charge;
   Float_t         vetoEle_eta;
   Float_t         vetoEle_phi;
   Float_t         vetoEle_pt;
   Float_t         vetoMu_charge;
   Float_t         vetoMu_eta;
   Float_t         vetoMu_phi;
   Float_t         vetoMu_pt;

   // List of branches
   TBranch        *b_EVENT;   
   TBranch        *b_RUN;   
   TBranch        *b_LUMI;   
   TBranch        *b_GBWeight;   
   TBranch        *b_J1_eta_gen_NoNu;   
   TBranch        *b_J1_phi_gen_NoNu;   
   TBranch        *b_J1_pt_gen_NoNu;   
   TBranch        *b_J2_eta_gen_NoNu;   
   TBranch        *b_J2_phi_gen_NoNu;   
   TBranch        *b_J2_pt_gen_NoNu;   
   TBranch        *b_J3_eta_gen_NoNu;   
   TBranch        *b_J3_phi_gen_NoNu;   
   TBranch        *b_J3_pt_gen_NoNu;   
   TBranch        *b_J4_eta_gen_NoNu;   
   TBranch        *b_J4_phi_gen_NoNu;   
   TBranch        *b_J4_pt_gen_NoNu;   
   TBranch        *b_SF_goodEle_IDIsoHLT;   
   TBranch        *b_SF_goodEle_IDIsoHLT_errDn;   
   TBranch        *b_SF_goodEle_IDIsoHLT_errUp;   
   TBranch        *b_SF_goodMu_IDIsoHLT;   
   TBranch        *b_SF_goodMu_IDIsoHLT_errDn;   
   TBranch        *b_SF_goodMu_IDIsoHLT_errUp;   
   TBranch        *b_SF_lumiWeightPU;   
   TBranch        *b_SF_qcdEle_IDIso;   
   TBranch        *b_SF_qcdEle_IDIsoHLT;   
   TBranch        *b_SF_qcdEle_IDIsoHLT_errDn;   
   TBranch        *b_SF_qcdEle_IDIsoHLT_errUp;   
   TBranch        *b_SF_qcdEle_IDIso_errDn;   
   TBranch        *b_SF_qcdEle_IDIso_errUp;   
   TBranch        *b_SF_qcdMu_IDIso;   
   TBranch        *b_SF_qcdMu_IDIsoHLT;   
   TBranch        *b_SF_qcdMu_IDIsoHLT_errDn;   
   TBranch        *b_SF_qcdMu_IDIsoHLT_errUp;   
   TBranch        *b_SF_qcdMu_IDIso_errDn;   
   TBranch        *b_SF_qcdMu_IDIso_errUp;   
   TBranch        *b_bCandidate1Eta;   
   TBranch        *b_bCandidate1Phi;   
   TBranch        *b_bCandidate1Pt;   
   TBranch        *b_bCandidate2Eta;   
   TBranch        *b_bCandidate2Phi;   
   TBranch        *b_bCandidate2Pt;   
   TBranch        *b_bCandidateBC1MASS;   
   TBranch        *b_bCandidateBC1nTracks;   
   TBranch        *b_bCandidateBC2MASS;   
   TBranch        *b_bCandidateBC2nTracks;   
   TBranch        *b_bCandidateBCDeltaR;   
   TBranch        *b_bCandidateBCEnergySum;   
   TBranch        *b_bCandidateBCGenEnergySum;   
   TBranch        *b_bCandidateBDeltaPHI;   
   TBranch        *b_bCandidateDeltaPhi;   
   TBranch        *b_bCandidateDeltaR;   
   TBranch        *b_bCandidateJet1BC1ETA;   
   TBranch        *b_bCandidateJet1BC1PHI;   
   TBranch        *b_bCandidateJet1BC1PT;   
   TBranch        *b_bCandidateJet1BC2ETA;   
   TBranch        *b_bCandidateJet1BC2PHI;   
   TBranch        *b_bCandidateJet1BC2PT;   
   TBranch        *b_bCandidateJet2BC1ETA;   
   TBranch        *b_bCandidateJet2BC1PHI;   
   TBranch        *b_bCandidateJet2BC1PT;   
   TBranch        *b_bCandidateJet2BC2ETA;   
   TBranch        *b_bCandidateJet2BC2PHI;   
   TBranch        *b_bCandidateJet2BC2PT;   
   TBranch        *b_bCandidateJet3BC1ETA;   
   TBranch        *b_bCandidateJet3BC1PHI;   
   TBranch        *b_bCandidateJet3BC1PT;   
   TBranch        *b_bCandidateJet3BC2ETA;   
   TBranch        *b_bCandidateJet3BC2PHI;   
   TBranch        *b_bCandidateJet3BC2PT;   
   TBranch        *b_bCandidateJet4BC1ETA;   
   TBranch        *b_bCandidateJet4BC1PHI;   
   TBranch        *b_bCandidateJet4BC1PT;   
   TBranch        *b_bCandidateJet4BC2ETA;   
   TBranch        *b_bCandidateJet4BC2PHI;   
   TBranch        *b_bCandidateJet4BC2PT;   
   TBranch        *b_bCandidatenBC;   
   TBranch        *b_bCandidatenJetAssociatedToBC;   
   TBranch        *b_bCandidatenJetAssociatedToBC1;   
   TBranch        *b_bCandidatenJetAssociatedToBC2;   
   TBranch        *b_bHadronsEta;   
   TBranch        *b_bHadronsPhi;   
   TBranch        *b_bHadronsPt;   
   TBranch        *b_fwdJ1_CSV;   
   TBranch        *b_fwdJ1_CSVreweight;   
   TBranch        *b_fwdJ1_SF_CSVM;   
   TBranch        *b_fwdJ1_SF_CSVM_errDn;   
   TBranch        *b_fwdJ1_SF_CSVM_errUp;   
   TBranch        *b_fwdJ1_SF_CSVT;   
   TBranch        *b_fwdJ1_SF_CSVT_errDn;   
   TBranch        *b_fwdJ1_SF_CSVT_errUp;   
   TBranch        *b_fwdJ1_eta;   
   TBranch        *b_fwdJ1_partonFlavour;   
   TBranch        *b_fwdJ1_phi;   
   TBranch        *b_fwdJ1_pt;   
   TBranch        *b_fwdJ2_CSV;   
   TBranch        *b_fwdJ2_CSVreweight;   
   TBranch        *b_fwdJ2_SF_CSVM;   
   TBranch        *b_fwdJ2_SF_CSVM_errDn;   
   TBranch        *b_fwdJ2_SF_CSVM_errUp;   
   TBranch        *b_fwdJ2_SF_CSVT;   
   TBranch        *b_fwdJ2_SF_CSVT_errDn;   
   TBranch        *b_fwdJ2_SF_CSVT_errUp;   
   TBranch        *b_fwdJ2_eta;   
   TBranch        *b_fwdJ2_partonFlavour;   
   TBranch        *b_fwdJ2_phi;   
   TBranch        *b_fwdJ2_pt;   
   TBranch        *b_genBs;   
   TBranch        *b_genCs;   
   TBranch        *b_genDs;   
   TBranch        *b_genSs;   
   TBranch        *b_genTbars;   
   TBranch        *b_genTs;   
   TBranch        *b_genUs;   
   TBranch        *b_genWs;   
   TBranch        *b_goodEle_charge_vec;   
   TBranch        *b_goodEle_eta_vec;   
   TBranch        *b_goodEle_phi_vec;   
   TBranch        *b_goodEle_pt_vec;   
   TBranch        *b_goodJ1_CSV;   
   TBranch        *b_goodJ1_CSVreweight;   
   TBranch        *b_goodJ1_SF_CSVM;   
   TBranch        *b_goodJ1_SF_CSVM_errDn;   
   TBranch        *b_goodJ1_SF_CSVM_errUp;   
   TBranch        *b_goodJ1_SF_CSVT;   
   TBranch        *b_goodJ1_SF_CSVT_errDn;   
   TBranch        *b_goodJ1_SF_CSVT_errUp;   
   TBranch        *b_goodJ1_eta;   
   TBranch        *b_goodJ1_partonFlavour;   
   TBranch        *b_goodJ1_phi;   
   TBranch        *b_goodJ1_pt;   
   TBranch        *b_goodJ2_CSV;   
   TBranch        *b_goodJ2_CSVreweight;   
   TBranch        *b_goodJ2_SF_CSVM;   
   TBranch        *b_goodJ2_SF_CSVM_errDn;   
   TBranch        *b_goodJ2_SF_CSVM_errUp;   
   TBranch        *b_goodJ2_SF_CSVT;   
   TBranch        *b_goodJ2_SF_CSVT_errDn;   
   TBranch        *b_goodJ2_SF_CSVT_errUp;   
   TBranch        *b_goodJ2_eta;   
   TBranch        *b_goodJ2_partonFlavour;   
   TBranch        *b_goodJ2_phi;   
   TBranch        *b_goodJ2_pt;   
   TBranch        *b_goodJ3_CSV;   
   TBranch        *b_goodJ3_CSVreweight;   
   TBranch        *b_goodJ3_SF_CSVM;   
   TBranch        *b_goodJ3_SF_CSVM_errDn;   
   TBranch        *b_goodJ3_SF_CSVM_errUp;   
   TBranch        *b_goodJ3_SF_CSVT;   
   TBranch        *b_goodJ3_SF_CSVT_errDn;   
   TBranch        *b_goodJ3_SF_CSVT_errUp;   
   TBranch        *b_goodJ3_eta;   
   TBranch        *b_goodJ3_partonFlavour;   
   TBranch        *b_goodJ3_phi;   
   TBranch        *b_goodJ3_pt;   
   TBranch        *b_goodJ4_CSV;   
   TBranch        *b_goodJ4_CSVreweight;   
   TBranch        *b_goodJ4_SF_CSVM;   
   TBranch        *b_goodJ4_SF_CSVM_errDn;   
   TBranch        *b_goodJ4_SF_CSVM_errUp;   
   TBranch        *b_goodJ4_SF_CSVT;   
   TBranch        *b_goodJ4_SF_CSVT_errDn;   
   TBranch        *b_goodJ4_SF_CSVT_errUp;   
   TBranch        *b_goodJ4_eta;   
   TBranch        *b_goodJ4_partonFlavour;   
   TBranch        *b_goodJ4_phi;   
   TBranch        *b_goodJ4_pt;   
   TBranch        *b_goodMu_charge_vec;   
   TBranch        *b_goodMu_eta_vec;   
   TBranch        *b_goodMu_phi_vec;   
   TBranch        *b_goodMu_pt_vec;   
   TBranch        *b_met_eesDn_phi;   
   TBranch        *b_met_eesDn_pt;   
   TBranch        *b_met_eesUp_phi;   
   TBranch        *b_met_eesUp_pt;   
   TBranch        *b_met_jesDn_phi;   
   TBranch        *b_met_jesDn_pt;   
   TBranch        *b_met_jesUp_phi;   
   TBranch        *b_met_jesUp_pt;   
   TBranch        *b_met_eta;   
   TBranch        *b_met_pt;   
   TBranch        *b_met_uesDn_phi;   
   TBranch        *b_met_uesDn_pt;   
   TBranch        *b_met_uesUp_phi;   
   TBranch        *b_met_uesUp_pt;   
   TBranch        *b_mt_goodElectron;   
   TBranch        *b_mt_goodElectron_eesDn;   
   TBranch        *b_mt_goodElectron_eesUp;   
   TBranch        *b_mt_goodElectron_jesDn;   
   TBranch        *b_mt_goodElectron_jesUp;   
   TBranch        *b_mt_goodElectron_uesDn;   
   TBranch        *b_mt_goodElectron_uesUp;   
   TBranch        *b_mt_goodMuon;   
   TBranch        *b_mt_goodMuon_eesDn;   
   TBranch        *b_mt_goodMuon_eesUp;   
   TBranch        *b_mt_goodMuon_jesDn;   
   TBranch        *b_mt_goodMuon_jesUp;   
   TBranch        *b_mt_goodMuon_uesDn;   
   TBranch        *b_mt_goodMuon_uesUp;   
   TBranch        *b_mt_qcdElectron;   
   TBranch        *b_mt_qcdElectron_eesDn;   
   TBranch        *b_mt_qcdElectron_eesUp;   
   TBranch        *b_mt_qcdElectron_jesDn;   
   TBranch        *b_mt_qcdElectron_jesUp;   
   TBranch        *b_mt_qcdElectron_uesDn;   
   TBranch        *b_mt_qcdElectron_uesUp;   
   TBranch        *b_mt_qcdMuon;   
   TBranch        *b_mt_qcdMuon_eesDn;   
   TBranch        *b_mt_qcdMuon_eesUp;   
   TBranch        *b_mt_qcdMuon_jesDn;   
   TBranch        *b_mt_qcdMuon_jesUp;   
   TBranch        *b_mt_qcdMuon_uesDn;   
   TBranch        *b_mt_qcdMuon_uesUp;   
   TBranch        *b_LHEProduct;   
   TBranch        *b_nbHadrons;   
   TBranch        *b_nrAllEle;   
   TBranch        *b_nrAllJets;   
   TBranch        *b_nrAllMu;   
   TBranch        *b_nrCleanJets;   
   TBranch        *b_nrFwdJets;   
   TBranch        *b_nrGoodEle;   
   TBranch        *b_nrGoodJets;   
   TBranch        *b_nrGoodMu;   
   TBranch        *b_nrQCDEle;   
   TBranch        *b_nrQCDMu;   
   TBranch        *b_nrVetoEle;   
   TBranch        *b_nrVetoMu;   
   TBranch        *b_puBXminus;   
   TBranch        *b_puTruth;   
   TBranch        *b_puBX0;   
   TBranch        *b_puBXplus;   
   TBranch        *b_qcdEle_charge;   
   TBranch        *b_qcdEle_eta;   
   TBranch        *b_qcdEle_phi;   
   TBranch        *b_qcdEle_pt;   
   TBranch        *b_qcdMu_charge;   
   TBranch        *b_qcdMu_eta;   
   TBranch        *b_qcdMu_phi;   
   TBranch        *b_qcdMu_pt;   
   TBranch        *b_weightTop;   
   TBranch        *b_topPt;   
   TBranch        *b_antitopPt;   
   TBranch        *b_HLT_IsoMu24_eta2p1_v_wasRun;   
   TBranch        *b_HLT_IsoMu24_eta2p1_v_fired;   
   TBranch        *b_HLT_IsoMu24_eta2p1_v_prescale;   
   TBranch        *b_HLT_IsoMu24_eta2p1_v_error;   
   TBranch        *b_HLT_Mu40_eta2p1_v_wasRun;   
   TBranch        *b_HLT_Mu40_eta2p1_v_fired;   
   TBranch        *b_HLT_Mu40_eta2p1_v_prescale;   
   TBranch        *b_HLT_Mu40_eta2p1_v_error;   
   TBranch        *b_HLT_Ele27_WP80_wasRun;   
   TBranch        *b_HLT_Ele27_WP80_fired;   
   TBranch        *b_HLT_Ele27_WP80_prescale;   
   TBranch        *b_HLT_Ele27_WP80_error;   
   TBranch        *b_HLT_Any;   
   TBranch        *b_vertices;   
   TBranch        *b_vetoEle_charge;   
   TBranch        *b_vetoEle_eta;   
   TBranch        *b_vetoEle_phi;   
   TBranch        *b_vetoEle_pt;   
   TBranch        *b_vetoMu_charge;   
   TBranch        *b_vetoMu_eta;   
   TBranch        *b_vetoMu_phi;   
   TBranch        *b_vetoMu_pt; 

   histoFiller(TTree *tree=0, Bool_t isMC=kTRUE);
   virtual ~histoFiller();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree, Bool_t isMC);
   virtual void     Loop(TString outFileName, Bool_t isMu, Bool_t isMC, Bool_t isQCD,
    TString cutType, TString shift, Int_t jType, UInt_t luminosity, UInt_t nrEvents, Float_t crossSec);
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef histoFiller_cxx
histoFiller::histoFiller(TTree *tree, Bool_t isMC) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("/hdfs/store/user/tperry/NouvelleYear_TTbar_semi-MuEle-PATMC/MuEle-PATMC-patTuple_cfg-00277FF2-7B84-E211-9475-782BCB27B958.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("/hdfs/store/user/tperry/NouvelleYear_TTbar_semi-MuEle-PATMC/MuEle-PATMC-patTuple_cfg-00277FF2-7B84-E211-9475-782BCB27B958.root");
      }
      TDirectory * dir = (TDirectory*)f->Get("/hdfs/store/user/tperry/NouvelleYear_TTbar_semi-MuEle-PATMC/MuEle-PATMC-patTuple_cfg-00277FF2-7B84-E211-9475-782BCB27B958.root:/muEleEventTree");
      dir->GetObject("eventTree",tree);

   }
   Init(tree, isMC);
}

histoFiller::~histoFiller()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();

   //  delete SFtableMu_Id;
   //  delete SFtableMu_Iso;
   //  delete SFtableMu_Trg;
   //  delete SFtableEle_IdIso;
   //  delete SFtableEle_Trg;
   //  std::cout<<"We're actually deleting"<<std::endl;
}

Int_t histoFiller::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t histoFiller::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void histoFiller::Init(TTree *tree, Bool_t isMC)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   //  std::string base = std::getenv("CMSSW_BASE"); 
   //  SFtableMu_Id = new table(base+"/src/UWAnalysis/RecoTools/data/SF_muon_ID.txt"); 
   //  SFtableMu_Iso = new table(base+"/src/UWAnalysis/RecoTools/data/SF_muon_Iso.txt"); 
   //  SFtableMu_Trg = new table(base+"/src/UWAnalysis/RecoTools/data/SF_muon_HLT.txt"); 
   //  SFtableEle_IdIso = new table(base+"/src/UWAnalysis/RecoTools/data/SF_ele_IDIso.txt"); 
   //  SFtableEle_Trg = new table(base+"/src/UWAnalysis/RecoTools/data/SF_ele_HLT.txt");


   // Set object pointer
   SF_goodEle_IDIsoHLT = 0;
   SF_goodEle_IDIsoHLT_errDn = 0;
   SF_goodEle_IDIsoHLT_errUp = 0;
   SF_goodMu_IDIsoHLT = 0;
   SF_goodMu_IDIsoHLT_errDn = 0;
   SF_goodMu_IDIsoHLT_errUp = 0;
   bHadronsEta = 0;
   bHadronsPhi = 0;
   bHadronsPt = 0;
   goodEle_charge_vec = 0;
   goodEle_eta_vec = 0;
   goodEle_phi_vec = 0;
   goodEle_pt_vec = 0;
   goodMu_charge_vec = 0;
   goodMu_eta_vec = 0;
   goodMu_phi_vec = 0;
   goodMu_pt_vec = 0;
   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);
   fChain->SetBranchAddress("EVENT", &EVENT, &b_EVENT);
   fChain->SetBranchAddress("RUN", &RUN, &b_RUN);
   fChain->SetBranchAddress("LUMI", &LUMI, &b_LUMI);
   if( isMC ) {
    fChain->SetBranchAddress("GBWeight", &GBWeight, &b_GBWeight);
    fChain->SetBranchAddress("J1_eta_gen_NoNu", &J1_eta_gen_NoNu, &b_J1_eta_gen_NoNu);
    fChain->SetBranchAddress("J1_phi_gen_NoNu", &J1_phi_gen_NoNu, &b_J1_phi_gen_NoNu);
    fChain->SetBranchAddress("J1_pt_gen_NoNu", &J1_pt_gen_NoNu, &b_J1_pt_gen_NoNu);
    fChain->SetBranchAddress("J2_eta_gen_NoNu", &J2_eta_gen_NoNu, &b_J2_eta_gen_NoNu);
    fChain->SetBranchAddress("J2_phi_gen_NoNu", &J2_phi_gen_NoNu, &b_J2_phi_gen_NoNu);
    fChain->SetBranchAddress("J2_pt_gen_NoNu", &J2_pt_gen_NoNu, &b_J2_pt_gen_NoNu);
    fChain->SetBranchAddress("J3_eta_gen_NoNu", &J3_eta_gen_NoNu, &b_J3_eta_gen_NoNu);
    fChain->SetBranchAddress("J3_phi_gen_NoNu", &J3_phi_gen_NoNu, &b_J3_phi_gen_NoNu);
    fChain->SetBranchAddress("J3_pt_gen_NoNu", &J3_pt_gen_NoNu, &b_J3_pt_gen_NoNu);
    fChain->SetBranchAddress("J4_eta_gen_NoNu", &J4_eta_gen_NoNu, &b_J4_eta_gen_NoNu);
    fChain->SetBranchAddress("J4_phi_gen_NoNu", &J4_phi_gen_NoNu, &b_J4_phi_gen_NoNu);
    fChain->SetBranchAddress("J4_pt_gen_NoNu", &J4_pt_gen_NoNu, &b_J4_pt_gen_NoNu);
    fChain->SetBranchAddress("SF_goodEle_IDIsoHLT", &SF_goodEle_IDIsoHLT, &b_SF_goodEle_IDIsoHLT);
    fChain->SetBranchAddress("SF_goodEle_IDIsoHLT_errDn", &SF_goodEle_IDIsoHLT_errDn, &b_SF_goodEle_IDIsoHLT_errDn);
    fChain->SetBranchAddress("SF_goodEle_IDIsoHLT_errUp", &SF_goodEle_IDIsoHLT_errUp, &b_SF_goodEle_IDIsoHLT_errUp);
    fChain->SetBranchAddress("SF_goodMu_IDIsoHLT", &SF_goodMu_IDIsoHLT, &b_SF_goodMu_IDIsoHLT);
    fChain->SetBranchAddress("SF_goodMu_IDIsoHLT_errDn", &SF_goodMu_IDIsoHLT_errDn, &b_SF_goodMu_IDIsoHLT_errDn);
    fChain->SetBranchAddress("SF_goodMu_IDIsoHLT_errUp", &SF_goodMu_IDIsoHLT_errUp, &b_SF_goodMu_IDIsoHLT_errUp);
    fChain->SetBranchAddress("SF_lumiWeightPU", &SF_lumiWeightPU, &b_SF_lumiWeightPU);
    fChain->SetBranchAddress("SF_qcdEle_IDIso", &SF_qcdEle_IDIso, &b_SF_qcdEle_IDIso);
    fChain->SetBranchAddress("SF_qcdEle_IDIsoHLT", &SF_qcdEle_IDIsoHLT, &b_SF_qcdEle_IDIsoHLT);
    fChain->SetBranchAddress("SF_qcdEle_IDIsoHLT_errDn", &SF_qcdEle_IDIsoHLT_errDn, &b_SF_qcdEle_IDIsoHLT_errDn);
    fChain->SetBranchAddress("SF_qcdEle_IDIsoHLT_errUp", &SF_qcdEle_IDIsoHLT_errUp, &b_SF_qcdEle_IDIsoHLT_errUp);
    fChain->SetBranchAddress("SF_qcdEle_IDIso_errDn", &SF_qcdEle_IDIso_errDn, &b_SF_qcdEle_IDIso_errDn);
    fChain->SetBranchAddress("SF_qcdEle_IDIso_errUp", &SF_qcdEle_IDIso_errUp, &b_SF_qcdEle_IDIso_errUp);
    fChain->SetBranchAddress("SF_qcdMu_IDIso", &SF_qcdMu_IDIso, &b_SF_qcdMu_IDIso);
    fChain->SetBranchAddress("SF_qcdMu_IDIsoHLT", &SF_qcdMu_IDIsoHLT, &b_SF_qcdMu_IDIsoHLT);
    fChain->SetBranchAddress("SF_qcdMu_IDIsoHLT_errDn", &SF_qcdMu_IDIsoHLT_errDn, &b_SF_qcdMu_IDIsoHLT_errDn);
    fChain->SetBranchAddress("SF_qcdMu_IDIsoHLT_errUp", &SF_qcdMu_IDIsoHLT_errUp, &b_SF_qcdMu_IDIsoHLT_errUp);
    fChain->SetBranchAddress("SF_qcdMu_IDIso_errDn", &SF_qcdMu_IDIso_errDn, &b_SF_qcdMu_IDIso_errDn);
    fChain->SetBranchAddress("SF_qcdMu_IDIso_errUp", &SF_qcdMu_IDIso_errUp, &b_SF_qcdMu_IDIso_errUp);
   }
   fChain->SetBranchAddress("bCandidate1Eta", &bCandidate1Eta, &b_bCandidate1Eta);
   fChain->SetBranchAddress("bCandidate1Phi", &bCandidate1Phi, &b_bCandidate1Phi);
   fChain->SetBranchAddress("bCandidate1Pt", &bCandidate1Pt, &b_bCandidate1Pt);
   fChain->SetBranchAddress("bCandidate2Eta", &bCandidate2Eta, &b_bCandidate2Eta);
   fChain->SetBranchAddress("bCandidate2Phi", &bCandidate2Phi, &b_bCandidate2Phi);
   fChain->SetBranchAddress("bCandidate2Pt", &bCandidate2Pt, &b_bCandidate2Pt);
   fChain->SetBranchAddress("bCandidateBC1MASS", &bCandidateBC1MASS, &b_bCandidateBC1MASS);
   fChain->SetBranchAddress("bCandidateBC1nTracks", &bCandidateBC1nTracks, &b_bCandidateBC1nTracks);
   fChain->SetBranchAddress("bCandidateBC2MASS", &bCandidateBC2MASS, &b_bCandidateBC2MASS);
   fChain->SetBranchAddress("bCandidateBC2nTracks", &bCandidateBC2nTracks, &b_bCandidateBC2nTracks);
   fChain->SetBranchAddress("bCandidateBCDeltaR", &bCandidateBCDeltaR, &b_bCandidateBCDeltaR);
   fChain->SetBranchAddress("bCandidateBCEnergySum", &bCandidateBCEnergySum, &b_bCandidateBCEnergySum);
   fChain->SetBranchAddress("bCandidateBCGenEnergySum", &bCandidateBCGenEnergySum, &b_bCandidateBCGenEnergySum);
   fChain->SetBranchAddress("bCandidateBDeltaPHI", &bCandidateBDeltaPHI, &b_bCandidateBDeltaPHI);
   fChain->SetBranchAddress("bCandidateDeltaPhi", &bCandidateDeltaPhi, &b_bCandidateDeltaPhi);
   fChain->SetBranchAddress("bCandidateDeltaR", &bCandidateDeltaR, &b_bCandidateDeltaR);
   fChain->SetBranchAddress("bCandidateJet1BC1ETA", &bCandidateJet1BC1ETA, &b_bCandidateJet1BC1ETA);
   fChain->SetBranchAddress("bCandidateJet1BC1PHI", &bCandidateJet1BC1PHI, &b_bCandidateJet1BC1PHI);
   fChain->SetBranchAddress("bCandidateJet1BC1PT", &bCandidateJet1BC1PT, &b_bCandidateJet1BC1PT);
   fChain->SetBranchAddress("bCandidateJet1BC2ETA", &bCandidateJet1BC2ETA, &b_bCandidateJet1BC2ETA);
   fChain->SetBranchAddress("bCandidateJet1BC2PHI", &bCandidateJet1BC2PHI, &b_bCandidateJet1BC2PHI);
   fChain->SetBranchAddress("bCandidateJet1BC2PT", &bCandidateJet1BC2PT, &b_bCandidateJet1BC2PT);
   fChain->SetBranchAddress("bCandidateJet2BC1ETA", &bCandidateJet2BC1ETA, &b_bCandidateJet2BC1ETA);
   fChain->SetBranchAddress("bCandidateJet2BC1PHI", &bCandidateJet2BC1PHI, &b_bCandidateJet2BC1PHI);
   fChain->SetBranchAddress("bCandidateJet2BC1PT", &bCandidateJet2BC1PT, &b_bCandidateJet2BC1PT);
   fChain->SetBranchAddress("bCandidateJet2BC2ETA", &bCandidateJet2BC2ETA, &b_bCandidateJet2BC2ETA);
   fChain->SetBranchAddress("bCandidateJet2BC2PHI", &bCandidateJet2BC2PHI, &b_bCandidateJet2BC2PHI);
   fChain->SetBranchAddress("bCandidateJet2BC2PT", &bCandidateJet2BC2PT, &b_bCandidateJet2BC2PT);
   fChain->SetBranchAddress("bCandidateJet3BC1ETA", &bCandidateJet3BC1ETA, &b_bCandidateJet3BC1ETA);
   fChain->SetBranchAddress("bCandidateJet3BC1PHI", &bCandidateJet3BC1PHI, &b_bCandidateJet3BC1PHI);
   fChain->SetBranchAddress("bCandidateJet3BC1PT", &bCandidateJet3BC1PT, &b_bCandidateJet3BC1PT);
   fChain->SetBranchAddress("bCandidateJet3BC2ETA", &bCandidateJet3BC2ETA, &b_bCandidateJet3BC2ETA);
   fChain->SetBranchAddress("bCandidateJet3BC2PHI", &bCandidateJet3BC2PHI, &b_bCandidateJet3BC2PHI);
   fChain->SetBranchAddress("bCandidateJet3BC2PT", &bCandidateJet3BC2PT, &b_bCandidateJet3BC2PT);
   fChain->SetBranchAddress("bCandidateJet4BC1ETA", &bCandidateJet4BC1ETA, &b_bCandidateJet4BC1ETA);
   fChain->SetBranchAddress("bCandidateJet4BC1PHI", &bCandidateJet4BC1PHI, &b_bCandidateJet4BC1PHI);
   fChain->SetBranchAddress("bCandidateJet4BC1PT", &bCandidateJet4BC1PT, &b_bCandidateJet4BC1PT);
   fChain->SetBranchAddress("bCandidateJet4BC2ETA", &bCandidateJet4BC2ETA, &b_bCandidateJet4BC2ETA);
   fChain->SetBranchAddress("bCandidateJet4BC2PHI", &bCandidateJet4BC2PHI, &b_bCandidateJet4BC2PHI);
   fChain->SetBranchAddress("bCandidateJet4BC2PT", &bCandidateJet4BC2PT, &b_bCandidateJet4BC2PT);
   fChain->SetBranchAddress("bCandidatenBC", &bCandidatenBC, &b_bCandidatenBC);
   fChain->SetBranchAddress("bCandidatenJetAssociatedToBC", &bCandidatenJetAssociatedToBC, &b_bCandidatenJetAssociatedToBC);
   fChain->SetBranchAddress("bCandidatenJetAssociatedToBC1", &bCandidatenJetAssociatedToBC1, &b_bCandidatenJetAssociatedToBC1);
   fChain->SetBranchAddress("bCandidatenJetAssociatedToBC2", &bCandidatenJetAssociatedToBC2, &b_bCandidatenJetAssociatedToBC2);
   if( isMC ) {
    fChain->SetBranchAddress("bHadronsEta", &bHadronsEta, &b_bHadronsEta);
    fChain->SetBranchAddress("bHadronsPhi", &bHadronsPhi, &b_bHadronsPhi);
    fChain->SetBranchAddress("bHadronsPt", &bHadronsPt, &b_bHadronsPt);
   }
   fChain->SetBranchAddress("fwdJ1_CSV", &fwdJ1_CSV, &b_fwdJ1_CSV);
   fChain->SetBranchAddress("fwdJ1_CSVreweight", &fwdJ1_CSVreweight, &b_fwdJ1_CSVreweight);
   fChain->SetBranchAddress("fwdJ1_SF_CSVM", &fwdJ1_SF_CSVM, &b_fwdJ1_SF_CSVM);
   fChain->SetBranchAddress("fwdJ1_SF_CSVM_errDn", &fwdJ1_SF_CSVM_errDn, &b_fwdJ1_SF_CSVM_errDn);
   fChain->SetBranchAddress("fwdJ1_SF_CSVM_errUp", &fwdJ1_SF_CSVM_errUp, &b_fwdJ1_SF_CSVM_errUp);
   fChain->SetBranchAddress("fwdJ1_SF_CSVT", &fwdJ1_SF_CSVT, &b_fwdJ1_SF_CSVT);
   fChain->SetBranchAddress("fwdJ1_SF_CSVT_errDn", &fwdJ1_SF_CSVT_errDn, &b_fwdJ1_SF_CSVT_errDn);
   fChain->SetBranchAddress("fwdJ1_SF_CSVT_errUp", &fwdJ1_SF_CSVT_errUp, &b_fwdJ1_SF_CSVT_errUp);
   fChain->SetBranchAddress("fwdJ1_eta", &fwdJ1_eta, &b_fwdJ1_eta);
   fChain->SetBranchAddress("fwdJ1_partonFlavour", &fwdJ1_partonFlavour, &b_fwdJ1_partonFlavour);
   fChain->SetBranchAddress("fwdJ1_phi", &fwdJ1_phi, &b_fwdJ1_phi);
   fChain->SetBranchAddress("fwdJ1_pt", &fwdJ1_pt, &b_fwdJ1_pt);
   fChain->SetBranchAddress("fwdJ2_CSV", &fwdJ2_CSV, &b_fwdJ2_CSV);
   fChain->SetBranchAddress("fwdJ2_CSVreweight", &fwdJ2_CSVreweight, &b_fwdJ2_CSVreweight);
   fChain->SetBranchAddress("fwdJ2_SF_CSVM", &fwdJ2_SF_CSVM, &b_fwdJ2_SF_CSVM);
   fChain->SetBranchAddress("fwdJ2_SF_CSVM_errDn", &fwdJ2_SF_CSVM_errDn, &b_fwdJ2_SF_CSVM_errDn);
   fChain->SetBranchAddress("fwdJ2_SF_CSVM_errUp", &fwdJ2_SF_CSVM_errUp, &b_fwdJ2_SF_CSVM_errUp);
   fChain->SetBranchAddress("fwdJ2_SF_CSVT", &fwdJ2_SF_CSVT, &b_fwdJ2_SF_CSVT);
   fChain->SetBranchAddress("fwdJ2_SF_CSVT_errDn", &fwdJ2_SF_CSVT_errDn, &b_fwdJ2_SF_CSVT_errDn);
   fChain->SetBranchAddress("fwdJ2_SF_CSVT_errUp", &fwdJ2_SF_CSVT_errUp, &b_fwdJ2_SF_CSVT_errUp);
   fChain->SetBranchAddress("fwdJ2_eta", &fwdJ2_eta, &b_fwdJ2_eta);
   fChain->SetBranchAddress("fwdJ2_partonFlavour", &fwdJ2_partonFlavour, &b_fwdJ2_partonFlavour);
   fChain->SetBranchAddress("fwdJ2_phi", &fwdJ2_phi, &b_fwdJ2_phi);
   fChain->SetBranchAddress("fwdJ2_pt", &fwdJ2_pt, &b_fwdJ2_pt);
   if( isMC ) {
    fChain->SetBranchAddress("genBs", &genBs, &b_genBs);
    fChain->SetBranchAddress("genCs", &genCs, &b_genCs);
    fChain->SetBranchAddress("genDs", &genDs, &b_genDs);
    fChain->SetBranchAddress("genSs", &genSs, &b_genSs);
    fChain->SetBranchAddress("genTbars", &genTbars, &b_genTbars);
    fChain->SetBranchAddress("genTs", &genTs, &b_genTs);
    fChain->SetBranchAddress("genUs", &genUs, &b_genUs);
    fChain->SetBranchAddress("genWs", &genWs, &b_genWs);
   }
   fChain->SetBranchAddress("goodEle_charge_vec", &goodEle_charge_vec, &b_goodEle_charge_vec);
   fChain->SetBranchAddress("goodEle_eta_vec", &goodEle_eta_vec, &b_goodEle_eta_vec);
   fChain->SetBranchAddress("goodEle_phi_vec", &goodEle_phi_vec, &b_goodEle_phi_vec);
   fChain->SetBranchAddress("goodEle_pt_vec", &goodEle_pt_vec, &b_goodEle_pt_vec);
   fChain->SetBranchAddress("goodJ1_CSV", &goodJ1_CSV, &b_goodJ1_CSV);
   fChain->SetBranchAddress("goodJ1_CSVreweight", &goodJ1_CSVreweight, &b_goodJ1_CSVreweight);
   fChain->SetBranchAddress("goodJ1_SF_CSVM", &goodJ1_SF_CSVM, &b_goodJ1_SF_CSVM);
   fChain->SetBranchAddress("goodJ1_SF_CSVM_errDn", &goodJ1_SF_CSVM_errDn, &b_goodJ1_SF_CSVM_errDn);
   fChain->SetBranchAddress("goodJ1_SF_CSVM_errUp", &goodJ1_SF_CSVM_errUp, &b_goodJ1_SF_CSVM_errUp);
   fChain->SetBranchAddress("goodJ1_SF_CSVT", &goodJ1_SF_CSVT, &b_goodJ1_SF_CSVT);
   fChain->SetBranchAddress("goodJ1_SF_CSVT_errDn", &goodJ1_SF_CSVT_errDn, &b_goodJ1_SF_CSVT_errDn);
   fChain->SetBranchAddress("goodJ1_SF_CSVT_errUp", &goodJ1_SF_CSVT_errUp, &b_goodJ1_SF_CSVT_errUp);
   fChain->SetBranchAddress("goodJ1_eta", &goodJ1_eta, &b_goodJ1_eta);
   fChain->SetBranchAddress("goodJ1_partonFlavour", &goodJ1_partonFlavour, &b_goodJ1_partonFlavour);
   fChain->SetBranchAddress("goodJ1_phi", &goodJ1_phi, &b_goodJ1_phi);
   fChain->SetBranchAddress("goodJ1_pt", &goodJ1_pt, &b_goodJ1_pt);
   fChain->SetBranchAddress("goodJ2_CSV", &goodJ2_CSV, &b_goodJ2_CSV);
   fChain->SetBranchAddress("goodJ2_CSVreweight", &goodJ2_CSVreweight, &b_goodJ2_CSVreweight);
   fChain->SetBranchAddress("goodJ2_SF_CSVM", &goodJ2_SF_CSVM, &b_goodJ2_SF_CSVM);
   fChain->SetBranchAddress("goodJ2_SF_CSVM_errDn", &goodJ2_SF_CSVM_errDn, &b_goodJ2_SF_CSVM_errDn);
   fChain->SetBranchAddress("goodJ2_SF_CSVM_errUp", &goodJ2_SF_CSVM_errUp, &b_goodJ2_SF_CSVM_errUp);
   fChain->SetBranchAddress("goodJ2_SF_CSVT", &goodJ2_SF_CSVT, &b_goodJ2_SF_CSVT);
   fChain->SetBranchAddress("goodJ2_SF_CSVT_errDn", &goodJ2_SF_CSVT_errDn, &b_goodJ2_SF_CSVT_errDn);
   fChain->SetBranchAddress("goodJ2_SF_CSVT_errUp", &goodJ2_SF_CSVT_errUp, &b_goodJ2_SF_CSVT_errUp);
   fChain->SetBranchAddress("goodJ2_eta", &goodJ2_eta, &b_goodJ2_eta);
   fChain->SetBranchAddress("goodJ2_partonFlavour", &goodJ2_partonFlavour, &b_goodJ2_partonFlavour);
   fChain->SetBranchAddress("goodJ2_phi", &goodJ2_phi, &b_goodJ2_phi);
   fChain->SetBranchAddress("goodJ2_pt", &goodJ2_pt, &b_goodJ2_pt);
   fChain->SetBranchAddress("goodJ3_CSV", &goodJ3_CSV, &b_goodJ3_CSV);
   fChain->SetBranchAddress("goodJ3_CSVreweight", &goodJ3_CSVreweight, &b_goodJ3_CSVreweight);
   fChain->SetBranchAddress("goodJ3_SF_CSVM", &goodJ3_SF_CSVM, &b_goodJ3_SF_CSVM);
   fChain->SetBranchAddress("goodJ3_SF_CSVM_errDn", &goodJ3_SF_CSVM_errDn, &b_goodJ3_SF_CSVM_errDn);
   fChain->SetBranchAddress("goodJ3_SF_CSVM_errUp", &goodJ3_SF_CSVM_errUp, &b_goodJ3_SF_CSVM_errUp);
   fChain->SetBranchAddress("goodJ3_SF_CSVT", &goodJ3_SF_CSVT, &b_goodJ3_SF_CSVT);
   fChain->SetBranchAddress("goodJ3_SF_CSVT_errDn", &goodJ3_SF_CSVT_errDn, &b_goodJ3_SF_CSVT_errDn);
   fChain->SetBranchAddress("goodJ3_SF_CSVT_errUp", &goodJ3_SF_CSVT_errUp, &b_goodJ3_SF_CSVT_errUp);
   fChain->SetBranchAddress("goodJ3_eta", &goodJ3_eta, &b_goodJ3_eta);
   fChain->SetBranchAddress("goodJ3_partonFlavour", &goodJ3_partonFlavour, &b_goodJ3_partonFlavour);
   fChain->SetBranchAddress("goodJ3_phi", &goodJ3_phi, &b_goodJ3_phi);
   fChain->SetBranchAddress("goodJ3_pt", &goodJ3_pt, &b_goodJ3_pt);
   fChain->SetBranchAddress("goodJ4_CSV", &goodJ4_CSV, &b_goodJ4_CSV);
   fChain->SetBranchAddress("goodJ4_CSVreweight", &goodJ4_CSVreweight, &b_goodJ4_CSVreweight);
   fChain->SetBranchAddress("goodJ4_SF_CSVM", &goodJ4_SF_CSVM, &b_goodJ4_SF_CSVM);
   fChain->SetBranchAddress("goodJ4_SF_CSVM_errDn", &goodJ4_SF_CSVM_errDn, &b_goodJ4_SF_CSVM_errDn);
   fChain->SetBranchAddress("goodJ4_SF_CSVM_errUp", &goodJ4_SF_CSVM_errUp, &b_goodJ4_SF_CSVM_errUp);
   fChain->SetBranchAddress("goodJ4_SF_CSVT", &goodJ4_SF_CSVT, &b_goodJ4_SF_CSVT);
   fChain->SetBranchAddress("goodJ4_SF_CSVT_errDn", &goodJ4_SF_CSVT_errDn, &b_goodJ4_SF_CSVT_errDn);
   fChain->SetBranchAddress("goodJ4_SF_CSVT_errUp", &goodJ4_SF_CSVT_errUp, &b_goodJ4_SF_CSVT_errUp);
   fChain->SetBranchAddress("goodJ4_eta", &goodJ4_eta, &b_goodJ4_eta);
   fChain->SetBranchAddress("goodJ4_partonFlavour", &goodJ4_partonFlavour, &b_goodJ4_partonFlavour);
   fChain->SetBranchAddress("goodJ4_phi", &goodJ4_phi, &b_goodJ4_phi);
   fChain->SetBranchAddress("goodJ4_pt", &goodJ4_pt, &b_goodJ4_pt);
   fChain->SetBranchAddress("goodMu_charge_vec", &goodMu_charge_vec, &b_goodMu_charge_vec);
   fChain->SetBranchAddress("goodMu_eta_vec", &goodMu_eta_vec, &b_goodMu_eta_vec);
   fChain->SetBranchAddress("goodMu_phi_vec", &goodMu_phi_vec, &b_goodMu_phi_vec);
   fChain->SetBranchAddress("goodMu_pt_vec", &goodMu_pt_vec, &b_goodMu_pt_vec);
   fChain->SetBranchAddress("met_eta", &met_eta, &b_met_eta);
   fChain->SetBranchAddress("met_pt", &met_pt, &b_met_pt);
   fChain->SetBranchAddress("mt_goodElectron", &mt_goodElectron, &b_mt_goodElectron);
   fChain->SetBranchAddress("mt_goodMuon", &mt_goodMuon, &b_mt_goodMuon);
   fChain->SetBranchAddress("mt_qcdElectron", &mt_qcdElectron, &b_mt_qcdElectron);
   fChain->SetBranchAddress("mt_qcdMuon", &mt_qcdMuon, &b_mt_qcdMuon);
   if( isMC ) {
    fChain->SetBranchAddress("met_eesDn_phi", &met_eesDn_phi, &b_met_eesDn_phi);
    fChain->SetBranchAddress("met_eesDn_pt", &met_eesDn_pt, &b_met_eesDn_pt);
    fChain->SetBranchAddress("met_eesUp_phi", &met_eesUp_phi, &b_met_eesUp_phi);
    fChain->SetBranchAddress("met_eesUp_pt", &met_eesUp_pt, &b_met_eesUp_pt);
    fChain->SetBranchAddress("met_jesDn_phi", &met_jesDn_phi, &b_met_jesDn_phi);
    fChain->SetBranchAddress("met_jesDn_pt", &met_jesDn_pt, &b_met_jesDn_pt);
    fChain->SetBranchAddress("met_jesUp_phi", &met_jesUp_phi, &b_met_jesUp_phi);
    fChain->SetBranchAddress("met_jesUp_pt", &met_jesUp_pt, &b_met_jesUp_pt);
    fChain->SetBranchAddress("met_uesDn_phi", &met_uesDn_phi, &b_met_uesDn_phi);
    fChain->SetBranchAddress("met_uesDn_pt", &met_uesDn_pt, &b_met_uesDn_pt);
    fChain->SetBranchAddress("met_uesUp_phi", &met_uesUp_phi, &b_met_uesUp_phi);
    fChain->SetBranchAddress("met_uesUp_pt", &met_uesUp_pt, &b_met_uesUp_pt);
    fChain->SetBranchAddress("mt_goodElectron_eesDn", &mt_goodElectron_eesDn, &b_mt_goodElectron_eesDn);
    fChain->SetBranchAddress("mt_goodElectron_eesUp", &mt_goodElectron_eesUp, &b_mt_goodElectron_eesUp);
    fChain->SetBranchAddress("mt_goodElectron_jesDn", &mt_goodElectron_jesDn, &b_mt_goodElectron_jesDn);
    fChain->SetBranchAddress("mt_goodElectron_jesUp", &mt_goodElectron_jesUp, &b_mt_goodElectron_jesUp);
    fChain->SetBranchAddress("mt_goodElectron_uesDn", &mt_goodElectron_uesDn, &b_mt_goodElectron_uesDn);
    fChain->SetBranchAddress("mt_goodElectron_uesUp", &mt_goodElectron_uesUp, &b_mt_goodElectron_uesUp);
    fChain->SetBranchAddress("mt_goodMuon_eesDn", &mt_goodMuon_eesDn, &b_mt_goodMuon_eesDn);
    fChain->SetBranchAddress("mt_goodMuon_eesUp", &mt_goodMuon_eesUp, &b_mt_goodMuon_eesUp);
    fChain->SetBranchAddress("mt_goodMuon_jesDn", &mt_goodMuon_jesDn, &b_mt_goodMuon_jesDn);
    fChain->SetBranchAddress("mt_goodMuon_jesUp", &mt_goodMuon_jesUp, &b_mt_goodMuon_jesUp);
    fChain->SetBranchAddress("mt_goodMuon_uesDn", &mt_goodMuon_uesDn, &b_mt_goodMuon_uesDn);
    fChain->SetBranchAddress("mt_goodMuon_uesUp", &mt_goodMuon_uesUp, &b_mt_goodMuon_uesUp);
    fChain->SetBranchAddress("mt_qcdElectron_eesDn", &mt_qcdElectron_eesDn, &b_mt_qcdElectron_eesDn);
    fChain->SetBranchAddress("mt_qcdElectron_eesUp", &mt_qcdElectron_eesUp, &b_mt_qcdElectron_eesUp);
    fChain->SetBranchAddress("mt_qcdElectron_jesDn", &mt_qcdElectron_jesDn, &b_mt_qcdElectron_jesDn);
    fChain->SetBranchAddress("mt_qcdElectron_jesUp", &mt_qcdElectron_jesUp, &b_mt_qcdElectron_jesUp);
    fChain->SetBranchAddress("mt_qcdElectron_uesDn", &mt_qcdElectron_uesDn, &b_mt_qcdElectron_uesDn);
    fChain->SetBranchAddress("mt_qcdElectron_uesUp", &mt_qcdElectron_uesUp, &b_mt_qcdElectron_uesUp);
    fChain->SetBranchAddress("mt_qcdMuon_eesDn", &mt_qcdMuon_eesDn, &b_mt_qcdMuon_eesDn);
    fChain->SetBranchAddress("mt_qcdMuon_eesUp", &mt_qcdMuon_eesUp, &b_mt_qcdMuon_eesUp);
    fChain->SetBranchAddress("mt_qcdMuon_jesDn", &mt_qcdMuon_jesDn, &b_mt_qcdMuon_jesDn);
    fChain->SetBranchAddress("mt_qcdMuon_jesUp", &mt_qcdMuon_jesUp, &b_mt_qcdMuon_jesUp);
    fChain->SetBranchAddress("mt_qcdMuon_uesDn", &mt_qcdMuon_uesDn, &b_mt_qcdMuon_uesDn);
    fChain->SetBranchAddress("mt_qcdMuon_uesUp", &mt_qcdMuon_uesUp, &b_mt_qcdMuon_uesUp);
    fChain->SetBranchAddress("LHEProduct", &LHEProduct, &b_LHEProduct);
    fChain->SetBranchAddress("nbHadrons", &nbHadrons, &b_nbHadrons);
    fChain->SetBranchAddress("weightTop", &weightTop, &b_weightTop);
    fChain->SetBranchAddress("topPt", &topPt, &b_topPt);
    fChain->SetBranchAddress("antitopPt", &antitopPt, &b_antitopPt);
   }
   fChain->SetBranchAddress("nrAllEle", &nrAllEle, &b_nrAllEle);
   fChain->SetBranchAddress("nrAllJets", &nrAllJets, &b_nrAllJets);
   fChain->SetBranchAddress("nrAllMu", &nrAllMu, &b_nrAllMu);
   fChain->SetBranchAddress("nrCleanJets", &nrCleanJets, &b_nrCleanJets);
   fChain->SetBranchAddress("nrFwdJets", &nrFwdJets, &b_nrFwdJets);
   fChain->SetBranchAddress("nrGoodEle", &nrGoodEle, &b_nrGoodEle);
   fChain->SetBranchAddress("nrGoodJets", &nrGoodJets, &b_nrGoodJets);
   fChain->SetBranchAddress("nrGoodMu", &nrGoodMu, &b_nrGoodMu);
   fChain->SetBranchAddress("nrQCDEle", &nrQCDEle, &b_nrQCDEle);
   fChain->SetBranchAddress("nrQCDMu", &nrQCDMu, &b_nrQCDMu);
   fChain->SetBranchAddress("nrVetoEle", &nrVetoEle, &b_nrVetoEle);
   fChain->SetBranchAddress("nrVetoMu", &nrVetoMu, &b_nrVetoMu);
   fChain->SetBranchAddress("puBXminus", &puBXminus, &b_puBXminus);
   fChain->SetBranchAddress("puTruth", &puTruth, &b_puTruth);
   fChain->SetBranchAddress("puBX0", &puBX0, &b_puBX0);
   fChain->SetBranchAddress("puBXplus", &puBXplus, &b_puBXplus);
   fChain->SetBranchAddress("qcdEle_charge", &qcdEle_charge, &b_qcdEle_charge);
   fChain->SetBranchAddress("qcdEle_eta", &qcdEle_eta, &b_qcdEle_eta);
   fChain->SetBranchAddress("qcdEle_phi", &qcdEle_phi, &b_qcdEle_phi);
   fChain->SetBranchAddress("qcdEle_pt", &qcdEle_pt, &b_qcdEle_pt);
   fChain->SetBranchAddress("qcdMu_charge", &qcdMu_charge, &b_qcdMu_charge);
   fChain->SetBranchAddress("qcdMu_eta", &qcdMu_eta, &b_qcdMu_eta);
   fChain->SetBranchAddress("qcdMu_phi", &qcdMu_phi, &b_qcdMu_phi);
   fChain->SetBranchAddress("qcdMu_pt", &qcdMu_pt, &b_qcdMu_pt);
   fChain->SetBranchAddress("HLT_IsoMu24_eta2p1_v_wasRun", &HLT_IsoMu24_eta2p1_v_wasRun, &b_HLT_IsoMu24_eta2p1_v_wasRun);
   fChain->SetBranchAddress("HLT_IsoMu24_eta2p1_v_fired", &HLT_IsoMu24_eta2p1_v_fired, &b_HLT_IsoMu24_eta2p1_v_fired);
   fChain->SetBranchAddress("HLT_IsoMu24_eta2p1_v_prescale", &HLT_IsoMu24_eta2p1_v_prescale, &b_HLT_IsoMu24_eta2p1_v_prescale);
   fChain->SetBranchAddress("HLT_IsoMu24_eta2p1_v_error", &HLT_IsoMu24_eta2p1_v_error, &b_HLT_IsoMu24_eta2p1_v_error);
   fChain->SetBranchAddress("HLT_Mu40_eta2p1_v_wasRun", &HLT_Mu40_eta2p1_v_wasRun, &b_HLT_Mu40_eta2p1_v_wasRun);
   fChain->SetBranchAddress("HLT_Mu40_eta2p1_v_fired", &HLT_Mu40_eta2p1_v_fired, &b_HLT_Mu40_eta2p1_v_fired);
   fChain->SetBranchAddress("HLT_Mu40_eta2p1_v_prescale", &HLT_Mu40_eta2p1_v_prescale, &b_HLT_Mu40_eta2p1_v_prescale);
   fChain->SetBranchAddress("HLT_Mu40_eta2p1_v_error", &HLT_Mu40_eta2p1_v_error, &b_HLT_Mu40_eta2p1_v_error);
   fChain->SetBranchAddress("HLT_Ele27_WP80_wasRun", &HLT_Ele27_WP80_wasRun, &b_HLT_Ele27_WP80_wasRun);
   fChain->SetBranchAddress("HLT_Ele27_WP80_fired", &HLT_Ele27_WP80_fired, &b_HLT_Ele27_WP80_fired);
   fChain->SetBranchAddress("HLT_Ele27_WP80_prescale", &HLT_Ele27_WP80_prescale, &b_HLT_Ele27_WP80_prescale);
   fChain->SetBranchAddress("HLT_Ele27_WP80_error", &HLT_Ele27_WP80_error, &b_HLT_Ele27_WP80_error);
   fChain->SetBranchAddress("HLT_Any", &HLT_Any, &b_HLT_Any);
   fChain->SetBranchAddress("vertices", &vertices, &b_vertices);
   fChain->SetBranchAddress("vetoEle_charge", &vetoEle_charge, &b_vetoEle_charge);
   fChain->SetBranchAddress("vetoEle_eta", &vetoEle_eta, &b_vetoEle_eta);
   fChain->SetBranchAddress("vetoEle_phi", &vetoEle_phi, &b_vetoEle_phi);
   fChain->SetBranchAddress("vetoEle_pt", &vetoEle_pt, &b_vetoEle_pt);
   fChain->SetBranchAddress("vetoMu_charge", &vetoMu_charge, &b_vetoMu_charge);
   fChain->SetBranchAddress("vetoMu_eta", &vetoMu_eta, &b_vetoMu_eta);
   fChain->SetBranchAddress("vetoMu_phi", &vetoMu_phi, &b_vetoMu_phi);
   fChain->SetBranchAddress("vetoMu_pt", &vetoMu_pt, &b_vetoMu_pt);
   Notify();
}

Bool_t histoFiller::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void histoFiller::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t histoFiller::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   if (!fChain) return 0;
   fChain->Show(entry);
   return 1;
}
#endif // #ifdef histoFiller_cxx
