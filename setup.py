import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
	long_description = fh.read()

setuptools.setup(
	name="pygraphsearch",
	version="1.2.3",
	author="Abraham Murciano",
	author_email="abrahammurciano@gmail.com",
	description="A python package to search graphs.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/abrahammurciano/pygraphsearch",
	project_urls={
		"Bug Tracker": "https://github.com/abrahammurciano/pygraphsearch/issues",
	},
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	package_dir={"": "src"},
	package_data={"pygraphsearch": ["py.typed"]},
	packages=setuptools.find_packages(where="src"),
	python_requires=">=3.6",
)
