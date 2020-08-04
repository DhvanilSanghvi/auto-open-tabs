chrome.browserAction.onClicked.addListener(function(tab) {
  chrome.tabs.create({url:"https://mail.google.com/mail/u/0/"});
});
chrome.browserAction.onClicked.addListener(function(tab) {
  chrome.tabs.create({url:"https://mail.google.com/mail/u/1/"});
});
chrome.browserAction.onClicked.addListener(function(tab) {
  chrome.tabs.create({url:"https://kite.zerodha.com/"});
});