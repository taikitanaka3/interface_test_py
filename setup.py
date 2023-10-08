from setuptools import setup
import os
import glob
package_name = 'interface_test'
submodules = [
    'interface_test/util']
setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name] + submodules,
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob.glob('launch/*xml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Taiki Tanaka',
    maintainer_email='taiki.tanaka@toer4.jp',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'interface_test_node = interface_test.interface_test:main',
        ],
    },
)
