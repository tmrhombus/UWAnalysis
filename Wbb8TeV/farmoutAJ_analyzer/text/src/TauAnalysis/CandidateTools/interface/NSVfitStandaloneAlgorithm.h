#ifndef TauAnalysis_CandidateTools_NSVfitStandaloneAlgorithm_h
#define TauAnalysis_CandidateTools_NSVfitStandaloneAlgorithm_h

#include "TauAnalysis/CandidateTools/interface/NSVfitStandaloneLikelihood.h"

#include <TMath.h>

using NSVfitStandalone::Vector;
using NSVfitStandalone::LorentzVector;
using NSVfitStandalone::MeasuredTauLepton;

/**
   \class   ObjectFunctionAdapter NSVfitStandaloneAlgorithm.h "TauAnalysis/CandidateTools/interface/NSVfitStandaloneAlgorithm.h"
   
   \brief   Function interface to minuit.
   
   This class is an interface of the global function pointer of the combined likelihood as defined in src/NSVfitStandaloneLikelihood.cc
   to minuit. It is a member of the of the NSVfitStandaloneAlgorithm class defined below and is used in NSVfitStandalone::fit(), where 
   it is passed on to a ROOT::Mathh::Functor. The parameters x correspond to the array of fit paramters as defined in 
   interface/NSVfitStandaloneLikelihood.h of this package. These are made known to minuit in the NSVfitStandaloneAlgorithm::setup 
   function.
*/

namespace NSVfitStandalone{
  class ObjectiveFunctionAdapter
  {
  public:
    double operator()(const double* x) const // function to be called in "fit" (MINUIT) mode
                                             // NOTE: return value = -log(likelihood)
    {
      double prob = NSVfitStandaloneLikelihood::gNSVfitStandaloneLikelihood->prob(x);
      double nll;
      if ( prob > 0. ) nll = -TMath::Log(prob);
      else nll = std::numeric_limits<float>::max();
      return nll;
    }
    double Eval(const double* x) const // function to be called in "integration" (VEGAS) mode
                                       // NOTE: return value = likelihood, **not** -log(likelihood)
    {
      double prob = NSVfitStandaloneLikelihood::gNSVfitStandaloneLikelihood->probint(x, mtest, par);      
      if ( TMath::IsNaN(prob) ) prob = 0.;
      return prob;
    }
    void SetPar(int parr) { par = parr; }
    void SetM(double m) { mtest = m; }
  private:
    int par;      //final state type
    double mtest; //current mass hypothesis
  };
}

/**
   \class   NSVfitStandaloneAlgorithm NSVfitStandaloneAlgorithm.h "TauAnalysis/CandidateTools/interface/NSVfitStandaloneAlgorithm.h"
   
   \brief   Standalone version of the NSVfitAlgorithm.

   This class is a standalone version of the NSVfitAlgorithm to perform the full reconstruction of a di-tau resonance system. 
   The implementation is supposed to deal with any combination of leptonic or hadronic tau decays. It exploits likelihood 
   functions as defined in interface/LikelihoodFunctions.h of this package, which are combined into a single likelihood 
   function as defined interface/NSVfitStandaloneLikelihood.h in this package. The combined likelihood function depends on 
   the following variables: 

   \var nunuMass : the invariant mass of the neutrino system for each decay branch (two parameters)
   \var decayAngle : the decay angle in the restframe of each decay branch (two parameters)
   \var visMass : the mass of the visible component of the di-tau system (two parameters)

   The actual fit parameters are:

   \var nunuMass : the invariant mass of the neutrino system for each decay branch (two parameters)
   \var xFrac : the fraction of the visible energy on the energy of the tau lepton in the labframe (two parameters)
   \var phi : the azimuthal angle of the tau lepton (two parameters)

   The azimuthal angle of each tau lepton is not constraint by measurement. It is limited to the physical values from -Math::Phi 
   to Math::Phi in the likelihood function nll of the combined likelihood class. The parameter nunuMass is constraint to the tau
   lepton mass minus the mass of the visible part of the decay (which is itself constraint to values below the tau lepton mass) 
   in the setup functioh of this class. The parameter xFrac is constraint to values between 0. and 1. in the setup function of 
   this class. The invariant mass of the neutrino system is fixed to be zero for hadronic tau lepton decays as only one (tau-) 
   neutrino is involved in the decay then. The original number of free parameters of 6 is therefore reduced by one for each hadronic 
   tau decay within the resonance. All information about the negative log likelihood is stored in the NSVfitStandaloneLikelihood 
   class as defined in the same package. This class interfaces the combined likelihood to the ROOT::Math::Minuit minimization program. 
   It does setup/initialize the fit parameters as defined in interface/NSVfitStandaloneLikelihood.h in this package, initializes the 
   minimization procedure, executes the fit algorithm and returns the fit result. The fit result consists of the fully reconstructed 
   di-tau system from which also the invariant mass can be derived.

   The following optional parameters can be applied after initialization but before running the fit: 

   \var metPower : indicating an additional power to enhance the MET likelihood (default is 1.)
   \var addLogM : specifying whether to use the LogM penalty term or not (default is true)     
   \var maxObjFunctionCalls : the maximum of function calls before the minimization procedure is terminated (default is 5000)

   Common usage is: 
   
   // construct the class object from the minimal necesarry information
   NSVfitStandaloneAlgorithm algo(measuredTauLeptons, measuredMET, covMET);
   // apply customized configurations if wanted (examples are given below)
   //algo.maxObjFunctionCalls(10000);
   //algo.addLogM(false);
   //algo.metPower(0.5)
   // run the fit
   algo.fit();
   // retrieve the results upon success
   if(algo.isValidSolution()){
   std::cout << algo.mass();
   }
*/
class NSVfitStandaloneAlgorithm
{
 public:
  /// constructor from a minimal set of configurables
  NSVfitStandaloneAlgorithm(std::vector<MeasuredTauLepton> measuredTauLeptons, Vector measuredMET, const TMatrixD& covMET, unsigned int verbosity = 0);
  /// destructor
  ~NSVfitStandaloneAlgorithm();

  /// add an additional logM(tau,tau) term to the nll to suppress tails on M(tau,tau) (default is true)
  void addLogM(bool value) { nll_->addLogM(value); }
  /// modify the MET term in the nll by an additional power (default is 1.)
  void metPower(double value) { nll_->metPower(value); }
  /// maximum function calls after which to stop the minimization procedure (default is 5000)
  void maxObjFunctionCalls(double value) { maxObjFunctionCalls_ = value; }

  /// actual fit function to be called from outside
  void fit();

  //integration 
  void integrate();

  /// return status of minuit fit
  int fitStatus() { return fitStatus_; };
  /// return whether this is a valid solution or not
    /*    
	  0: Valid solution
	  1: Covariance matrix was made positive definite
	  2: Hesse matrix is invalid
	  3: Estimated distance to minimum (EDM) is above maximum
	  4: Reached maximum number of function calls before reaching convergence
	  5: Any other failure
    */
  bool isValidSolution() { return fitStatus_ == 0; };
  /// return mass of the fitted di-tau system 
  double mass() const { return fittedDiTauSystem().mass(); };
  /// return uncertainty on the mass of the fitted di-tau system
  double massUncert() const { return massUncert_; };
  
  // mtt mass, svfit integration
  double getMass() const {return mass_;};

  /// return 4-vectors of the fitted tau leptons
  std::vector<LorentzVector> fittedTauLeptons() const { return fittedTauLeptons_; }
  /// return 4-vectors of measured tau leptons
  std::vector<LorentzVector> measuredTauLeptons() const; 
  /// return 4-vector of the fitted di-tau system
  LorentzVector fittedDiTauSystem() const { return fittedTauLeptons_[0] + fittedTauLeptons_[1]; }
  /// return 4-vector of the measured di-tau system
  LorentzVector measuredDiTauSystem() const { return measuredTauLeptons()[0] + measuredTauLeptons()[1]; }
  /// return spacial vector of the fitted MET
  Vector fittedMET() const { return (fittedDiTauSystem().Vect() - measuredDiTauSystem().Vect()); }
  // return spacial vector of the measured MET
  Vector measuredMET() const { return nll_->measuredMET(); }

 private:
  /// setup the starting values for the minimization (default values for the fit parameters are taken from src/SVFitParameters.cc in the same package)
  void setup();

 private:
  /// return whether this is a valid solution or not
  int fitStatus_;
  /// verbosity level
  unsigned int verbosity_;
  /// stop minimization after a maximal number of function calls
  unsigned int maxObjFunctionCalls_;

  /// minuit instance 
  ROOT::Math::Minimizer* minimizer_;
  /// standalone combined likelihood
  NSVfitStandalone::NSVfitStandaloneLikelihood* nll_;
  /// needed to make the fit function callable from within minuit
  NSVfitStandalone::ObjectiveFunctionAdapter standaloneObjectiveFunctionAdapter_;
  
  double mass_;
  /// uncertainty of the fitted di-tau mass
  double massUncert_;
  /// fit result for each of the decay branches 
  std::vector<NSVfitStandalone::LorentzVector> fittedTauLeptons_;
};

inline
std::vector<NSVfitStandalone::LorentzVector> 
NSVfitStandaloneAlgorithm::measuredTauLeptons() const 
{ 
  std::vector<NSVfitStandalone::LorentzVector> measuredTauLeptons;
  measuredTauLeptons.push_back(nll_->measuredTauLeptons()[0].p4());
  measuredTauLeptons.push_back(nll_->measuredTauLeptons()[1].p4());
  return measuredTauLeptons; 
}

#endif
