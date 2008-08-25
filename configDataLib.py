# $Header: /nfs/slac/g/glast/ground/cvs/GlastRelease-scons/configData/configDataLib.py,v 1.1 2008/08/15 21:42:38 ecephas Exp $
def generate(env, **kw):
    if not kw.get('depsOnly', 0):
        env.Tool('addLibrary', library = ['configData'])
    env.Tool('mootCoreLib')
    env.Tool('commonRootDataLib')
def exists(env):
    return 1;
