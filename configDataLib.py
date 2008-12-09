# $Header: /nfs/slac/g/glast/ground/cvs/GlastRelease-scons/configData/configDataLib.py,v 1.2 2008/08/25 20:26:16 ecephas Exp $
def generate(env, **kw):
    if not kw.get('depsOnly', 0):
        env.Tool('addLibrary', library = ['configData'])
    env.Tool('mootCoreLib')
    env.Tool('commonRootDataLib')
    env.Tool('addLibrary', library = env['rootLibs'])
    env.Tool('addLibrary', library = env['pythonLibs'])
    env.Tool('lsfDataLib')
def exists(env):
    return 1;
