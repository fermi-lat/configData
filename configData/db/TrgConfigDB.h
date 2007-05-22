/** @class TrgConfigDB
    @author M. Kocian

    A simple DB class for TrgConfig

    $Id: TrgConfigDB.h,v 1.1 2007/04/02 20:23:15 kocian Exp $
*/
#ifndef TRGCONFIGDB_H
#define TRGCONFIGDB_H

#include "configData/gem/TrgConfig.h"
#include "configData/db/LatcDB.h"

class TrgConfigDB:public TrgConfig{
 public:
  /// Constructor with the DB interface implementation as the argument
  TrgConfigDB(LatcDB* lc);
  /// Virtual destructor
  virtual ~TrgConfigDB(){}
  /// Check if we need to parse a new object, parse it if necessary
  bool updateKey(const unsigned int key);
 protected:
  LatcDB* m_lc;
  unsigned m_key;
};
    
  
#endif
