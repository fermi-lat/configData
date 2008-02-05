#!/bin/env python
#
#                               Copyright 2008
#                                     by
#                        The Board of Trustees of the
#                     Leland Stanford Junior University.
#                            All rights reserved.
#

__facility__ = "Online"
__abstract__ = "ACD config reporting classes"
__author__   = "P.A.Hart <philiph@SLAC.Stanford.edu> SLAC - GLAST LAT I&T/Online"
__date__     = "2008/01/25 00:00:00"
__updated__  = "$Date: 2008/02/01 22:50:54 $"
__version__  = "$Revision: 1.1 $"
__release__  = "$Name:  $"
__credits__  = "SLAC"

import logging

from PrecinctReport import *
from RootRptGenerator import SystemCommand
from AcdPlotChecker import *

FN_SHORTSUM = "%sACD_%s_shortSum.txt"

class AcdXmlReport(PrecinctXmlReport):
    def __init__(self, precinctInfo, configData):
        PrecinctXmlReport.__init__(self, precinctInfo, configData)
        self.__precinctName = precinctInfo.getPrecinct()
        self.__confRootFile = configData.configRootFileName()
        self.__baseRootFile = configData.baselineRootFileName()
        self.__compRootFile = configData.compareRootFileName()
        self.__pngFileInfos = []
        
    def createReport(self):
        self.createHeader()
        summary = self.addSection("ACD_%s_Summary" %(self.__precinctName))

        self.addIntent(summary)  # blank intent node for later?

        self.shortSummary(self.data.configDir, rebuild=True) ## rebuild for now
        self.includeText(summary, self.__builtName, nLines=10)
        for info in self.__pngFileInfos:
            file = info.fileName
            caption = info.caption
            title = info.title
            self.addImage(summary, file, title, caption)
        self.addComment(summary, "empty comment")

    def shortSummary(self, outputStub="", rebuild=False):
        self.__builtName = FN_SHORTSUM % (outputStub, self.__precinctName)
        if not os.path.exists(self.__builtName) or rebuild:
            fp = open(self.__builtName, 'w')
            fp.write("no comparison information available currently")
            fp.close()
            acdPlotChecker = AcdPlotChecker(self.__precinctName, self.__compRootFile)
            self.__pngFileInfos = acdPlotChecker.makePngs(outputStub)
            
class AcdBiasXmlReport(AcdXmlReport):
    def __init__(self, precinctInfo, configData):
        AcdXmlReport.__init__(self, precinctInfo, configData)

class AcdHldXmlReport(AcdXmlReport):
    def __init__(self, precinctInfo, configData):
        AcdXmlReport.__init__(self, precinctInfo, configData)
        
class AcdModeXmlReport(AcdXmlReport):
    def __init__(self, precinctInfo, configData):
        AcdXmlReport.__init__(self, precinctInfo, configData)

class AcdPHAXmlReport(AcdXmlReport):
    def __init__(self, precinctInfo, configData):
        AcdXmlReport.__init__(self, precinctInfo, configData)

class AcdTimingXmlReport(AcdXmlReport):
    def __init__(self, precinctInfo, configData):
        AcdXmlReport.__init__(self, precinctInfo, configData)
        ## Martin's domain - just #s
        
class AcdVetoXmlReport(AcdXmlReport):
    def __init__(self, precinctInfo, configData):
        AcdXmlReport.__init__(self, precinctInfo, configData)