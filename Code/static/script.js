const rand = document.getElementById('form')

rand.addEventListener('submit', function(e){
  e.preventDefault()
  fetch('/data').then(function(res) {
    return res.json()
  }).then(function(json) {
    const h3 = document.querySelector('h3')
    console.log(h3)
    // Use the JSON data to populate these elements
    h3.innerHTML = json.sentence + json.num
    console.log(json.sentence)
  }).catch(function(err) {
    console.log(err.message)
  })
})




