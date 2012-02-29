# -*- python -*-
# $Header: /nfs/slac/g/glast/ground/cvs/GlastRelease-scons/configData/SConscript,v 1.14 2012/01/23 19:30:34 jrb Exp $
# Authors: M. Kocian <kocian@slac.stanford.edu>
# Version: configData-01-11-05
Import('baseEnv')
Import('listFiles')
Import('packages')
progEnv = baseEnv.Clone()
libEnv = baseEnv.Clone()

libEnv.Tool('addLinkDeps', package='configData', toBuild='shared')

configData = libEnv.SharedLibrary('configData',
                                  listFiles(['src/*.cxx','src/gem/*.cxx',
                                             'src/fsw/*.cxx','src/base/*.cxx',
                                             'src/db/*.cxx']))

progEnv.Tool('configDataLib')

if baseEnv['PLATFORM'] != 'win32':
    progEnv.AppendUnique(CCFLAGS = ['-Wno-unused-parameter'])


if baseEnv['PLATFORM'] != 'win32':
    ConfigXml2Root = progEnv.Program('ConfigXml2Root',
				     ['apps/ConfigXml2Root.cxx'])
    RootConfigCompare = progEnv.Program('RootConfigCompare',
					['apps/RootConfigCompare.cxx'])
    findConfigs = progEnv.Program('findConfigs',['apps/findConfigs.cxx'])
    dumpGemConfiguration=progEnv.Program('dumpGemConfiguration',
					 ['apps/dumpGemConfiguration.cxx'])
else:
    XGetoptObj = '#/lib/' + baseEnv['VARIANT'] + '/XGetopt.obj'
    ConfigXml2Root = progEnv.Program('ConfigXml2Root',
				     ['apps/ConfigXml2Root.cxx', XGetoptObj])
    RootConfigCompare=progEnv.Program('RootConfigCompare',
				      ['apps/RootConfigCompare.cxx',XGetoptObj])
    findConfigs = progEnv.Program('findConfigs',
				  ['apps/findConfigs.cxx', XGetoptObj])
    dumpGemConfiguration=progEnv.Program('dumpGemConfiguration',
					 ['apps/dumpGemConfiguration.cxx',
					  XGetoptObj])

testdb = progEnv.Program('testdb',['apps/testdb.cxx'])
test_configData = progEnv.Program('test_configData',
				  ['src/test/test_configData.cxx'])

progEnv.Tool('registerTargets', package = 'configData',
             libraryCxts = [[configData, libEnv]],
	     testAppCxts = [[test_configData, progEnv]],
	     binaryCxts =[[ConfigXml2Root,progEnv],[RootConfigCompare,progEnv],
                          [findConfigs,progEnv],[dumpGemConfiguration,progEnv],
                           [testdb,progEnv]],
	     includes = listFiles(['configData/*'], recursive = 1),
	     xml = ['xml/defaultTrgConfig.xml'])




