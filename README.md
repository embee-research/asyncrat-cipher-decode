# IronPyMalwareDecoder
Scripts related to the "Snakes on a Domain" Huntress Blog Post

Full Blog can be found here
https://www.huntress.com/blog/snakes-on-a-domain-an-analysis-of-a-python-malware-loader

The main script is a python implementation of the "Cipher" encoding function found in the malware described above. 

The cipher function takes a base64 input and a key, and implements a custom decoding routine to produce shellcode or a .NET RAT. 

This function is commonly found in malware loaded by IronPython, and is potentially related to the IronNetInjector used by Turla. 
Alternatively, this may just be a complex loader for an AsyncRAT infection. 

https://unit42.paloaltonetworks.com/ironnetinjector/


# Usage

`cipherdecode.py --file <filename.b64> --key <keyfrommalware>`

<img width="698" alt="image" src="https://user-images.githubusercontent.com/82847168/159846123-671865c7-da25-4147-b142-36099e7ac162.png">


# Samples

<img width="710" alt="image" src="https://user-images.githubusercontent.com/82847168/159845963-606eb4ec-02c8-451c-9d8e-a16cd2ec9f0c.png">





<img width="802" alt="image" src="https://user-images.githubusercontent.com/82847168/159845201-b13f13e0-04b7-4332-a75c-1ffd666effa5.png">


![image](https://user-images.githubusercontent.com/82847168/159845155-129016d9-1f46-4876-ab15-0a0539ce78f2.png)









# Original Code
![image](https://user-images.githubusercontent.com/82847168/159845314-2041010d-5083-437e-8884-113996e2e3a6.png)
