def addUrl(urls):
	url = input("Please enter the URL : ")
	urls.insert(len(urls), url)

def printAll(urls):
	for i, u in enumerate(urls, start=1):
		print(f"URL {i} : {u}")
	print("\n")
def printAllTabs(urls):
	for i, u in enumerate(urls, start=1):
		print(f"Tab no. {i} : {u}")
	print("\n")
def buildFile(urls):
	temp1 = 'chrome.browserAction.onClicked.addListener(function(tab) {chrome.tabs.create({url:"'
	temp2 = '"});});'
	with open("background.js", "w") as f:
		for u in urls:
			f.write(temp1 + u + temp2 + "\n")

def main():
	urls = []
	print("Welcome to Auto Tab Creator")
	addUrl(urls)
	printAll(urls)

	add = input("Do you want to add another URL ? (y/n)")
	while(add == "y"):
		addUrl(urls)
		printAll(urls)
		add = input("Do you want to add another URL ? (y/n)")
	print("These are the final tabs that would be opened : ")
	printAllTabs(urls)
	buildFile(urls)
	print("Please proceed to adding this directory as an extension.")
	print("i.e. Go to chrome://extensions in chrome, make sure developer mode is on")
	print("Then, click on Load unpacked and select this AutoOpenTabs directory")
	print("Your extension is now installed and you will be able to open all your tabs with a single click!")
	print("Thanks!")
	print("Created by Dhvanil Sanghvi.")

if __name__ == "__main__":
	main()