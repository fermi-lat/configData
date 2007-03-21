//---------------------------------------------------------------------------
// File and Version Information:
//      $Id: TrgConfLUT.h,v 1.1.1.1 2007/03/19 23:21:39 kocian Exp $
//
// Description:
//      GEM LUT class
//
// Environment:
//      Software developed for GLAST.
//
// Author List:
//      Martin Kocian
//
// Copyright Information:
//      Copyright (C) 2005      Stanford Linear Accelerator Center
//
//---------------------------------------------------------------------------
#ifndef TRGCONFLUT_HH
#define TRGCONFLUT_HH
#include <string.h>
#include <iostream>
#include <vector>
#include "TrgConditions.h"

#include "configData/base/ConfigTuple.h"

// number of registers in LUT
#define NREG 32
// number of conditions per register
#define CONDSREG 8
// number of entries in LUT
#define NENTRIES NREG*CONDSREG
// number of bits per condition
#define NBITS 4
// mask one condition (NBITS bits high)
#define CONDMASK 0xf
//---------------

class TrgConfLUT: public ConfigBranch {

public:
  
  TrgConfLUT();
  int engineNumber(int i) const;
  std::vector<unsigned long> conditionsInEngine(int i) const;
  unsigned long reg(int i) const {if (i<NREG && i>=0)return _lut[i];
                                       else return 0;} 

  // Reset the cached and output values
  virtual void reset();
  // Attach this value to a TTree
  virtual void makeBranch(TTree& tree, const std::string& prefix) const;
  virtual void attach(TTree& tree, const std::string& prefix) const;    

private:
  friend class TrgConfigParser;
  void setEngineNumber(int i, int entry);
  void setRegister(int i, unsigned long r){if (i<NREG && i>=0)_lut[i]=r;}

  unsigned long _lut[NREG];
};
std::ostream& operator <<(std::ostream& os, const TrgConfLUT& tc);
#endif
