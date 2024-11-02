# WebIdeku
Web automation for Ideku

What you need to do before trigger:  

[Setup necessary pip list]  
  pip install -r requirements.txt  

[Make sure you use Selenium4]  
  Check Selenium version by using "pip list"  

Trigger:  
[Run all login cases]  
  python RunTest.py -T WebIdekuLogin  
  
[Run single login cases]  
  python RunTest.py -T WebIdekuLogin-0001  
  
[Run multiple login cases]  
  python RunTest.py -T WebIdekuLogin-0001,WebIdekuLogin-0002  
