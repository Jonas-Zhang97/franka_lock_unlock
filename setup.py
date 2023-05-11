import os
from glob import glob
from setuptools import setup


package_name = "franka_lock_unlock"
setup(
    name=package_name,
    version="0.0.0",
    packages=[package_name],
    data_files=[
        # Install marker file in the package index
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        # Include our package.xml file
        (os.path.join('share', package_name), ['package.xml']),
        # Include all launch files.
        (os.path.join('share', package_name), glob('launch/*launch.py')),
        (os.path.join('share', package_name), glob('launch/*.launch'))
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Andrew Madden",
    maintainer_email="andrew.madden@tum.de",
    description="ROS2 version ",
    license="TODO: License declaration",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": ["lock_unlock = franka_lock_unlock.__init__:main"],
    },
)
