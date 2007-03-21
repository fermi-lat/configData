//---------------------------------------------------------------------------
// File and Version Information:
//      $Id: TrgDisabledChannels.h,v 1.1.1.1 2007/03/19 23:21:39 kocian Exp $
//
// Description:
//      Disabled channels in GEM configuration
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

#ifndef TRGDISABLEDCHANNELS_HH
#define TRGDISABLEDCHANNELS_HH

#include <vector>
#include <iostream>
#include "TrgConditions.h"
#include "configData/base/ConfigTuple.h"

class TrgDisabledChannels : public ConfigBranch {

public:
  TrgDisabledChannels();
  void clear();
  void setTowerRegister(unsigned i,unsigned val);
  unsigned towerRegister(unsigned i);
  void setTileRegister(unsigned i, unsigned val);
  unsigned tileRegister(unsigned i);
  void setCnoRegister(unsigned val);
  unsigned cnoRegister(){return _cno;}
  void setBusyRegister(unsigned val);
  unsigned busyRegister(){return _busy;}
  void setExternal(unsigned val);
  const bool externalEnabled() const{return _external;}
  void setTowerMask(unsigned tower, unsigned mask);
  const unsigned towerMask(unsigned tower) const;
  void setCalLowEnable(unsigned tower, bool on);
  void setCalHighEnable(unsigned tower, bool on);
  void setTkrEnable(unsigned tower, bool on);
  const bool calLowEnabled(unsigned tower) const;
  const bool calHighEnabled(unsigned tower) const;
  const bool tkrEnabled(unsigned tower) const;
  void setBusyFlag(unsigned tower, bool on);
  const bool busyFlagEnabled(unsigned tower) const;
  void setTileEnableByIndex(unsigned tile, TrgConditions::pmt pmt, bool on);
  const bool tileEnabledByIndex(unsigned tile,TrgConditions::pmt pmt) const;
  void setTileEnableByName(unsigned tile, TrgConditions::pmt pmt, bool on);
  const bool tileEnabledByName(unsigned tile,TrgConditions::pmt pmt) const;
  
  // Reset the cached and output values
  virtual void reset() { clear() ;}
  // Attach this value to a TTree
  virtual void makeBranch(TTree& tree, const std::string& prefix) const;
  virtual void attach(TTree& tree, const std::string& prefix) const;

private:
  
  unsigned _towers[4];
  unsigned _tiles[12];
  unsigned _cno;
  unsigned _busy;
  bool _external;

  friend class TrgConfigParser;
};

std::ostream& operator <<(std::ostream& os, const TrgDisabledChannels& tc);
std::ostream& operator <<(std::ostream& os, const TrgDisabledChannels* tc);


#endif
