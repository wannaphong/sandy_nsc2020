# -*- coding: utf-8 -*-
import wave, struct
import requests
 
Apikey=''
url = 'https://api.aiforthai.in.th/vaja'
headers = {'Apikey':Apikey,'Content-Type' : 'application/x-www-form-urlencoded'}

def ai4thai(text,filename):
    global headers
    params = {'text':text,'mode':'st'}
    response = requests.get(url, params=params, headers=headers)
    save_wav(response,filename)
 
def save_wav(response,filename):
    result = response.json()['output']['audio']['result']
    numChannels =response.json()['output']['audio']['numChannels']
    validBits = response.json()['output']['audio']['validBits']
    sizeSample=response.json()['output']['audio']['sizeSample']
    sampleRate=response.json()['output']['audio']['sampleRate']
    len(result), numChannels, validBits, sizeSample,sampleRate

    obj = wave.open(filename,'wb') 
    obj.setparams((1, int(validBits/8), sampleRate, 0, 'NONE', 'not compressed'))
    for i in range(sizeSample):
      value = int(result[i])
      data = struct.pack('<h', value)  
      obj.writeframesraw(data)
    obj.close()

 
# sending post request and saving response as response object
