#!/bin/env python
#
#                               Copyright 2008
#                                     by
#                        The Board of Trustees of the
#                     Leland Stanford Junior University.
#                            All rights reserved.
#

__facility__ = "Online"
__abstract__ = "Timing config reporting classes"
__author__   = "P.A.Hart <philiph@SLAC.Stanford.edu> SLAC - GLAST LAT I&T/Online"
__date__     = "2008/01/25 00:00:00"
__updated__  = "$Date: 2008/06/09 23:45:42 $"
__version__  = "$Revision: 1.6 $"
__release__  = "$Name: v1r10p2 $"
__credits__  = "SLAC"

import logging, os

from ConfigXmlReport import *
from RootRptGenerator import SystemCommand
from BasicRootMacroRunner import *

FN_SHORTSUM = "%s_shortSum.txt"

class TimingXmlReport(PrecinctXmlReport):
    def __init__(self, precinctInfo, configData):
        PrecinctXmlReport.__init__(self, precinctInfo, configData)
        self.__precinctName = precinctInfo.getPrecinct()
        self.__confRootFile = configData.configRootFileName()
        
    def createReport(self, rebuild=False):
        self.createHeader()
        summary = self.addSection("%s_Summary" %(self.__precinctName))

        self.addIntent(summary)  # blank intent node for later?

        self.shortSummary(self.path, rebuild)
        self.includeText(summary, self.__builtName, isHtml=True)
        self.addComment(summary, "empty comment")

    def shortSummary(self, path, rebuild=False):
        self.__builtName = os.path.join(self.path, FN_SHORTSUM % (self.__precinctName))
        if not os.path.exists(self.__builtName) or rebuild:
            macroRunner = BasicRootMacroRunner(self.__precinctName, self.__confRootFile, self.__builtName)
            macroRunner.doChecks()
            
class AcdTimingXmlReport(TimingXmlReport):
    def __init__(self, precinctInfo, configData):
        TimingXmlReport.__init__(self, precinctInfo, configData)
class GnlModeXmlReport(TimingXmlReport):
    def __init__(self, precinctInfo, configData):
        TimingXmlReport.__init__(self, precinctInfo, configData)
class GnlTimingXmlReport(TimingXmlReport):
    def __init__(self, precinctInfo, configData):
        TimingXmlReport.__init__(self, precinctInfo, configData)
class CalTimingXmlReport(TimingXmlReport):
    def __init__(self, precinctInfo, configData):
        TimingXmlReport.__init__(self, precinctInfo, configData)
class TkrTimingXmlReport(TimingXmlReport):
    def __init__(self, precinctInfo, configData):
        TimingXmlReport.__init__(self, precinctInfo, configData)
