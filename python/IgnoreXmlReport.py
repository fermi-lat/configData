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
__updated__  = "$Date: 2008/06/09 23:46:12 $"
__version__  = "$Revision: 1.1 $"
__release__  = "$Name: v1r10p2 $"
__credits__  = "SLAC"

import logging, os

from ConfigXmlReport import *

class IgnoreXmlReport(PrecinctXmlReport):
    def __init__(self, precinctInfo, configData):
        PrecinctXmlReport.__init__(self, precinctInfo, configData)
        
    def createReport(self, rebuild=False):
        self.createHeader()
        summary = self.addSection("%s_Summary" %(self.info.getPrecinct()))

        self.addIntent(summary)  # blank intent node for later?


    
            
