#!/bin/env python
#
#                               Copyright 2008
#                                     by
#                        The Board of Trustees of the
#                     Leland Stanford Junior University.
#                            All rights reserved.
#

__facility__ = "Online"
__abstract__ = "Cal config reporting classes"
__author__   = "Z. Fewtrell based on TkrXmlReport by P.A.Hart <philiph@SLAC.Stanford.edu> SLAC - GLAST LAT I&T/Online"
__date__     = "2008/01/25 00:00:00"
__updated__  = "$Date: 2008/06/09 23:45:42 $"
__version__  = "$Revision: 1.3 $"
__release__  = "$Name: v1r10p2 $"
__credits__  = "SLAC"

import logging, os

from ConfigXmlReport import *
from RootRptGenerator import SystemCommand
from CalPrecinctReport import *

# template for txt output filename
FN_SHORTSUM = "CAL_%s_shortSum.txt"

class CalXmlReport(PrecinctXmlReport):
    def __init__(self, precinctInfo, configData, type):
        PrecinctXmlReport.__init__(self, precinctInfo, configData)
        self.__type = type
        self._rootDataPath = configData.configRootFileName()
        self._baselineRootPath = configData.baselineRootFileName()
        self.__pngFileInfos = []

        # to be populated by CalPrecinctReport class
        self._precinctReport = None

        
    def createReport(self, rebuild=False):
        """
        generate all report img & data

        """
        self.createHeader()

        summary = self.addSection("CAL_%s_Summary" %(self.__type))

        self.addIntent(summary)  # blank intent node for later?

        # write TXT report to file & generate images
        self.shortSummary(self.path, rebuild)

        # read in nLines of TXT back from file
        self.includeText(summary, self._txtName, nLines=100)

        # insert images generated in shortSummary
        for info in self.__pngFileInfos:
            file = info.fileName
            caption = info.caption
            title = info.title
            self.addImage(summary, file, title, caption)
        self.addComment(summary, "empty comment")

    def shortSummary(self, path, rebuild=False):
        """
        Write TXT report to file && generate images for use in full report
        
        """
        # output TXT report
        self._txtName = os.path.join(path, FN_SHORTSUM % (self.__type))

        if not os.path.exists(self._txtName) or rebuild:
            self._precinctReport.createTXTReport(self._txtName)
            self.__pngFileInfos += self._precinctReport.makeImgs(self.path)

            
class CalModeXmlReport(CalXmlReport):
    def __init__(self, precinctInfo, configData):
        CalXmlReport.__init__(self, precinctInfo, configData, 'Mode')

        self._precinctReport = CalModeReport(self._rootDataPath,
                                             self._baselineRootPath)

                                              


class CalLacXmlReport(CalXmlReport):
    def __init__(self, precinctInfo, configData):
        CalXmlReport.__init__(self, precinctInfo, configData, 'Lac')

        self._precinctReport = CalLACReport(self._rootDataPath,
                                            self._baselineRootPath)


class CalFleXmlReport(CalXmlReport):
    def __init__(self, precinctInfo, configData):
        CalXmlReport.__init__(self, precinctInfo, configData, 'Fle')

        self._precinctReport = CalFLEReport(self._rootDataPath,
                                            self._baselineRootPath)


class CalFheXmlReport(CalXmlReport):
    def __init__(self, precinctInfo, configData):
        CalXmlReport.__init__(self, precinctInfo, configData, 'Fhe')

        self._precinctReport = CalFHEReport(self._rootDataPath,
                                            self._baselineRootPath)


class CalUldXmlReport(CalXmlReport):
    def __init__(self, precinctInfo, configData):
        CalXmlReport.__init__(self, precinctInfo, configData, 'Uld')

        self._precinctReport = CalULDReport(self._rootDataPath,
                                            self._baselineRootPath)

