/** @class LatcDBImplFile
    @author M. Kocian
    

    Implementation to retrieve a filename that was set previously to fit in with the DB interface

    $Id: LatcDBImplFile.h,v 1.1 2007/05/23 22:53:37 kocian Exp $
*/
#ifndef LATCDBIMPLFILE_H
#define LATCDBIMPLFILE_H

#include "configData/db/LatcDB.h"
#include <string>


class LatcDBImplFile:public LatcDB{
 public:
  /// Default constructor
  LatcDBImplFile();
  /// function to retrieve filename of type type given key key.
  const std::string getFilename(const char* type, unsigned key);
  /// function to retrieve the list of filenames
  const std::vector<std::string> getFilenameList(unsigned key);
  /// function to set the filename
  void setFilename(const std::string filename);
 private:
  std::string m_filename;
};

#endif
