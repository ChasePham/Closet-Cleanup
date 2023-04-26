async function logJSONData() {
  const response = await fetch("http://localhost:4000");
  const jsonData = await response.json();
  console.log(jsonData);
    for(var i  = 1; i <= 6; i++) {
      var image_id = 'image_op_' + i + "";
      var brand_id = 'brand_' + i + "";
      var price_id = 'price_' + i + "";
      var class_id = 'image_link_' + i + "";
      document.getElementById(image_id).src=(""+jsonData['result'][0][i-1]+"");
      document.getElementById(brand_id).innerHTML=(""+jsonData['result'][2][i-1]+"");
      document.getElementById(price_id).innerHTML=(""+jsonData['result'][3][i-1]+"");
      document.getElementById(class_id).href=(""+jsonData['result'][1][i-1]+"");
    }
    for(var i = 1; i <= 3; i++) {
      var secondhand_img_id = 'image_second_' + i + "";
      var secondhand_link_id = 'second_link_' + i + "";
      document.getElementById(secondhand_img_id).src=(""+jsonData['result_two'][0][i-1]+"");
      document.getElementById(secondhand_link_id).href=(""+jsonData['result_two'][1][i-1]+"");
    }
}

logJSONData()

// // function to get the tabId of the current tab
// async function getTabId() {
//   let queryOptions = { active: true, currentWindow: true };
//   let tabs = await chrome.tabs.query(queryOptions);
//   return tabs[0].id;
// }