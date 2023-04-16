
  logJSONData()
  async function logJSONData() {
    const response = await fetch("http://localhost:4000");
    const jsonData = await response.json();
    console.log(jsonData);
  }
  var xhr = new XMLHttpRequest();
  xhr.open('GET', '/data');
  xhr.onload = function() {
      if (xhr.status === 200) {
          var data = JSON.parse(xhr.responseText);
          console.log(data.message);
      }
  };
  xhr.send();
  function sayHello() {
    console.log("Hello, World!");
  }