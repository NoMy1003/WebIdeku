# WebIdeku
WebIdeku login test automation cases

# What you need to do before trigger
## Make sure to run on Window OS
Since Windows and Mac got different code operation method

## Install python3
Make sure to install python3 and version higher than 3.11  

## Check install necessary pip list
pip install -r requirenents.txt  

## Make sure you use Selenium4
Check Selenium version by command : pip list  

# Trigger method
## Trigger all login cases
python .\RunTest.py -T WebIdekuLogin  

## Trigger single login case
python .\RunTest.py -T WebIdekuLogin-0001  

## Trigger multiple login case
python .\RunTest.py -T WebIdekuLogin-0001,WebIdekuLogin-0002  
