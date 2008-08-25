# -*- python -*-
# $Header: /nfs/slac/g/glast/ground/cvs/GlastRelease-scons/configData/SConscript,v 1.1 2008/08/15 21:22:46 ecephas Exp $
# Authors: M. Kocian <kocian@slac.stanford.edu>
# Version: configData-01-10-04
Import('baseEnv')
Import('listFiles')
Import('packages')
progEnv = baseEnv.Clone()
libEnv = baseEnv.Clone()

libEnv.Tool('configDataLib', depsOnly = 1)

configData = libEnv.SharedLibrary('configData', listFiles(['src/*.cxx','src/gem/*.cxx',
	'src/fsw/*.cxx','src/base/*.cxx','src/db/*.cxx']))


progEnv.Tool('configDataLib')

if baseEnv['PLATFORM'] != 'win32':
	progEnv.AppendUnique(CCFLAGS = ['-Wno-unused-parameter'])



ConfigXml2Root = progEnv.Program('ConfigXml2Root',['apps/ConfigXml2Root.cxx'])
RootConfigCompare = progEnv.Program('RootConfigCompare',['apps/RootConfigCompare.cxx'])
findConfigs = progEnv.Program('findConfigs',['apps/findConfigs.cxx'])
dumpGemConfiguration = progEnv.Program('dumpGemConfiguration',['apps/dumpGemConfiguration.cxx'])
testdb = progEnv.Program('testdb',['apps/testdb.cxx'])
test_configData = progEnv.Program('test_configData',['src/test/test_configData.cxx'])

progEnv.Tool('registerObjects', package = 'configData', libraries = [configData],
	     testApps = [test_configData],
	     binaries = [ConfigXml2Root,RootConfigCompare,findConfigs,
			 dumpGemConfiguration,testdb],
	     includes = listFiles(['configData/*'], recursive = 1))

