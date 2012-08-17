# $Header: /nfs/slac/g/glast/ground/cvs/GlastRelease-scons/configData/configDataLib.py,v 1.4 2009/01/23 00:20:54 ecephas Exp $
def generate(env, **kw):
    if not kw.get('depsOnly', 0):
        env.Tool('addLibrary', library = ['configData'])
        if env['PLATFORM']=='win32' and env.get('CONTAINERNAME','')=='GlastRelease':
	    env.Tool('findPkgPath', package = 'configData') 
    env.Tool('mootCoreLib')
    env.Tool('commonRootDataLib')
    env.Tool('addLibrary', library = env['rootLibs'])
    env.Tool('addLibrary', library = env['pythonLibs'])
    env.Tool('lsfDataLib')
    if env['PLATFORM']=='win32' and env.get('CONTAINERNAME','')=='GlastRelease':
        env.Tool('findPkgPath', package = 'enums') 
def exists(env):
    return 1;
