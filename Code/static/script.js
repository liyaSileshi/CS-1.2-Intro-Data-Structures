const rand = document.getElementById('form')
const slidesInner = slides.querySelector('.slides-inner')
const text = document.getElementById('textSlide')
const sub_button = document.getElementById('random_sentence')
const num = rand.querySelector("input[type='number']")
const sentence = document.querySelector('h3')
const fav = document.getElementById('favorite')
let json_sentence = ''

sub_button.addEventListener('click', function(e){
  let q = 10
  if (num.value) {
    q = num.value
  }

  // /data?q=${q}&book=a
  fetch(`/data?q=${q}`).then(function(res) {
    return res.json()
  }).then(function(json) {
    
    mySlides.nextSlide()
    // Use the JSON data to populate these elements
    // console.log(json.sentence)
    sentence.innerHTML = json.sentence 
    json_sentence = json // { sentence: "Hello World" } 
    // console.log(json_sentence)

  }).catch(function(err) {
    console.error(err.message)
  })
})

fav.addEventListener('click', function(e){
  console.log("It's getting clicked!")
  console.log(json_sentence)

  // JSON.stringify(json_sentence)

  const url = `/favorites?sentence=${json_sentence.sentence}`
  fetch(url).then(function(res){
    return res.json()
  }).then(function(json){
    console.log(json)
  }).catch(function(err){
    console.log(err.message)
  })
  
  // foo(url).then()
})

const slideshow = document.querySelector('.ms-slide-show')
const mySlides = makeSlideshow(slideshow)
