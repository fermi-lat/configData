//---------------------------------------------------------------------------
// File and Version Information:
//      $Id: TrgConfig.cxx,v 1.1.1.1 2007/03/19 23:21:39 kocian Exp $
//
// Description:
//      A top level GEM configuration class 
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
#include "configData/gem/TrgConfig.h"


TrgConfig::TrgConfig(){}

// Reset the cached and output values
void TrgConfig::reset() {
  _twp.reset();
  _tpt.reset();
  _lut.reset();
  _tev.reset();
  _tdv.reset();
  _configuration.reset();
  _roi.reset();  
}

// Attach this value to a TTree
void TrgConfig::makeBranches(TTree& tree, const std::string& prefix) const {
  _twp.makeBranch(tree,prefix);
  _tpt.makeBranch(tree,prefix);
  _lut.makeBranch(tree,prefix);
  _tev.makeBranch(tree,prefix);
  _tdv.makeBranch(tree,prefix);
  _configuration.makeBranch(tree,prefix);
  _roi.makeBranch(tree,prefix);  
 
}

void TrgConfig::attach(TTree& tree, const std::string& prefix) const {
  _twp.attach(tree,prefix);
  _tpt.attach(tree,prefix);
  _lut.attach(tree,prefix);
  _tev.attach(tree,prefix);
  _tdv.attach(tree,prefix);
  _configuration.attach(tree,prefix);
  _roi.attach(tree,prefix);  
}
