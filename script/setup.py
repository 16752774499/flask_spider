from distutils.core import setup

from Cython.Build import cythonize

# language_level=3表示python3语法，否则会报错。生成的动态链接库不指定，则根据*.pyx的名字来生成（指定方法，cythonize（name="指定链接库名"））
setup(ext_modules=cythonize("tools.pyx", language_level=3))
