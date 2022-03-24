



import base64,gzip,shutil,sys
import argparse,gzip

parser = argparse.ArgumentParser()
parser.add_argument("--file", type=str,required=False)
parser.add_argument("--b64",type=str,required=False)
parser.add_argument('--key', type=str, required=False)
parser.add_argument('--encipher', type=str, required=False, default=False)
parser.add_argument('--save', type=str, required=False, default="output.bin")
args = parser.parse_args()

#Exit if no arguments are present
if not (args.file or args.b64 or args.key):
    print("Please enter input data using --file or --b64")
    sys.exit(1)


#Python implementation of the mod function found in the original malware code
def modcustom(a,b):
    result = ((a%b + b) % b )
    return result

#Python implementation of the cipher function found in the original malware code
#This functions contains the primary decoding logic for the malware
def cipher(encoded, key, encipher):
    out =""
    num = 0
    num2 = 0
    j = 0
    index = 0
    c = ""
    charIsUpper = False
    for j in range(0, len(encoded)):
        if encoded[j].isalpha():
            charIsUpper = encoded[j].isupper()
            if charIsUpper:
                c = "A"
            else:
                c = "a"

            index = (j - num) % len(key)
            if charIsUpper:
                num2 = ord(key[index].upper()) - ord(c)
            else:
                num2 = ord(key[index].lower()) - ord(c)
            #negate value if encipher set to true
            if encipher:
                num2 = num2
            else:
                num2 = -num2
            out += (chr((modcustom(ord(encoded[j]) + num2 - ord(c),26) + ord(c))))
        else:
            out += str(encoded[j])
            num +=1

    return out

def main():
    #Open and read in the input and output files
    f = open(args.file, "r")
    out = open(args.save, "wb")
    encoded = str(f.read())

    #read in the key and encipher flag from CLI arguments
    encipher = args.encipher
    key = args.key

    #execute the cipher decoder on the input
    b64text = cipher(encoded,key,encipher)
    #base64 decode the resulting data
    compressed = bytearray(base64.b64decode(b64text))

    #decompress the resulting data, and write the result to a file
    try:
        out.write(gzip.decompress(compressed))
        print("\nwrote {} bytes to {}".format(len(compressed),args.save))
    except Exception as e:
        print("error writing output to file")
        print(e)
    #close the remaining handles
    f.close()
    out.close()

if __name__ == "__main__":
    main()
