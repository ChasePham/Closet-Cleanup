async function logJSONData() {
  const response = await fetch("http://localhost:4000");
  const jsonData = await response.json();
  console.log(jsonData);
  console.log(jsonData[0]['thumbnail']);
    for(var i  = 1; i <= 6; i++) {
      var image_id = 'image_op_' + i + "";
      var brand_id = 'brand_' + i + "";
      var price_id = 'price_' + i + "";
      document.getElementById(image_id).src=(""+jsonData[i-1]['thumbnail']+"");
      document.getElementById(image_id).href=(""+jsonData[i-1]['link']+"");
      document.getElementById(brand_id).innerHTML=(""+jsonData[i-1]['source']+"");
      document.getElementById(price_id).innerHTML=(""+jsonData[i-1]['price']+"");
    }
}

logJSONData()

// // function to get the tabId of the current tab
// async function getTabId() {
//   let queryOptions = { active: true, currentWindow: true };
//   let tabs = await chrome.tabs.query(queryOptions);
//   return tabs[0].id;
// }