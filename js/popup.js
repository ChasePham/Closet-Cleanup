// listening for a click event on the #DanceOn <button>
document.getElementById("DanceOn").addEventListener('click', async () => {

    // get the ID of the current tab
    tabId = await getTabId()
  
    // send a message to the content script running in the tab with tabId
    chrome.tabs.sendMessage(tabId, "dance_on", (response) => {
      // for testing purposes
      // alert('successfully sent message to content script');
      
      // EXTRA CODE NOT COVERED IN WORKSHOP
      // get a response from the content script
      if (response === 'success') {
        // do something after you find receive a response/reply
        // from content.js that the message has been received successfully 
        console.log("YES");
      } else {
        console.log("NO");
      }
    });
  
  });
  
  
  // function to get the tabId of the current tab
  async function getTabId() {
    let queryOptions = { active: true, currentWindow: true };
    let tabs = await chrome.tabs.query(queryOptions);
    return tabs[0].id;
  }
  
  function myFunction() {
    var x = document.getElementById("myLinks");
    if (x.style.display === "block") {
      x.style.display = "none";
    } else {
      x.style.display = "block";
    }
  }