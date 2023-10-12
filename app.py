from fastapi import FastAPI, Form
from fastapi.templating import Jinja2Templates
import uvicorn
import requests
import re
from fastapi.responses import JSONResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.post("/add")
async def add(num1: int = Form(0), num2: int = Form(0)):
    print(num1,num2)
    data = f"""
    <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
      <soap12:Body>
        <Add xmlns="http://tempuri.org/">
          <intA>{num1}</intA>
          <intB>{num2}</intB>
        </Add>
      </soap12:Body>
    </soap12:Envelope>
    """

    # URL for the SOAP service
    url = "http://www.dneonline.com/calculator.asmx"
    headers = {'content-type': 'text/xml'}

    # Sending the SOAP request for card type
    response = requests.post(url, data=data, headers=headers)
    print(response.text)
    res = re.search(
        "<AddResult>(.*)</AddResult>", response.text)

    try:
        result = res.group(1)
    except:
        result = "Invalid"

    # Returning the response with template rendering
    return JSONResponse(content={"result": result})

@app.post("/sub")
async def sub(num1: int = Form(0), num2: int = Form(0)):
    # print(num1,num2)
    data = f"""
    <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
      <soap12:Body>
        <Subtract xmlns="http://tempuri.org/">
          <intA>{num1}</intA>
          <intB>{num2}</intB>
        </Subtract>
      </soap12:Body>
    </soap12:Envelope>
    """
    url = "http://www.dneonline.com/calculator.asmx"
    headers = {'content-type': 'text/xml'}
    response = requests.post(url, data=data, headers=headers)
    print(response.text)
    res = re.search(
        "<SubtractResult>(.*)</SubtractResult>", response.text)
    try:
        result = res.group(1)
    except:
        result = "Invalid"
    return JSONResponse(content={"result": int(result)})

@app.post("/mul")
async def mul(num1: int = Form(0), num2: int = Form(0)):
    data = f"""
    <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
      <soap12:Body>
        <Multiply xmlns="http://tempuri.org/">
          <intA>{num1}</intA>
          <intB>{num2}</intB>
        </Multiply>
      </soap12:Body>
    </soap12:Envelope>
    """
    url = "http://www.dneonline.com/calculator.asmx"
    headers = {'content-type': 'text/xml'}
    response = requests.post(url, data=data, headers=headers)
    print(response.text)
    res = re.search(
        "<MultiplyResult>(.*)</MultiplyResult>", response.text)
    try:
        result = res.group(1)
    except:
        result = "Invalid"
    return JSONResponse(content={"result": int(result)})

@app.post("/div")
async def div(num1: int = Form(0), num2: int = Form(0)):
    data = f"""
    <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
      <soap12:Body>
        <Divide xmlns="http://tempuri.org/">
          <intA>{num1}</intA>
          <intB>{num2}</intB>
        </Divide>
      </soap12:Body>
    </soap12:Envelope>
    """
    url = "http://www.dneonline.com/calculator.asmx"
    headers = {'content-type': 'text/xml'}
    response = requests.post(url, data=data, headers=headers)
    print(response.text)
    res = re.search(
        "<DivideResult>(.*)</DivideResult>", response.text)
    try:
        result = res.group(1)
    except:
        result = "Invalid"
    return JSONResponse(content={"result": int(result)})

@app.post("/sos")
async def sos(num1: str = Form(0), num2: str = Form(0)):
    data = f"""
    <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
      <soap12:Body>
        <SOS>
          <intA>{num1}</intA>
          <intB>{num2}</intB>
        </SOS>
      </soap12:Body>
    </soap12:Envelope>
    """
    url = "http://127.0.0.6:5000/soap_sos.asmx"
    headers = {'content-type': 'text/xml'}
    response = requests.post(url, data=data, headers=headers)
    print(response.text)
    res = re.search(
        "<SOSResult>(.*)</SOSResult>", response.text)
    try:
        result = res.group(1)
    except:
        result = "Invalid"
    return JSONResponse(content={"result": int(result)})

@app.post("/rmsd")
async def rmsd(num1: int = Form(0), num2: int = Form(0)):
    data = f"""
    <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
      <soap12:Body>
        <rmsd>
          <intA>{num1}</intA>
          <intB>{num2}</intB>
        </rmsd>
      </soap12:Body>
    </soap12:Envelope>
    """
    url = "http://127.0.0.6:5000/soap_rmsd.asmx"
    headers = {'content-type': 'text/xml'}
    response = requests.post(url, data=data, headers=headers)
    print(response.text)
    res = re.search(
        "<rmsdResult>(.*)</rmsdResult>", response.text)
    try:
        result = res.group(1)
    except:
        result = "Invalid"
    return JSONResponse(content={"result": result})



if __name__ == '__main__':
    uvicorn.run(app, port=5000, host="127.0.0.4")