/********************************
Instantiates histoFiller.C with
the correct chain and naming
for a definable set of parameters

Usage: 
root -l -b
.L PSANDSHIFT_callHistoFiller.cc
PSANDSHIFT_callHistoFiller()

root -l -b -q PSANDSHIFT_callHistoFiller.cc

Author: T.M.Perry UW-Madison
********************************/

#include <TStyle.h>
#include <vector>
#include <TChain.h>
#include "TROOT.h"
#include "TSystem.h"
#include "TApplication.h"
#include <iostream>
#include <exception>

void PSANDSHIFT_callHistoFillerLLBF()
{
 int error = 0;
 gROOT->ProcessLine(".L histoFillerLLBF.C++", &error);
 if(error!=0){std::cerr<<"ERROR LOADING histoFillerLLBF.C"<<std::endl;}
 histoFillerLLBF m;

// TChain *chainDataEle    = new TChain("electronEventTree/eventTree");
// TChain *chainDataMu     = new TChain("muonEventTree/eventTree");
// TChain *theChain        = new TChain("muEleEventTree/eventTree");
// TChain *theChainJESUp   = new TChain("muEleEventTreeJetUp/eventTree");
// TChain *theChainJESDown = new TChain("muEleEventTreeJetDown/eventTree");
// TChain *theChainLESUp   = new TChain("muEleEventTreeMuonUp/eventTree");
// TChain *theChainLESDown = new TChain("muEleEventTreeMuonDown/eventTree");

 TString outfileName = getenv("OUTPUT");
 TString inputListName = getenv("INPUT");

 TChain *theChain = new TChain("TREENAME");

 // Define Sample Criteria
 UInt_t lumi_mu  = LUMIMU ;
 UInt_t lumi_ele = LUMIELE ;

 TString sample="PSNAME";
 UInt_t nrEvents = NREVENTS ;
 Float_t crossSec = CROSSSEC ;

 Bool_t isMC_ = ISMC ;
 Bool_t isW_ = ISW ;
 TString shift="SHIFT";

 std::cout<<"Sample = "<<sample<<std::endl; 
 std::cout<<"Shift = "<<shift<<std::endl; 

 std::vector<TString> infileName_dump;
  
 ifstream inputList;
 inputList.open(inputListName);
 if( !inputList.good() ) { 
   std::cerr << "Cannot open the file: \"" << inputListName+"\""<<std::endl;
   abort();
 }

 // OK we have the file!
 TString infileName = ""; 
 while( !inputList.eof() ) { 
  infileName="";
  inputList >> infileName;
  
  std::cout << "Output File Name: " << outfileName << std::endl;
  std::cout << "Input File Name: "  << infileName <<  std::endl;
 
  theChain->Add( infileName );

  infileName_dump.push_back(infileName);
 } //while !inputList.eof()
 m.Init(theChain, isMC_); 
 m.Loop( outfileName, shift, isMC_, isW_, lumi_mu, lumi_ele, nrEvents, crossSec); 
} // void PSANDSHIFT_callHistoFiller()

