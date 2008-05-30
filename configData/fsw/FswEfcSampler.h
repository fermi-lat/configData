//---------------------------------------------------------------------------
// File and Version Information:
//      $Id: FswEfcSampler.h,v 1.3 2007/03/28 21:21:02 kocian Exp $
//
// Description:
//      A GEM ROI register class 
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
/** @class FswEfcSampler
    @author M. Kocian

    Class to hold GEM ROI information.
*/

#ifndef FSWEFCSAMPLER_HH
#define FSWEFCSAMPLER_HH

#include <iostream>
#include <vector>

#include "configData/base/ConfigTuple.h"

class FswEfcSampler: public ConfigBranch {

public:

  static FswEfcSampler* makeFromXmlFile(const char* fileName);

  static unsigned mapKey(unsigned lpaMode, unsigned handlerId);

public:
  /// Default constructor
  FswEfcSampler();
  /// Clear data contents
  void clear();

  /// 
  inline unsigned prescaler(unsigned line) const { return m_prescalers[line]; }
  ///
  inline unsigned inputPrescaler() const { return m_inputPrescaler; }
  ///
  inline unsigned outputPrescaler() const { return m_outputPrescaler; }
  ///
  inline unsigned enabled() const { return m_enabled; }
  ///

  void set(unsigned prescalers[32], unsigned input, unsigned output, unsigned enabled);

  /// Reset the cached and output values
  virtual void reset() { clear() ;}
  /// Attach this value to a TTree
  virtual void makeBranch(TTree& tree, const std::string& prefix) const;
  virtual void attach(TTree& tree, const std::string& prefix) const;  
private:
  unsigned m_prescalers[32];
  unsigned m_inputPrescaler;
  unsigned m_outputPrescaler;
  unsigned m_enabled;
}; 
#endif
/// Printout Function
std::ostream& operator <<(std::ostream& os, const FswEfcSampler& tc);
