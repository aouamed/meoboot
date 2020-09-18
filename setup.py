from distutils.core import setup
import setup_translate


setup(name = 'enigma2-plugin-extensions-meoboot',
		version='1.4.1',
		author='aouamedj',
		author_email='aouamed@gmail.com',
                package_dir = {'Extensions.Meoboot': ''},
		packages=['Extensions.Meoboot'],
		package_data={'Extensions.Meoboot': ['*.png', '*.sh']},
		description = 'Meoboot and manual flashing image',
		cmdclass = setup_translate.cmdclass,
	)


