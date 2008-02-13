#!/bin/env python
#
#                               Copyright 2008
#                                     by
#                        The Board of Trustees of the
#                     Leland Stanford Junior University.
#                            All rights reserved.
#

__facility__ = "Online"
__abstract__ = "Cal precinct report code"
__author__   = "Z.Fewtrell, based on TkrRegisterChecker by P.A.Hart <philiph@SLAC.Stanford.edu> SLAC - GLAST LAT I&T/Online"
__date__     = "2008/01/25 00:00:00"
__updated__  = "$Date: 2008/02/13 20:21:11 $"
__version__  = "$Revision: 1.7 $"
__release__  = "$Name:  $"
__credits__  = "SLAC"


import ROOT
# set batch mode (avoid plotting)
ROOT.gROOT.SetBatch(True)


class CalPrecinctReport(object):
  def __init__(self,
               precinctName,
               rootDataPath,
               baselineRootPath):
    """
    rootDataPath - path to LATC Root data for 'current' config
    baselineRootPath - path to LATC Root data for 'baseline' comparison
    """
    object.__init__(self)
    
    self._precinctName = precinctName

    # read in root files
    # path to 'current' LATC ROOT File
    self.__rootDataPath = rootDataPath
    # current LATC register data dictionary
    import LATCRootData
    self._cfgPrecinctData = LATCRootData.PrecinctData(self.__rootDataPath, self._precinctName)

    # optional baseline ROOT data
    if baselineRootPath == None:
      self.__baselineRootPath = None
      self._baselinePrecinctData = None
    else:
      self.__baselineRootPath = baselineRootPath
      self._baselinePrecinctData = LATCRootData.PrecinctData(self.__baselineRootPath, self._precinctName)

  def createTXTReport(self, filename):
    """
    Write TXT report data to output file.
    """
    txtFile = open(filename,'w')
    txtFile.close()

  def makeImgs(self, outputDir):
    """
    Generate image report files & return list describing each output img
    """
    return []


  def _genCCCDiff(self, regName, outputDir):
    """
    plot the difference (cfg - baseline) between two configs against GCCC id
    
    return:
    BasicPlotChecker.PlotInfo
    """

    import LATCRootData
    regInfo = LATCRootData.PRECINCT_INFO[self._precinctName][regName]
    title = "%s_%s_diff_vs_GCCC"%(self._precinctName, regName)
    caption = title
    
    regData = self._cfgPrecinctData.getRegisterData(regName)
    baselineData = self._baselinePrecinctData.getRegisterData(regName)
    diffData = [new - old for (new,old) in zip(regData,baselineData)]
    # extract GCCC index from global GCFE indeces
    import calConstant
    cccData = [calConstant.getCFEId(idx)[1] for idx in range(calConstant.GLOBAL_N_GCFE)]
    
    import ROOTPlotUtils
    return ROOTPlotUtils.make2DHist(cccData,
                                    diffData,
                                    title,
                                    caption,
                                    "GCCC",
                                    "%s diff (cfg - baseline)"%regName,
                                    outputDir,
                                    calConstant.NUM_GCCC,
                                    2*(regInfo.maxVal+1),
                                    calConstant.NUM_GCCC,
                                    regInfo.maxVal+1,
                                    0,
                                    -1*(regInfo.maxVal+1))

  def _genCCCPlot(self, regName, outputDir):
    """
    Plot CFE data against CCC id - write to img file

    return:
    BasicPlotChecker.PlotInfo
    """
    import LATCRootData
    regInfo = LATCRootData.PRECINCT_INFO[self._precinctName][regName]
    title = "%s_%s_vs_GCCC"%(self._precinctName, regName)
    caption = title

    regData = self._cfgPrecinctData.getRegisterData(regName)
    # extract GCCC index from global GCFE indeces
    import calConstant
    cccData = [calConstant.getCFEId(idx)[1] for idx in range(calConstant.GLOBAL_N_GCFE)]

    import ROOTPlotUtils
    return ROOTPlotUtils.make2DHist(cccData,
                                    regData,
                                    title,
                                    caption,
                                    "GCCC",
                                    regName,
                                    outputDir,
                                    calConstant.NUM_GCCC,
                                    regInfo.maxVal+1,
                                    calConstant.NUM_GCCC,
                                    regInfo.maxVal+1)
                                    
  def _genDiffHist(self, regName, outputDir):
    """
    Generated 1D histogram of (new - old) difference between settings

    return:
    BasicPlotChecker.PlotInfo object
    """

    import LATCRootData
    regInfo = LATCRootData.PRECINCT_INFO[self._precinctName][regName]

    title = "%s_%s_diff"%(self._precinctName, regName)
    caption = title

    cfgData = self._cfgPrecinctData.getRegisterData(regName)
    baselineData = self._baselinePrecinctData.getRegisterData(regName)
    diffData = [cfg - baseline for (cfg, baseline) in zip(cfgData, baselineData)]

    import ROOTPlotUtils
    return ROOTPlotUtils.make1DHist(diffData,
                                    title,
                                    caption,
                                    "%s diff (cfg - baseline)"%regName,
                                    "",
                                    outputDir,
                                    (regInfo.maxVal+1)*2,
                                    regInfo.maxVal+1,
                                    -1*(regInfo.maxVal+1))

  def _genScatterPlot(self, regName, outputDir):
    """
    Generate scatter plot between cfg and baseline settings

    return:
    BasicPlotChecker.PlotInfo object
    """

    import LATCRootData
    regInfo = LATCRootData.PRECINCT_INFO[self._precinctName][regName]

    title = "%s_%s_scatter"%(self._precinctName, regName)
    caption = title

    cfgData = self._cfgPrecinctData.getRegisterData(regName)
    baselineData = self._baselinePrecinctData.getRegisterData(regName)

    import ROOTPlotUtils
    return ROOTPlotUtils.make2DHist(baselineData,
                                    cfgData,
                                    title,
                                    caption,
                                    "BASELINE",
                                    "CFG",
                                    outputDir,
                                    regInfo.maxVal+1,
                                    regInfo.maxVal+1,
                                    regInfo.maxVal+1,
                                    regInfo.maxVal+1)

class CalThreshReport(CalPrecinctReport):
  """
  Code shared by various Cal threhold precincts (LAC,FLE,FHE,ULD)
  """
  def __init__(self,
               precinctName,
               rootDataPath,
               baselineRootPath):
    CalPrecinctReport.__init__(self,
                               precinctName,
                               rootDataPath,
                               baselineRootPath)

  def createTXTReport(self, filename):
    """
    Write TXT rpeort to otuput file
    """

    txtFile = open(filename,'w')

    self.basicTXTReport(txtFile)

    txtFile.close()

  def basicTXTReport(self, outFile):
    """
    Write basic Cal Threshold report to given output file
    """
    import calConstant
    regName = calConstant.THRESH_REG_NAME[self._precinctName]
    outFile.write("Nominal DAC slope: %f (%s)\n"%
                  (calConstant.NOMINAL_THRESH_DAC_SLOPE[regName],
                   calConstant.THRESH_DAC_SLOPE_UNITS[regName]))

    bcast_regName = "%s_bcast"%regName
    bcast_value = self._cfgPrecinctData.getRegisterData(bcast_regName)[0]
    outFile.write("Broadcast value: %d\n"%bcast_value)

    cfgData = self._cfgPrecinctData.getRegisterData(regName)
    nBcast = cfgData.count(bcast_value)
    outFile.write("Num Broadcast channels: %d of %d\n"%(nBcast, len(cfgData)))


  def makeImgs(self, outputDir):
    """
    Return list of BasicPlotChecker.PlotInfo objects
    """
    imgList = []

    import calConstant
    regName = calConstant.THRESH_REG_NAME[self._precinctName]

    import LATCRootData
    regInfo = LATCRootData.PRECINCT_INFO[self._precinctName][regName]
    import ROOTPlotUtils
    imgList.append(ROOTPlotUtils.make1DHist(self._cfgPrecinctData.getRegisterData(regName),
                                            "%s_%s_cfg_summary"%(self._precinctName,regName),
                                            "%s_%s_cfg_summary"%(self._precinctName,regName),
                                            regName,
                                            "",
                                            outputDir,
                                            regInfo.maxVal+1,
                                            regInfo.maxVal+1))

    if self._baselinePrecinctData is not None:
      imgList.append(ROOTPlotUtils.make1DHist(self._baselinePrecinctData.getRegisterData(regName),
                                              "%s_%s_baseline_summary"%(self._precinctName,regName),
                                              "%s_%s_baseline_summary"%(self._precinctName,regName),
                                              regName,
                                              "",
                                              outputDir,
                                              regInfo.maxVal+1,
                                              regInfo.maxVal+1))
      imgList.append(self._genScatterPlot(regName, outputDir))
      imgList.append(self._genDiffHist(regName, outputDir))

    return imgList

  

class CalLACReport(CalThreshReport):
  def __init__(self,
               rootDataPath,
               baselineRootPath):
    CalThreshReport.__init__(self,
                             "CAL_LAC",
                             rootDataPath,
                             baselineRootPath)
    
  def makeImgs(self, outputDir):
    imgList = CalThreshReport.makeImgs(self, outputDir)

    import calConstant
    regName = calConstant.THRESH_REG_NAME[self._precinctName]
    imgList.append(self._genCCCPlot(regName, outputDir))
    if self._baselinePrecinctData is not None:
      imgList.append(self._genCCCDiff(regName, outputDir))  
  

      
    return imgList

class CalFLEReport(CalThreshReport):
  def __init__(self,
               rootDataPath,
               baselineRootPath):
    CalThreshReport.__init__(self,
                               "CAL_FLE",
                               rootDataPath,
                               baselineRootPath)

  def makeImgs(self, outputDir):
    imgList = CalThreshReport.makeImgs(self, outputDir)

    import calConstant
    regName = calConstant.THRESH_REG_NAME[self._precinctName]
    imgList.append(self._genCCCPlot(regName, outputDir))
    if self._baselinePrecinctData is not None:
      imgList.append(self._genCCCDiff(regName, outputDir))  

    return imgList
  

class CalFHEReport(CalThreshReport):
  def __init__(self,
               rootDataPath,
               baselineRootPath):
    CalThreshReport.__init__(self,
                             "CAL_FHE",
                             rootDataPath,
                             baselineRootPath)
    
    


class CalULDReport(CalThreshReport):
  def __init__(self,
               rootDataPath,
               baselineRootPath):
    CalThreshReport.__init__(self,
                               "CAL_ULD",
                               rootDataPath,
                               baselineRootPath)

class CalModeReport(CalPrecinctReport):
  def __init__(self,
               rootDataPath,
               baselineRootPath):
    CalPrecinctReport.__init__(self,
                               "CAL_Mode",
                               rootDataPath,
                               baselineRootPath)

  def createTXTReport(self, filename):
    """
    Write TXT report data to output file.
    """
    txtFile = open(filename,'w')

    txtFile.write(self.calModeTXT(self._cfgPrecinctData))
    
    txtFile.close()

  def calModeTXT(self, precinctData):
    """
    Create string report of cal mode configuration
    """

    txtRpt = ""

    txtRpt += "precinct\t%s\tidx\t%s\t%s\t%s\tval\tfield_desc\n"%("register".ljust(20),
                                                                  "reg_val".ljust(12),
                                                                  "bcast_val".ljust(12),
                                                                  "field".ljust(20))
    # loop through all register groups in precinct
    import LATCRootData
    precinctInfo = LATCRootData.PRECINCT_INFO[self._precinctName]
    for (regName,regInfo) in precinctInfo.iteritems():
      regData = precinctData.getRegisterData(regName)
      
      
      # find bcast register if it exists
      # case 0: i am a 'bcast' register
      isBcast = (regName.find("bcast") >= 0)
      
      if isBcast:
        bcastRegName = regName
      else:
        # case 1: I will look for my bcast register
        bcastRegName = "%s_bcast"%regName
        
      if bcastRegName in precinctInfo.keys():
        bcastVal = precinctData.getRegisterData(bcastRegName)[0]
      else:
        bcastVal = None
        
      # loop through all registers in register group
      for idx in range(regInfo.nInstances):
        regVal = regData[idx]
        
        # only print individual registers that don't match the bcast
        if not isBcast and regVal == bcastVal:
          continue
        
        # handle case where no subfields defined
        if len(regInfo.fieldDict) == 0:
          txtRpt += "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n"%(self._precinctName,
                                                        regName.ljust(20),
                                                        idx,
                                                        ("0x%x"%regVal).ljust(12),
                                                        ("0x%x"%bcastVal).ljust(12),
                                                        "",
                                                        "",
                                                        "")
          
          # loop through all fields in register
        else:
          for (fieldName, fieldInfo) in regInfo.fieldDict.iteritems():
            txtRpt += "%s\t%s\t%s\t%s\t%s\t%s\t0x%x\t%s\n"%(self._precinctName,
                                                            regName.ljust(20),
                                                            idx,
                                                            ("0x%x"%regVal).ljust(12),
                                                            ("0x%x"%bcastVal).ljust(12),
                                                            fieldName.ljust(20),
                                                            fieldInfo.extractVal(regVal),
                                                            fieldInfo.desc)
        # per register instance
        txtRpt += "\n" 
        
    return txtRpt
    
