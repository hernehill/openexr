name = "openexr"

version = "3.1.12.hh.1.0.0"

authors = [
    "ILM & AcademySoftwareFoundation",
]

description = """Specification and reference of EXR file format"""

with scope("config") as c:
    import os

    c.release_packages_path = os.environ["HH_REZ_REPO_RELEASE_EXT"]

requires = [
    "imath", "zlib",
]

private_build_requires = []

variants = []


def commands():
    env.REZ_OPENEXR_ROOT = "{root}"
    env.OPENEXR_ROOT = "{root}"
    env.OPENEXR_LOCATION = "{root}"
    env.ILMBASE_ROOT = "{root}"
    env.ILMBASE_LOCATION = "{root}"

    env.OPENEXR_INCLUDE_DIR = "{root}/include"

    env.PATH.append("{root}/bin")
    env.PATH.append("{root}/lib")
    env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")


uuid = "repository.openexr"
