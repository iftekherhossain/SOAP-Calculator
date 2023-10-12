from fastapi import FastAPI, HTTPException, Request
from lxml import etree
import uvicorn
from math import sqrt

app = FastAPI()

@app.post("/soap_sos.asmx")
async def soap_sos(request: Request):
    # Retrieve the SOAP XML data from the request
    xml_data = await request.body()
    root = etree.fromstring(xml_data)
    intA = root.find(".//intA")
    intB = root.find(".//intB")
    num1 = int(intA.text)
    num2 = int(intB.text)

    s1 = num1**2
    s2 = num2**2
    result = s1+s2
    soap_sos_out = f"""
    <?xml version="1.0" encoding="utf-8"?>
    <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
                     xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
                     xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
        <soap12:Body>
            <SOSResponse>
                <SOSResult>{result}</SOSResult>
            </SOSResponse>
        </soap12:Body>
    </soap12:Envelope>
    """
    return soap_sos_out

@app.post("/soap_rmsd.asmx")
async def soap_rmsd(request: Request):
    # Retrieve the SOAP XML data from the request
    xml_data = await request.body()
    root = etree.fromstring(xml_data)
    intA = root.find(".//intA")
    intB = root.find(".//intB")
    num1 = int(intA.text)
    num2 = int(intB.text)

    s1 = num1**2
    s2 = num2**2
    result = sqrt(s1-s2)
    soap_sos_out = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
    <soap12:Body>
        <rmsdResponse>
        <rmsdResult>{result}</rmsdResult>
        </rmsdResponse>
    </soap12:Body>
    </soap12:Envelope>"""
    
    return soap_sos_out


if __name__ == '__main__':
    uvicorn.run(app, port=5000, host="127.0.0.6")