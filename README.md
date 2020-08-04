# auto-open-tabs
A Chrome extension to auto open particular tabs when clicked on.   
   
I am a student and every morning when I open my laptop, I have this routine of opening my personal and college mails and my trading account. I thought about automating the   process. Here is the result. It's an easy to use chrome extension.    
What it does is, on clickcing the extension icon, it will open all the tabs that you've selected, automatically.    
You can program it to open as many tabs as you like.   
   
## How to use it?   
Just clone this repo to your own machine.   
   
### Modifying for your own requirement   
In the file - "manifest.json", you can see the function call for different tabs.   
   
Modify the file "background.js" -    
Copy the following three lines of code and insert the url inside the quotes in the second line :   
   
chrome.browserAction.onClicked.addListener(function(tab) {   
  chrome.tabs.create({url: ""});   
});   
   
To add more tabs to auto open, just append "background.js" with the same 3 lines, with a different URL.   
   
### Adding to Chrome   
   
Goto chrome://extensions in your chrome browser.   
Enable "developer mode" in the upper right corner.   
Then hit "Load Unpacked" and select the directory - AutoOpenTabs from the directory where you cloned this project.   
The extension is now added and working. Look out for the "O" icon in the extensions with the description - "Open your day to day tabs".   
You can also pin it.   
