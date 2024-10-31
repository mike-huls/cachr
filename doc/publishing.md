sh 
build project
`poetry build`

### TestPyPI
Set testpypi repository  
`poetry config repositories.testpypi https://test.pypi.org/legacy/`  

Set testpypi token  
`poetry config pypi-token.testpypi <YOUR TOKEN>`  

publish to testpypi  
`poetry publish -r testpypi`  

install and check  
`pip install --index-url https://test.pypi.org/simple/ cachr`  


### PyPI

Set pypi repository  
`poetry config pypi-token.pypi <YOUR TOKEN>`  

Publish to PyPi  
`poetry publish`  