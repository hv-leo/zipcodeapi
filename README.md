# zipcodeapi
This is a Web API, that uses zipcodelib, to provide a Rest interface to validate and format zipcodes.

- Pre-requisites: 
  - [Python3](https://www.python.org/downloads/)
  - [zipcodelib](https://github.com/hv-leo/zipcodelib)

### Installation
```
git clone https://github.com/hv-leo/zipcodelib
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

### Run the Tests
```
pip install -r requirements.txt
pytest
```

### Documentation
- With the server up and running, check the [OpenApi Specs](http://localhost:8000/docs).

## Authors:
- Leonardo Coelho: <leonardo.coelho@ua.pt>