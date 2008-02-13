#!/bin/env python
#
#                               Copyright 2008
#                                     by
#                        The Board of Trustees of the
#                     Leland Stanford Junior University.
#                            All rights reserved.
#

__facility__ = "Online"
__abstract__ = "PyROOT based plotting utilties"
__author__   = "Z. Fewtrell"
__date__     = "2008/01/25 00:00:00"
__updated__  = "$Date: 2008/02/12 13:04:08 $"
__version__  = "$Revision: 1.5 $"
__release__  = "$Name:  $"
__credits__  = "SLAC"

import ROOT
# set batch mode (avoid plotting)
ROOT.gROOT.SetBatch(True)

def __saveHist(hist,
               title,
               outputDir,
               caption):
    """
    Save histogram to image (png) file.

    return BasicPlotChecker.PlotInfo object
    """

    hist.Draw()
    imgPath = outputDir + '/' + title + ".png"
    ROOT.gPad.SaveAs(imgPath)
    

    # create img file record for use in report builder
    import BasicPlotChecker
    plotInfo = BasicPlotChecker.PlotInfo()
    plotInfo.save(imgPath, title, caption)

    return plotInfo

def make1DHist(data,
               title,
               caption,
               xTitle,
               yTitle,
               outputDir,
               nbins,
               xmax,
               xmin=0):
    """
    Create 1D ROOT Histogram plot, save to file.

    args:
    data - 1-D sequence of data
    title - should be valid as part of a filename
    caption - can be longer & can contain any characters.
    xTitle - x axis title
    yTitle - y axis title
    outputDir - output directory for image file.
    nbins - number of histogram bins
    xmax - x axis max value
    xmin - x axis minium value:

    return:
    BasicPlotChecker.PlotInfo object
    """

    # create histogram object
    hist = ROOT.TH1I(title, title,
                     nbins, xmin, xmax)
    hist.SetXTitle(xTitle)
    hist.SetYTitle(yTitle)

    # fill histogram
    import array
    hist.FillN(len(data),
             array.array('d',data),
             array.array('d',[1]*len(data)))

    return __saveHist(hist, title, outputDir, caption)

    
    
    
def make2DHist(xPts,
               yPts,
               title,
               caption,
               xTitle,
               yTitle,
               outputDir,
               nBinsX,
               nBinsY,
               xMax,
               yMax,
               xMin=0,
               yMin=0):
    """
    Create 2D ROOT Histogram plot, save to file.

    args:
    xData - 1-D sequence of x-values
    yData - 2-D sequence of y-values
    title - should be valid as part of a filename
    caption - can be longer & can contain any characters.
    xTitle - x axis title
    yTitle - y axis title
    outputDir - output directory for image file.
    nbinsX - number of histogram bins on x axis
    nbinsY - number of histogram bins on y axis
    xMax, xMin, yMax, yMin - axis limits

    return:
    BasicPlotChecker.PlotInfo object
    """

    # create histogram object
    hist = ROOT.TH2I(title, title,
                     nBinsX, xMin, xMax,
                     nBinsY, yMin, yMax)
    hist.SetXTitle(xTitle)
    hist.SetYTitle(yTitle)
    hist.SetMarkerStyle(ROOT.kFullTriangleUp)
    hist.SetMarkerSize(2)


    # fill histogram
    import array
    hist.FillN(len(xPts),
               array.array('d', xPts),
               array.array('d', yPts),
               array.array('d',[1]*len(xPts)))

    return __saveHist(hist, title, outputDir, caption)


                            
    
               
                    
               
               
