VERSION = '0.0.1'
APPNAME = 'redsvd'

srcdir = '.'
blddir = 'bin'

def set_options(ctx):
  ctx.tool_options('compiler_cxx')
  ctx.tool_options('unittestt')

def configure(ctx):
  ctx.check_tool('compiler_cxx')
  ctx.check_tool('unittestt')	
  ctx.check_cfg(package = 'eigen3')
  ctx.env.CXXFLAGS += ['-O2', '-Wall', '-g']

def build(bld):
  bld.recurse('src')
