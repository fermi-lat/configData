#ifndef ConfigTuple_h
#define ConfigTuple_h 

//
// This File has basic interface for the monitoring values
//
//

//
// STL 
#include <string>
#include <list>
#include <map>

// ROOT
#include "Rtypes.h"


// Forward Declares
class TTree;

//
//
// Base class to ID channels
//
class ChannelKey {

public :

  enum { UNDEF = -2, BCAST = -1 };

public :
  
  // c'tor, default and copy
  inline ChannelKey(Int_t i0 = UNDEF, Int_t i1 = UNDEF, Int_t i2 = UNDEF, Int_t i3 = UNDEF):
    m_0(i0),m_1(i1),m_2(i2),m_3(i3){
  }
  inline ChannelKey(const ChannelKey& other)
    :m_0(other.index0()),m_1(other.index1()),m_2(other.index2()),m_3(other.index3()){
  }

  // D'tor, no-op
  inline ~ChannelKey(){
  }

  // get the indices
  inline Int_t index0() const { return m_0; }
  inline Int_t index1() const { return m_1; }
  inline Int_t index2() const { return m_2; }  
  inline Int_t index3() const { return m_3; }

  inline Bool_t singleton() const {
    return ( m_0 == 1 && m_1 == 1 && m_2 == 1 && m_3 == 1 );
  }

  // return true if any incides set to BCAST
  inline Bool_t hasBCAST() const {
    return (m_0 == BCAST || m_1 == BCAST || m_2 == BCAST || m_3 == BCAST );
  }

private:

  const Int_t m_0;
  const Int_t m_1;
  const Int_t m_2;
  const Int_t m_3;

};



//
// 
// Base class for Branches
//
class ConfigBranch {
    
public :
  
  // Standard c'tor, needs a name, this is where the data end up
  // on the output tree
  ConfigBranch(const char* name, const Char_t type, const ChannelKey& size)
    :m_name(name),m_type(type),m_size(size){}

  // D'tor, no-op
  virtual ~ConfigBranch(){
  }

  // Just return the name of this var
  inline const std::string& name() const { return m_name; }
  inline Char_t type() const { return m_type; }
  const ChannelKey& branchSize() const { return m_size; }

  // Reset the cached and output values
  virtual void reset() = 0;

  // Attach this value to a TTree
  virtual void makeBranch(TTree& tree, const std::string& prefix) const = 0;
  virtual void attach(TTree& tree, const std::string& prefix) const = 0;

protected:

  void setLeafSuffix(std::string& leafName) const;
  Int_t index(const ChannelKey& channel) const;

private:

  // The name of this register
  const std::string m_name;    
  const Char_t m_type;
  const ChannelKey m_size;

};

//
//
// Template to Build various types of channels
// Only need T = UShort_t, UInt_t, ULong64_t
//
template <typename T>
class ConfigBranchImpl : public ConfigBranch {
    
public :
  
  // Standard c'tor, needs a name, this is where the data end up
  // on the output tree
  ConfigBranchImpl(const char* name, const Char_t type, const ChannelKey& size) :ConfigBranch(name,type,size),m_vals(0){
    build();
    static ChannelKey nullKey(0); static T dummy;
    getVal(nullKey,dummy);
    setVal(nullKey,dummy);
  }

  // D'tor, no-op
  virtual ~ConfigBranchImpl(){
    if ( m_vals != 0 ) {
      delete [] m_vals;
    }
  }

  // Set a value
  inline void setVal(const ChannelKey& key, T val) {
    Int_t i = index(key);
    m_vals[i] = val;    
    ;
  }

  // Get a value
  inline void getVal(const ChannelKey& key, T& val) const {
  Int_t i = index(key);
  m_vals[i] = val;
}


  // Reset the cached and output values
  virtual void reset() {
    setAll(0);
  }

  void setAll(T val = 0) {
    Int_t idx = 0;
    m_bcast = val;
    for ( Int_t i(0); i < branchSize().index0(); i++ ) {    
      for ( Int_t j(0); j < branchSize().index1(); j++ ) {
	for ( Int_t k(0); k < branchSize().index2(); k++ ) {
	  for ( Int_t l(0); l < branchSize().index3(); l++ ) {    
	    m_vals[idx] = val;
	    idx++;
	  }    
	}    
      }
    }    
    ;
  }
  // Attach this value to a TTree
  virtual void makeBranch(TTree& tree, const std::string& prefix) const;
  virtual void attach(TTree& tree, const std::string& prefix) const;

protected:

  inline void build() {
    Int_t bSize = branchSize().index0() * branchSize().index1() * branchSize().index2() * branchSize().index3();
    m_vals = new T[bSize];
  }


private:

  // The name of this register
  T* m_vals;
  T  m_bcast;

};

class ConfigTuple {
  
public :
  
  // Standard c'tor, needs a name, this is where the data end up
  // on the output tree
  ConfigTuple(const char* name)
    :m_name(name){}

  // D'tor, no-op
  virtual ~ConfigTuple(){
  }

  // Just return the name of this tuple
  inline const std::string& name() const { return m_name; }

  // Reset the cached and output values
  void reset();

  // Attach this value to a TTree
  void makeBranches(TTree& tree, const std::string& prefix) const;
  void attach(TTree& tree, const std::string& prefix) const;

  // Add an new branch
  void addBranch(ConfigBranch& aBranch);

  // get a branch by name
  ConfigBranch* branch(const std::string& bname);

private:

  // The name of this tuple
  const std::string m_name;

  // The list and map of branches
  std::list<ConfigBranch*> m_branchList;           
  std::map<std::string,ConfigBranch*> m_branchMap;

};

#endif
