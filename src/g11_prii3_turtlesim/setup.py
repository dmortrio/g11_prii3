import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'g11_prii3_turtlesim'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dylan',
    maintainer_email='dylan@todo.todo',
    description='Paquete de control de turtlesim para el grupo 11',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'turtle_drawer = g11_prii3_turtlesim.turtle_drawer:main',
        ],
    },
)
