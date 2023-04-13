
  logJSONData()
  async function logJSONData() {
    const response = await fetch("http://localhost:4000");
    const jsonData = await response.json();
    console.log(jsonData);
  }
  
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