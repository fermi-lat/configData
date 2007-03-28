//---------------------------------------------------------------------------
// File and Version Information:
//      $Id: TrgConditions.h,v 1.1.1.1 2007/03/19 23:21:39 kocian Exp $
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
/** @class TrgConditions
    @author M. Kocian

    Auxiliary class to define trigger conditions by name.
*/


#ifndef TRGCONDITIONS_HH
#define TRGCONDITIONS_HH

#define NCOND 8

class TrgConditions{
 
 public:
  enum pmt {PMTA,PMTB};
  enum conditions {ROI, TKR, CALlow, CALhigh, CNO, Periodic, Solicited, EXT};
  /// Return a string with the name of the condition
  static const char* condName(conditions i){
    switch(i){
    case ROI: return "ROI";
      break;
    case TKR: return "TKR";
      break;
    case CALlow: return "CALlow";
      break;
    case CALhigh: return "CALhigh";
      break;
    case CNO: return "CNO";
      break;
    case Periodic: return "Periodic";
      break;
    case Solicited:return "Solicited";
      break;
    case EXT: return "EXT";
      break;
    }  
    return "";
  }
  
};
#endif
